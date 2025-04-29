import os
import eel
import subprocess

eel.init("www")

# I error run this : python -m http.server 8000

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.Popen([edge_path, '--app=http://localhost:8000/index.html'])
eel.start("index.html", mode = None, host='localhost', block=True)
