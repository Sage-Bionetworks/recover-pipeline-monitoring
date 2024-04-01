# Monitoring jobs and processes for RECOVER pipelines

To send notifications to a Slack channel, you will need a Slack app that allows incoming wehbooks. Read [this](https://practicaldatascience.co.uk/data-science/how-to-send-a-slack-message-in-python-using-webhooks) for more info.

## Quick Start

Reaplce `your_private_webhook_url` with your actual webhook url

```sh
python3 /path/to/send_slack_message.py '{"text": "message to send to Slack"}' "your_private_webhook_url"
```

You can chain this command together with other shell commands and a cron schedule to have context-specific Slack messages be sent automatically

```sh
0 0 * * * first command && \
python3 /path/to/send_slack_message.py '{"text": "pipeline started running"}' "your_private_webhook_url" && \
second command && \
python3 /path/to/send_slack_message.py '{"text": "second command exited with 0 errors"}' "your_private_webhook_url" || \
python3 /path/to/send_slack_message.py '{"text": "second command exited with an error"}' "your_private_webhook_url"
```

## Examples

### Run Docker-ized Pipeline

```sh
0 9 * * * docker pull ghcr.io/sage-bionetworks/<pipeline>:main && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job started"}' "<webhook>" && \
docker run -e AWS_SYNAPSE_TOKEN=<token> -e SYNAPSE_AUTH_TOKEN=<token> ghcr.io/sage-bionetworks/<pipeline>:main > /home/ec2-user/output.log 2> /home/ec2-user/error.log && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job succeeded"}' "<webhook>" || \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "<pipeline>: cron job failed"}' "<webhook>"
```

**Note:** You can customize your `docker run ...` command with optional flags like `--rm`, `--i`, `--d`, etc. for your specific use case.

### Store Logs in Synapse

```sh
0 12 * * * python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job started"}' "<webhook>" && \
synapse login && \
synapse store ~/output.log --parentid <pipeline_logs_dir_synid> --name stdout_log && \
synapse store ~/error.log --parentid <pipeline_logs_dir_synid> --name stderr_log && \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job succeeded"}' "<webhook>" || \
python3 /home/ec2-user/recover-pipeline-monitoring/send_slack_message.py '{"text": "Storing logs for <pipeline>: cron job failed"}' "<webhook>"
```
