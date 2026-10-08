import pytest
import pandas as pd
from src.engine import AltitudePaceEngine

@pytest.fixture
def engine():
    return AltitudePaceEngine()

@pytest.fixture
def sample_telemetry():
    return pd.DataFrame({
        'timestamp': ['2026-09-01 06:00:00', '2026-09-01 06:00:10'],
        'distance_m': [0.0, 30.0],
        'elevation_m': [2100.0, 2110.0],
        'heart_rate_bpm': [135.0, 172.0],
        'speed_ms': [3.2, 2.8]
    })

def test_grade_and_speed_calculation(engine, sample_telemetry):
    processed = engine.compute_features(sample_telemetry)
    assert 'grade' in processed.columns
    assert 'adjusted_speed_ms' in processed.columns
    assert processed.loc[1, 'grade'] > 0

def test_fatigue_classification(engine, sample_telemetry):
    statuses = engine.classify_fatigue(sample_telemetry)
    assert len(statuses) == 2
    assert statuses[1] in ['Moderate Fatigue', 'High Fatigue (Risk of Collapse)', 'Optimal Pacing']
