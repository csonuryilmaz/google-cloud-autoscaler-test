# google-cloud-autoscaler-test

Requirements:

- `pip install google-cloud-monitoring`
- Export credentials .json before running script
  - `export GOOGLE_APPLICATION_CREDENTIALS=autoscaletest-342212-0c209fda57a1.json`

See [here](https://cloud.google.com/monitoring/docs/reference/libraries#create-service-account-console) for Monitoring client libraries.

References:

- Autoscaler REST API [here](https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers).
  - It can be used to check `recommendedSize` to support manual scale in decision when using only scale out mode.
- [Managing autoscalers](https://cloud.google.com/compute/docs/autoscaler/managing-autoscalers#gcloud_2)
- [Scaling based on Cloud Monitoring metrics](https://cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#custom_metrics)
- [Autoscaling groups of instances - Fundamentals](https://cloud.google.com/compute/docs/autoscaler#autoscaling_policy)
- [Setting up health checking and autohealing](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs)
- [Work with managed instances](https://cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance)
- [Instance Groups](https://cloud.google.com/compute/docs/instance-groups/#autohealing)
- [Understanding autoscaler decisions](https://cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#preparing_for_instance_terminations)
- [Custom metrics](https://cloud.google.com/monitoring/custom-metrics#global-v-generic)
- [Sample app for testing autoscaling and autohealing](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/compute/managed-instances/demo)
- [Create custom metrics with the API](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#monitoring_create_metric-python)
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details)

Example, delete an instance from instance group:

```bash
gcloud compute instance-groups managed delete-instances autoscaling-group-metrics-1 --instances=autoscaling-group-metrics-1-trl1 --zone=us-central1-a
```
