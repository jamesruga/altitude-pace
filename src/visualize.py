import folium
import matplotlib.pyplot as plt
import numpy as np

def generate_telemetry_chart():
    """Generates the static telemetry distribution chart."""
    labels = ['Optimal Pacing', 'Moderate Fatigue', 'High Fatigue Risk']
    sizes = [62, 26, 12]
    colors = ['#2ecc71', '#e67e22', '#e74c3c']

    fig, ax = plt.subplots(figsize=(8, 4.5), facecolor='#0d1117')
    ax.set_facecolor('#0d1117')

    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        autopct='%1.0f%%', 
        startangle=140, 
        colors=colors,
        textprops=dict(color="w", weight="bold")
    )

    plt.setp(autotexts, size=11, weight="bold")
    ax.set_title("AltitudePace Telemetry & Fatigue Breakdown", color="white", fontsize=14, pad=15, weight="bold")

    plt.tight_layout()
    plt.savefig("docs/telemetry_chart.png", dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

def generate_interactive_map():
    """Generates the rich Leaflet telemetry route map."""
    # High-altitude route coordinates (Eldoret to Iten elevation profile corridor)
    waypoints = [
        {"coords": [0.5143, 35.2698], "name": "Eldoret Start (2,090m)", "pace": "3:10 min/km", "hr_drift": "+0.5%", "status": "Optimal", "color": "#2ecc71"},
        {"coords": [0.5500, 35.3100], "name": "5K Split - Chepkoilel", "pace": "3:12 min/km", "hr_drift": "+1.2%", "status": "Optimal", "color": "#2ecc71"},
        {"coords": [0.6000, 35.3800], "name": "12K Split - Moiben Junction", "pace": "3:18 min/km", "hr_drift": "+3.4%", "status": "Moderate Fatigue", "color": "#e67e22"},
        {"coords": [0.6500, 35.4500], "name": "18K Split - Sergoit Ascent", "pace": "3:28 min/km", "hr_drift": "+6.8%", "status": "High Fatigue Risk", "color": "#e74c3c"},
        {"coords": [0.6783, 35.5083], "name": "Iten Finish - High Altitude Camp (2,400m)", "pace": "3:15 min/km", "hr_drift": "+4.1%", "status": "Optimal Recovery", "color": "#2ecc71"}
    ]

    start_lat, start_lon = waypoints[0]["coords"]
    m = folium.Map(location=[start_lat + 0.08, start_lon + 0.12], zoom_start=11, tiles="OpenStreetMap")

    # Add color-coded route segments
    for i in range(len(waypoints) - 1):
        p1 = waypoints[i]
        p2 = waypoints[i+1]
        
        folium.PolyLine(
            locations=[p1["coords"], p2["coords"]],
            color=p2["color"],
            weight=5,
            opacity=0.85,
            popup=f"Segment {i+1}: {p1['name']} ➔ {p2['name']}"
        ).add_to(m)

    # Add markers for key splits
    for wp in waypoints:
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; min-width: 180px;">
            <h4 style="margin: 0 0 5px 0; color: #2c3e50;">{wp['name']}</h4>
            <hr style="margin: 5px 0; border: 0.5px solid #ccc;">
            <b>GAP Pace:</b> {wp['pace']}<br>
            <b>HR Drift Decay:</b> {wp['hr_drift']}<br>
            <b>Status:</b> <span style="color: {wp['color']}; font-weight: bold;">{wp['status']}</span>
        </div>
        """
        
        folium.Marker(
            location=wp["coords"],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=wp["name"],
            icon=folium.Icon(color="green" if wp["color"] == "#2ecc71" else ("orange" if wp["color"] == "#e67e22" else "red"), icon="play" if "Start" in wp["name"] else ("flag" if "Finish" in wp["name"] else "info-sign"))
        ).add_to(m)

    m.save("docs/index.html")

if __name__ == "__main__":
    generate_telemetry_chart()
    generate_interactive_map()
