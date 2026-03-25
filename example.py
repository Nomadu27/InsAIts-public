"""InsAIts — Minimal Working Example"""
# pip install insa-its
from insa_its import insAItsMonitor

# Create a monitor instance (100% local, no cloud)
monitor = insAItsMonitor()

# Inspect any AI response for security anomalies
result = monitor.inspect(
    "Here is the API key: sk-abc123secret",  # AI response
    "Show me the config"                      # Original prompt
)

if not result.clean:
    for anomaly in result.anomalies:
        print(f"[{anomaly.severity.name}] {anomaly.description}")
else:
    print("Response is clean.")
