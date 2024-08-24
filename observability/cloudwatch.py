# observability/cloudwatch_setup.py
import boto3

cloudwatch = boto3.client('cloudwatch')
logs = boto3.client('logs')

def create_log_group():
    logs.create_log_group(logGroupName='/aws/generative-ai')

def put_metric_data(namespace, metric_name, value):
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Value': value
            },
        ]
    )

def setup_xray():
    from aws_xray_sdk.core import xray_recorder
    from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
    from flask import Flask

    app = Flask(__name__)
    xray_recorder.configure(service='MyService')
    XRayMiddleware(app, xray_recorder)

    return app
