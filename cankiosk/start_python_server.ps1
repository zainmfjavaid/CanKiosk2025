# Find Python executable path
$pythonPath = (Get-Command python).Source

# Set the path to the Python server script
$pythonScriptPath = "/home/pi/website/server.py"

# Start the Python server in the background
Start-Process -FilePath $pythonPath -ArgumentList $pythonScriptPath -WorkingDirectory "/home/pi/website/" -NoNewWindow -PassThru

Write-Host "Python server started successfully."

# Ensure script runs on startup (manually edit if needed)
Set-Content -Path "/etc/xdg/lxsession/LXDE-pi/autostart" -Value "@lxterminal -e 'powershell /cankiosk/script.ps1'"

# Start the kiosk script
Start-Process "lxterminal" -ArgumentList "-e", "powershell /cankiosk/script.ps1"

 b 