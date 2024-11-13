import requests
import re
import pandas as pd
metrics_url = 'localhost:3030'

res = requests.get(metrics_url)

if res.status_code == 200:
    metrics = res.text
else:
    metrics = ''
    print("failure")

def parse_metrics(metrics):
    metric = {}
    for line in metrics.splitlines():
        if line.startswith('#') or not line.strip():
            continue
        
        match = re.match(r'^([\w:]+)(\{.*?\})?\s+([0-9\.\-e]+)$', line)
        if match:
            metric_name = match.group(1)
            metric_value = float(match.group(3))
            
            if metric_name not in metric:
                metric[metric_name] = []

            metric[metric_name].append(metric_value)
    return metric

metrics_data = parse_metrics(metrics)

df = pd.DataFrame({k: pd.Series(v) for k,v in metrics_data.items()})
print(df.head())
