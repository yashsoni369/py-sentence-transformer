# Use an official PyTorch runtime as a parent image
FROM pytorch/pytorch:latest

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Use CUDA runtime if available (uncomment this line if you are not using GPU)
# ENV NVIDIA_VISIBLE_DEVICES all

# Run app.py when the container launches
CMD ["python", "app.py"]
