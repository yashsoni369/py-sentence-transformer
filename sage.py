import json
import boto3
import os


class SageClient:
    def __init__(self):
        print(os.environ.get('ENDPOINT_NAME'))
        self.__endpoint_name = os.environ.get('ENDPOINT_NAME')
        self.__boto_client = boto3.client('runtime.sagemaker',
                                          region_name=os.environ.get('AWS_REGION', 'us-east-1'),
                                          aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                                          aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
                                          )

    def get_embeddings(self, sentence):
        # Prepare the payload
        payload = {"inputs": sentence}

        # Send a request
        response = self.__invoke_endpoint(payload)
        return response['vectors']

    def __invoke_endpoint(self, payload):
        try:
            response = self.__boto_client.invoke_endpoint(EndpointName=self.__endpoint_name,
                                                          ContentType="application/json",
                                                          Body=json.dumps(payload))
            embeddings = json.loads((response["Body"].read()))
            return embeddings
        except Exception as e:
            print(f"Failed to invoke endpoint: {e}")
            raise
