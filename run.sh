#!/bin/bash
python3 server.py &
ngrok http http://localhost:5000
