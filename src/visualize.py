import os
import folium
import pandas as pd
from src.engine import AltitudePaceEngine

def render_telemetry_map():
    data_path = "data/runner_telemetry.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Missing {data_path}")
        
    df = pd.read_csv(data_path)
    engine = AltitudePaceEngine()
    df['fatigue_level'] = engine.classify_fatigue(df)
    
    # Coordinates centered near Eldoret high-altitude training grounds
    base_lat, base_lon = 0.5143, 35.2698
    df['lat'] = base_lat + (df['distance_m'] * 0.000008)
    df['lon'] = base_lon + (df['distance_m'] * 0.000005)
    
    m = folium.Map(location=[base_lat, base_lon], zoom_start=13, tiles="OpenStreetMap")
    
    # Plot route points with color-coded fatigue markers
    color_map = {
        'Optimal Pacing': 'green',
        'Moderate Fatigue': 'orange',
        'High Fatigue (Risk of Collapse)': 'red'
    }
    
    for idx, row in df.iloc[::20].iterrows():
        color = color_map.get(row['fatigue_level'], 'blue')
        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"HR: {row['heart_rate_bpm']:.1f} BPM | Elev: {row['elevation_m']:.1f}m | Status: {row['fatigue_level']}"
        ).add_to(m)
        
    os.makedirs("docs", exist_ok=True)
    map_path = "docs/index.html"
    m.save(map_path)
    print(f"[Visualizer] Interactive telemetry map rendered to {map_path}")

if __name__ == "__main__":
    render_telemetry_map()
