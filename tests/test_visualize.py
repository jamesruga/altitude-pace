import os
import pytest
from src.visualize import generate_telemetry_chart, generate_map_preview_image, generate_interactive_map

def test_visualize_artifacts_generation():
    os.makedirs("docs", exist_ok=True)
    generate_telemetry_chart()
    generate_map_preview_image()
    generate_interactive_map()

    assert os.path.exists("docs/telemetry_chart.png")
    assert os.path.exists("docs/map_preview.png")
    assert os.path.exists("docs/index.html")
