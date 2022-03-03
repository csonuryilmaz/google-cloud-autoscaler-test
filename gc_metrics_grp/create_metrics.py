# requirements:
# $ pip install google-cloud-monitoring
# setup service account .json: https://cloud.google.com/monitoring/docs/reference/libraries#setting_up_authentication

from google.api import label_pb2 as ga_label
from google.api import metric_pb2 as ga_metric
from google.cloud import monitoring_v3

print('Google Cloud Monitoring - Custom Metrics')

client = monitoring_v3.MetricServiceClient()
project_id = 'autoscaletest-342212'
project_name = f"projects/{project_id}"

descriptor = ga_metric.MetricDescriptor()
descriptor.name = 'Agent Workload'
descriptor.type = "custom.googleapis.com/agent_workload_per_group"
descriptor.metric_kind = ga_metric.MetricDescriptor.MetricKind.GAUGE
descriptor.value_type = ga_metric.MetricDescriptor.ValueType.DOUBLE
descriptor.description = "Cumulative workload for agents. (work in progress+queue=total workload)"

# The kind of metric data tells you how to interpret the values relative to each other.
# It can be either GAUGE , which represents the value of a metric at a particular point,,
# unlike DELTA , where value measures the change since it was last recorded.

descriptor = client.create_metric_descriptor(
    name=project_name, metric_descriptor=descriptor
)
print("Created {}.".format(descriptor.name))

# Created projects/autoscaletest-342212/metricDescriptors/custom.googleapis.com/agent_workload_per_group.
