# requirements:
# $ pip install google-cloud-monitoring
# setup service account .json: https://cloud.google.com/monitoring/docs/reference/libraries#setting_up_authentication

from google.cloud import monitoring_v3

import time
import sys

print('Google Cloud Monitoring - Custom Metrics')

if len(sys.argv)-1 != 2:
    print("Usage: python ping_workload.py {WORKLOAD} {INSTANCE_ID}")
    sys.exit(1)

workload = float(sys.argv[1])
instance = sys.argv[2]

client = monitoring_v3.MetricServiceClient()
project_id = 'autoscaletest-342212'
project_name = f"projects/{project_id}"

series = monitoring_v3.TimeSeries()
series.metric.type = "custom.googleapis.com/agent_workload_per_instance"
# series.resource.type = "global"
series.resource.type = "gce_instance"
series.resource.labels["instance_id"] = instance
series.resource.labels["zone"] = "us-central1-a"

now = time.time()
seconds = int(now)
nanos = int((now - seconds) * 10 ** 9)
interval = monitoring_v3.TimeInterval(
    {"end_time": {"seconds": seconds, "nanos": nanos}}
)
point = monitoring_v3.Point({"interval": interval, "value": {"double_value": workload}})

series.points = [point]
client.create_time_series(request={"name": project_name, "time_series": [series]})

print(f"Successfully ping {series.metric.type} for instance {instance}.")
