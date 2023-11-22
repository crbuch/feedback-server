@echo off

:: Start the Python server in the background
start "Python Server" cmd /k "python server.py"
start "Ngrok Server" cmd /k "ngrok http http://localhost:5000"
