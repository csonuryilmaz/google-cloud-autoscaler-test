# requirements:
# $ pip install google-cloud-monitoring
# setup service account .json: https://cloud.google.com/monitoring/docs/reference/libraries#setting_up_authentication

from google.api import label_pb2 as ga_label
from google.api import metric_pb2 as ga_metric
from google.cloud import monitoring_v3

client = monitoring_v3.MetricServiceClient()

descriptor_name = f"projects/autoscaletest-342212/metricDescriptors/custom.googleapis.com/agent_workload"
client.delete_metric_descriptor(name=descriptor_name)

print("Deleted metric descriptor {}.".format(descriptor_name))
