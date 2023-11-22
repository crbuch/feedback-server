#!/bin/bash

# Start the Python server in the background
gnome-terminal --title="Python Server" -- bash -c "python server.py"

# Start ngrok in a new terminal window
gnome-terminal --title="Ngrok Server" -- bash -c "ngrok http http://localhost:5000"
