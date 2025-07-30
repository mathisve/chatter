# Fake Chatter

Immersive fake terminal output generator with separate frontend and backend components, Docker containers, and Kubernetes deployment.

## Live Demo

Explore the running system at:  
[https://outpost.homek8s.com](https://outpost.homek8s.com)

## Architecture

- **Backend**  
  A Python Flask application that generates Server-Sent Events (SSE) or WebSocket streams of sci-fi terminal logs.
- **Frontend**  
  A static HTML/JavaScript client served via Nginx that connects to the backend stream and displays slow-printed, colorized terminal output.
- **Deployment**  
  Both components are packaged as Docker images (`mathisve/fake-chatter-backend` and `mathisve/fake-chatter-frontend`) and can be deployed on Kubernetes with provided manifests.

## Prerequisites

- Docker & Docker Hub account
- Kubernetes cluster with NGINX Ingress 
- `kubectl` configured to target your cluster

## Build

1. Modify the build.sh script with your username
2. Modify `client/index.html` EVENTSOURCE_URL
3. Build and push Docker images:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

## Kubernetes Deployment

1. Apply the backend resources:

   ```bash
   kubectl apply -f manifests/backend.yaml
   ```

2. Apply the frontend resources:

   ```bash
   kubectl apply -f manifests/frontend.yaml
   ```

3. Verify the namespace and pods:

   ```bash
   kubectl -n fake-chatter get all
   ```

## Customization

- **Add events**: Edit `main.py` to extend `fake_terminal_line()` with new message types.
- **Adjust colors**: Modify ANSI color mappings in both `main.py` and `client.js`.
- **Tuning**: Change pacing, probabilities, and resource limits to suit your environment.

## License

MIT License. Feel free to fork and adapt for your own storytelling, demos, or ambient installations!