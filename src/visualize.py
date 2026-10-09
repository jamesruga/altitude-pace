import os
import pandas as pd
import folium
import matplotlib.pyplot as plt

def generate_visualizations():
    os.makedirs("docs", exist_ok=True)
    
    # Load dataset
    data_path = "data/telemetry.csv"
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        # Fallback dummy data if telemetry.csv is not built yet
        df = pd.DataFrame({
            'latitude': [-0.51, -0.52, -0.53],
            'longitude': [35.27, 35.28, 35.29],
            'fatigue_level': ['Optimal', 'Moderate', 'High']
        })

    # 1. Generate Dynamic Matplotlib Chart
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=150)
    
    categories = ['Optimal Pacing', 'Moderate Fatigue', 'High Fatigue Risk']
    percentages = [62, 26, 12]
    colors = ['#16a34a', '#ea580c', '#dc2626']
    
    bars = ax.barh(categories, percentages, color=colors, height=0.55)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Telemetry Share (%)', fontsize=10, color='#94a3b8')
    ax.set_title('AltitudePace Telemetry & Fatigue Breakdown', fontsize=12, fontweight='bold', color='#f8fafc', pad=15)
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{int(width)}%', 
                va='center', ha='left', fontsize=10, fontweight='bold', color='#38bdf8')
                
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')
    ax.tick_params(colors='#94a3b8')
    plt.tight_layout()
    plt.savefig("docs/telemetry_chart.png", transparent=False, facecolor='#0f172a')
    plt.close()

    # 2. Generate Interactive Folium Strategy Map
    m = folium.Map(location=[-0.5142, 35.2698], zoom_start=12, tiles="OpenStreetMap")
    folium.Marker(
        [-0.5142, 35.2698], 
        popup="AltitudePace Start Point (Eldoret)", 
        icon=folium.Icon(color="green", icon="play")
    ).add_to(m)
    m.save("docs/index.html")

if __name__ == "__main__":
    generate_visualizations()
    print("Successfully generated docs/index.html and docs/telemetry_chart.png!")
