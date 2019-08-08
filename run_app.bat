rem "set FLASK_APP=app.py if not using .py directly"
set FLASK_DEBUG=True

rem "start flask server"
start "Flextime" python app.py

rem "go to C drive"
C:

rem "locate and run chrome"
start "chrome" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --new-window "http://localhost:5000"