import json
import boto3
prompt_data="""
act as a shakespeare and write apoem on machine learning"""
bedrock=boto3.client(service_name="bedrock-runtime",region_name="us-east-1")
payload={
    "prompt": "[INST]"+prompt_data+"[/INST]",
    "max_gen_len": 512,
    "temperature": 0.7,
    "top_p": 0.9
}
body=json.dumps(payload)
model_id="meta.llama3-70b-instruct-v1:0"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)
response_body=json.loads(response.get('body').read())
response_text=response_body['generation']
print(response_text)
