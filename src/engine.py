import os
import numpy as np
import pandas as pd

class AltitudePaceEngine:
    def __init__(self):
        self.fatigue_threshold_hr = 165.0

    def compute_features(self, df):
        """Calculates Grade-Adjusted Pace (GAP) and fatigue risk indicators."""
        # Calculate grade (rise over run)
        distance_diff = df['distance_m'].diff().fillna(1.0)
        elevation_diff = df['elevation_m'].diff().fillna(0.0)
        grade = elevation_diff / distance_diff.clip(lower=0.1)
        
        # Grade-Adjusted Pace factor (rough biomechanical adjustment)
        gap_multiplier = 1.0 + (grade * 3.3)
        adjusted_speed = df['speed_ms'] * gap_multiplier.clip(lower=0.5)
        
        # Fatigue Risk Score
        hr_decay = df['heart_rate_bpm'] - df['heart_rate_bpm'].rolling(10, min_periods=1).mean()
        fatigue_score = (df['heart_rate_bpm'] > self.fatigue_threshold_hr).astype(int) * 2 + (hr_decay > 5).astype(int)
        
        df['grade'] = grade
        df['adjusted_speed_ms'] = adjusted_speed
        df['fatigue_score'] = fatigue_score
        return df

    def classify_fatigue(self, df):
        processed = self.compute_features(df)
        predictions = np.where(processed['fatigue_score'] >= 3, 'High Fatigue (Risk of Collapse)',
                      np.where(processed['fatigue_score'] >= 1, 'Moderate Fatigue', 'Optimal Pacing'))
        return predictions

if __name__ == "__main__":
    df = pd.read_csv("data/runner_telemetry.csv")
    engine = AltitudePaceEngine()
    statuses = engine.classify_fatigue(df)
    print(f"[Engine] Processed {len(df)} telemetry points. Fatigue breakdown:")
    print(pd.Series(statuses).value_counts())
