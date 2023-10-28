# py-sentence-transformer

### Sentence Embeddings Service

Using Local &amp; Sagemaker Provisioned sentence transformer in Python

This repository contains a service for generating sentence embeddings using a deployed model on Amazon SageMaker also on
local machine

## Setup

### Environment Variables

1. Copy the `.env.example` file to a new file named `.env` and update the values to match your configuration:

    ```bash
    cp .env.example .env
    ```

The following environment variables are required:

- `ENDPOINT_NAME`: The name of your SageMaker endpoint.
- `AWS_REGION`: The AWS region your SageMaker endpoint is deployed in.
- `AWS_ACCESS_KEY`: The AWS access key.
- `AWS_SECRET_KEY`: The AWS secret.

### Running Locally

1. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python app.py
    ```

### Running with Docker

1. Build the Docker image:

    ```bash
    docker build -t sentence-embeddings .
    ```

2. Run the Docker container with Docker Compose:

    ```bash
    docker-compose up
    ```
