Monitoring jobs and processes for RECOVER pipelines

## Run pipeline

```sh
0 9 * * * docker pull ghcr.io/sage-bionetworks/<pipeline>:main && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job started"}' "<webhook>" && \
docker run -e AWS_SYNAPSE_TOKEN=<token> -e SYNAPSE_AUTH_TOKEN=<token> ghcr.io/sage-bionetworks/<pipeline>:main > /home/ec2-user/output.log 2> /home/ec2-user/error.log && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job succeeded"}' "<webhook>" || \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job failed"}' "<webhook>"
```

## Store logs in Synapse

```sh
0 12 * * * python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job started"}' "<webhook>" && \
synapse login && \
synapse store ~/output.log --parentid <pipeline_logs_dir_synid> --name stdout_log && \
synapse store ~/error.log --parentid <pipeline_logs_dir_synid> --name stderr_log && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job succeeded"}' "<webhook>" || \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job failed"}' "<webhook>"
```
