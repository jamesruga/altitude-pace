# 🏃‍♂️ AltitudePace — Biomechanical Marathon Telemetry Engine (`altitude-pace`)

[![Build Status](https://github.com/jamesruga/altitude-pace/actions/workflows/telemetry.yml/badge.svg)](https://github.com/jamesruga/altitude-pace/actions)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Folium](https://img.shields.io/badge/Maps-Folium%2FLeaflet-green.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

An automated biomechanical signal processing engine inspired by Kenya's high-altitude running legacy (Eldoret/Iten). **AltitudePace** ingests GPS, elevation, and physiological telemetry to compute Grade-Adjusted Pace (GAP), model heart-rate drift decay, predict muscle collapse risk, and render interactive Leaflet race strategy maps.

---

## 📖 Operational Context & Problem Solved

High-altitude training creates unique physiological pacing dynamics. When long-distance runners transition from high-altitude camps (~2,100m elevation) to sea-level marathons, unmonitored heart-rate drift often leads to late-stage muscle collapse. **AltitudePace** provides telemetry feature engineering to optimize pacing splits and flag fatigue hotspots in real time.

---

## 🏗 Architecture & Stack

- **Telemetry Processing**: Python 3.10+, Pandas, NumPy, `gpxpy`
- **Biomechanical Logic**: Grade-Adjusted Pace (GAP), Heart-Rate Drift Decay, Multi-Tier Fatigue Risk Classifier
- **Geospatial Mapping**: Folium / Leaflet.js
- **Quality Assurance**: `pytest` unit test suite
- **CI/CD Automation**: GitHub Actions scheduled cloud execution with GitHub Pages map deployment

---

## 🛠 Local Quickstart & Testing

```bash
# Install dependencies
pip install -r requirements.txt
# Run pytest unit tests
PYTHONPATH=. pytest -v
# Generate telemetry and render map
python src/dataset.py
PYTHONPATH=. python src/visualize.py
```

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.
