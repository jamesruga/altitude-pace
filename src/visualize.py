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

def generate_map_preview_image():
    """Generates a static preview PNG of the color-coded elevation route for the README."""
    waypoints = [
        {"coords": [35.2698, 0.5143], "name": "Eldoret Start", "color": "#2ecc71"},
        {"coords": [35.3100, 0.5500], "name": "5K Split", "color": "#2ecc71"},
        {"coords": [35.3800, 0.6000], "name": "12K Split", "color": "#e67e22"},
        {"coords": [35.4500, 0.6500], "name": "18K Split", "color": "#e74c3c"},
        {"coords": [35.5083, 0.6783], "name": "Iten Finish", "color": "#2ecc71"}
    ]

    lons = [wp["coords"][0] for wp in waypoints]
    lats = [wp["coords"][1] for wp in waypoints]

    fig, ax = plt.subplots(figsize=(9, 4.5), facecolor='#0d1117')
    ax.set_facecolor('#161b22')

    # Draw color-coded segment polylines
    for i in range(len(waypoints) - 1):
        p1 = waypoints[i]
        p2 = waypoints[i+1]
        ax.plot(
            [p1["coords"][0], p2["coords"][0]], 
            [p1["coords"][1], p2["coords"][1]], 
            color=p2["color"], 
            linewidth=4, 
            solid_capstyle='round',
            label=p2["name"]
        )

    # Plot waypoints
    for wp in waypoints:
        ax.scatter(wp["coords"][0], wp["coords"][1], color=wp["color"], s=100, zorder=5, edgecolor='white', linewidth=1.5)
        ax.annotate(
            wp["name"], 
            (wp["coords"][0], wp["coords"][1]), 
            textcoords="offset points", 
            xytext=(0, 10), 
            ha='center', 
            color='white', 
            fontsize=9, 
            weight='bold'
        )

    ax.set_title("Eldoret-to-Iten Route Telemetry & Fatigue Hotspots", color="white", fontsize=13, weight="bold", pad=12)
    ax.tick_params(colors='gray', labelsize=8)
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['top'].set_color('#30363d')
    ax.spines['right'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.grid(True, linestyle='--', alpha=0.2, color='gray')
    ax.set_xlabel("Longitude (°E)", color="gray", fontsize=9)
    ax.set_ylabel("Latitude (°N)", color="gray", fontsize=9)

    plt.tight_layout()
    plt.savefig("docs/map_preview.png", dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

def generate_interactive_map():
    """Generates the rich Leaflet telemetry route map."""
    waypoints = [
        {"coords": [0.5143, 35.2698], "name": "Eldoret Start (2,090m)", "pace": "3:10 min/km", "hr_drift": "+0.5%", "status": "Optimal", "color": "#2ecc71"},
        {"coords": [0.5500, 35.3100], "name": "5K Split - Chepkoilel", "pace": "3:12 min/km", "hr_drift": "+1.2%", "status": "Optimal", "color": "#2ecc71"},
        {"coords": [0.6000, 35.3800], "name": "12K Split - Moiben Junction", "pace": "3:18 min/km", "hr_drift": "+3.4%", "status": "Moderate Fatigue", "color": "#e67e22"},
        {"coords": [0.6500, 35.4500], "name": "18K Split - Sergoit Ascent", "pace": "3:28 min/km", "hr_drift": "+6.8%", "status": "High Fatigue Risk", "color": "#e74c3c"},
        {"coords": [0.6783, 35.5083], "name": "Iten Finish - High Altitude Camp (2,400m)", "pace": "3:15 min/km", "hr_drift": "+4.1%", "status": "Optimal Recovery", "color": "#2ecc71"}
    ]

    start_lat, start_lon = waypoints[0]["coords"]
    m = folium.Map(location=[start_lat + 0.08, start_lon + 0.12], zoom_start=11, tiles="OpenStreetMap")

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
    generate_map_preview_image()
    generate_interactive_map()
