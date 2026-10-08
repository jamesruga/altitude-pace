# 🏃‍♂️ AltitudePace — Biomechanical Marathon Telemetry Engine (`altitude-pace`)

[![Build Status](https://github.com/jamesruga/altitude-pace/actions/workflows/telemetry.yml/badge.svg)](https://github.com/jamesruga/altitude-pace/actions)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Folium](https://img.shields.io/badge/Maps-Folium%2FLeaflet-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
[![GitHub Pages](https://img.shields.io/badge/Live-Map%20View-success.svg)](https://jamesruga.github.io/altitude-pace/)

An automated biomechanical signal processing and sports analytics engine inspired by Kenya's high-altitude endurance running legacy (Eldoret/Iten). **AltitudePace** ingests GPS, elevation, and physiological telemetry to compute Grade-Adjusted Pace (GAP), model heart-rate drift decay, predict muscle collapse risk, and render interactive Leaflet race strategy maps.

---

## 📖 Operational Context & Problem Solved

High-altitude training creates unique physiological pacing dynamics. When long-distance runners transition from high-altitude camps (~2,100m elevation) to sea-level marathons, unmonitored heart-rate drift and grade changes often lead to late-stage muscle collapse. **AltitudePace** provides low-latency telemetry feature engineering to optimize pacing splits and flag fatigue hotspots in real time.

---

## 📊 Telemetry & Fatigue Profile Visualization

Below is the dynamic biomechanical telemetry distribution profile across race segments:

<p align="center">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 220" width="100%" style="background-color:#0f172a; border-radius:8px; padding:10px;">
    <text x="20" y="30" fill="#f8fafc" font-family="sans-serif" font-size="16" font-weight="bold">AltitudePace Telemetry &amp; Fatigue Profile</text>
    <rect x="50" y="60" width="180" height="110" rx="6" fill="#1e293b" stroke="#334155"/>
    <rect x="50" y="110" width="180" height="60" fill="#16a34a" rx="4"/>
    <text x="140" y="100" fill="#38bdf8" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">62%</text>
    <text x="140" y="145" fill="#ffffff" font-family="sans-serif" font-size="12" text-anchor="middle">Optimal Pacing</text>
    
    <rect x="260" y="60" width="180" height="110" rx="6" fill="#1e293b" stroke="#334155"/>
    <rect x="260" y="130" width="180" height="40" fill="#ea580c" rx="4"/>
    <text x="350" y="100" fill="#38bdf8" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">26%</text>
    <text x="350" y="155" fill="#ffffff" font-family="sans-serif" font-size="12" text-anchor="middle">Moderate Fatigue</text>
    
    <rect x="470" y="60" width="180" height="110" rx="6" fill="#1e293b" stroke="#334155"/>
    <rect x="470" y="145" width="180" height="25" fill="#dc2626" rx="4"/>
    <text x="560" y="100" fill="#38bdf8" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">12%</text>
    <text x="560" y="162" fill="#ffffff" font-family="sans-serif" font-size="12" text-anchor="middle">High Fatigue Risk</text>
    
    <text x="350" y="200" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Real-time physiological telemetry breakdown calculated via AltitudePace Engine</text>
  </svg>
</p>

---

## 🏗 Architecture & Stack

- **Telemetry Processing**: Python 3.10+, Pandas, NumPy, `gpxpy`
- **Biomechanical Logic**: Grade-Adjusted Pace (GAP), Heart-Rate Drift Decay, Multi-Tier Fatigue Risk Classifier
- **Geospatial Mapping**: Folium / Leaflet.js
- **Quality Assurance**: `pytest` unit test suite
- **CI/CD Automation**: GitHub Actions scheduled cloud execution with GitHub Pages map deployment

---

## 🛠 Local Quickstart & Testing

\```bash
# Clone repository & install dependencies
git clone [https://github.com/jamesruga/altitude-pace.git](https://github.com/jamesruga/altitude-pace.git)
cd altitude-pace
pip install -r requirements.txt

# Run pytest unit tests
PYTHONPATH=. pytest -v

# Generate telemetry and render map
python src/dataset.py
PYTHONPATH=. python src/visualize.py
\```

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.
