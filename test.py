import boto3

client = boto3.client("bedrock", region_name="us-east-1")

print(client.list_foundation_models())