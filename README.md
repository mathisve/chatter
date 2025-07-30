# Fake Chatter: Immersive Fake Terminal Output Generator

## Overview

Fake Chatter is a Python script designed to generate immersive fake terminal output, simulating a remote outpost's computer system. This tool is perfect for creating atmospheric visuals for storytelling, games, or immersive experiences. The output includes fictional timestamps, system logs, graphs, solar system maps, encryption events, crew chat messages, and more, all rendered in a stylized terminal format.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fake-chatter.git
   cd fake-chatter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main Python script to generate the fake terminal output:
```
python main.py
```

The script will display a sequence of simulated terminal logs and events, creating the illusion of an active remote outpost system.

## Key Features

- **Fictional Timestamps:** Logs and events are timestamped with realistic, but fictional, dates and times.
- **Graphs and Visualizations:** Displays ASCII graphs representing system metrics.
- **Solar System Maps:** Shows stylized maps of the solar system with relevant data.
- **Encryption Events:** Simulated encryption and decryption logs to enhance immersion.
- **Crew Chat Messages:** Includes fictional chat conversations between crew members.
- **Dynamic Event Generation:** Events are generated dynamically to keep the output varied and engaging.

## Customization

- **Adding More Events:** Extend the event list in the script to include additional fake logs or messages.
- **Changing Colors:** Modify the color scheme by editing the terminal color codes in the script.
- **Adjusting Timing:** Customize the delay and pacing of the output to suit your presentation style.

## Example Output

```
[2024-06-15 14:23:07] SYSTEM INIT: Remote Outpost Alpha
[2024-06-15 14:23:10] SENSOR DATA: Temperature nominal at -45°C
[2024-06-15 14:23:15] ENCRYPTION: Data packet #452 encrypted successfully
[2024-06-15 14:23:20] CREW CHAT: "All systems green. Preparing for EVA."
[2024-06-15 14:23:25] SOLAR SYSTEM MAP:
   [*] Earth
       |
   [*] Mars
       |
   [*] Outpost Alpha
[2024-06-15 14:23:30] GRAPH: Power levels stable
```

Feel free to contribute or customize Fake Chatter to fit your creative needs!

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