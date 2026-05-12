import boto3
import botocore.config
import json
from datetime import datetime
def blog_generate_using_bedrock(blogtopic:str)->str:
    prompt=f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]"""
    body={
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }
    try:
        bedrock=boto3.client(service_name="bedrock-runtime",region_name="us-east-1",config=botocore.config.Config(retries={'max_attempts': 5, 'mode': 'standard'}))
        response=bedrock.invoke_model(
            body=json.dumps(body),
            modelId="meta.llama3-70b-instruct-v1:0",
        )
        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        print(response_data)
        blog_details=response_data['generation']
        return blog_details
    except Exception as e:
        print(f"Error generating blog: {e}")
        return "Sorry, I couldn't generate the blog at this moment."
def save_blog_to_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket,Key=s3_key,Body=generate_blog)
        print(f"Blog saved to S3 bucket {s3_bucket} with key {s3_key}")
    except Exception as e:
        print(f"Error saving blog to S3: {e}")

def lambda_handler(event, context):
    event=json.loads(event['body'])
    blogtopic=event['blogtopic']
    generate_blog=blog_generate_using_bedrock(blogtopic)
    if generate_blog:
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        s3_key=f"blog_output_{current_time}.txt"
        s3_bucket="aws_bedrock_course1"
        save_blog_to_s3(s3_key, s3_bucket,generate_blog)
    else:
        print("no blog was generated")
    return{
        'statusCode': 200,
        'body': json.dumps('Blog generation and storage process completed.')
    }