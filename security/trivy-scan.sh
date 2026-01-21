#!/bin/bash
# Scan the best image using Trivy

IMAGE_NAME="docker-prod-image-prod:v1.0.0"

#echo "Building best image..."
#docker build -f docker/Dockerfile.best -t $IMAGE_NAME .

echo "Scanning $IMAGE_NAME..."
trivy image $IMAGE_NAME
echo "Scan completed."