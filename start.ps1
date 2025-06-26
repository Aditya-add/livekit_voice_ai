# Start first process
Start-Process powershell -ArgumentList "python src/agent.py dev"
Start-Sleep -Seconds 5  # Wait 5 seconds (adjust as needed)

# Start second process
Start-Process powershell -ArgumentList "python src/token_server.py"
Start-Sleep -Seconds 5  # Wait 5 seconds (adjust as needed)

# Start third process
Start-Process powershell -ArgumentList "cd agent-starter-react; npm run dev"
