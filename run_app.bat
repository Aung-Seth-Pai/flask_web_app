rem "start virtual env and flextime server"
rem "/k = keep screen on"
start cmd.exe /k "color b && D:\Workspace\flextime\flextime\scripts\activate.bat && D: && cd/Workspace/flextime && python flextime.py"

rem "go to C drive"
C:

rem "locate and run chrome"
start "chrome" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --new-window "http://localhost:5000"