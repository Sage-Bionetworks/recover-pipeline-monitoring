Monitoring jobs and processes for RECOVER pipelines

## Ingress pipeline (recover-s3-synindex)

```sh
0 9 * * * \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "recover-s3-synindex cron job started"}' "webhook" \
&& docker run -e AWS_SYNAPSE_TOKEN=<token> -e SYNAPSE_AUTH_TOKEN=<token> ghcr.io/sage-bionetworks/recover-s3-synindex:main \
>> /home/ec2-user/output.log \
2>> /home/ec2-user/error.log \
&& python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "recover-s3-synindex cron job succeeded"}' "webhook" \
|| python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "recover-s3-synindex cron job failed"}' "webhook"
```
