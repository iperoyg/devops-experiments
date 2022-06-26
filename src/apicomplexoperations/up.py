import sys
import uvicorn
import subprocess

pkg = "complexoperations-iperoyg"
noindex = "--no-index"
folder = "--find-links=dep/"
params = [sys.executable, "-m", "pip", "install", noindex, folder, pkg]
subprocess.check_call(params)

from main import app

apiapp = app
port = int(sys.argv[1])

if __name__ == "__main__":
    uvicorn.run("up:apiapp", host="127.0.0.1", port=port, log_level="trace")
