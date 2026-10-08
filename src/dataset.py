import os
import numpy as np
import pandas as pd

def generate_telemetry_csv(num_points=500, output_path="data/runner_telemetry.csv"):
    np.random.seed(42)
    time_steps = pd.date_range(start="2026-09-01 06:00:00", periods=num_points, freq="10s")
    
    # Simulate high-altitude run (Eldoret terrain profile)
    distance = np.cumsum(np.random.uniform(20, 35, num_points))
    elevation = 2100 + np.sin(np.linspace(0, 10, num_points)) * 150 + np.random.normal(0, 2, num_points)
    heart_rate = 130 + np.cumsum(np.random.normal(0, 0.2, num_points)).clip(-15, 35) + (elevation / 50)
    speed_ms = np.random.normal(3.5, 0.4, num_points).clip(2.0, 5.5)
    
    df = pd.DataFrame({
        "timestamp": time_steps,
        "distance_m": distance,
        "elevation_m": elevation,
        "heart_rate_bpm": heart_rate,
        "speed_ms": speed_ms
    })
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[Dataset] Generated {num_points} telemetry records at {output_path}")

if __name__ == "__main__":
    generate_telemetry_csv()
