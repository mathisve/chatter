#!/usr/bin/env bash
set -euo pipefail

# Docker Hub username
USERNAME="mathisve"

# Backend image settings
BACKEND_IMAGE="${USERNAME}/fake-chatter-backend:latest"
BACKEND_DOCKERFILE="Dockerfile"
BACKEND_CONTEXT="."

# Frontend image settings
FRONTEND_IMAGE="${USERNAME}/fake-chatter-frontend:latest"
FRONTEND_DOCKERFILE="client/Dockerfile"
FRONTEND_CONTEXT="client"

# Ensure Docker is logged in
echo "Logging into Docker Hub as ${USERNAME}..."
docker login

# Build backend image for linux/amd64
echo "Building backend image ${BACKEND_IMAGE} for linux/amd64..."
docker build --platform linux/amd64 \
    --file "${BACKEND_DOCKERFILE}" \
    --tag "${BACKEND_IMAGE}" \
    "${BACKEND_CONTEXT}"

# Push backend image
echo "Pushing backend image ${BACKEND_IMAGE}..."
docker push "${BACKEND_IMAGE}"

# Build frontend image for linux/amd64
echo "Building frontend image ${FRONTEND_IMAGE} for linux/amd64..."
docker build --platform linux/amd64 \
    --file "${FRONTEND_DOCKERFILE}" \
    --tag "${FRONTEND_IMAGE}" \
    "${FRONTEND_CONTEXT}"

# Push frontend image
echo "Pushing frontend image ${FRONTEND_IMAGE}..."
docker push "${FRONTEND_IMAGE}"

echo "All images built and pushed successfully."