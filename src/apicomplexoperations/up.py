import sys
import uvicorn
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-index", "--find-links=dep/", "complexoperations-iperoyg"])

from main import app

apiapp = app
port = int(sys.argv[1])    

if __name__ == "__main__":
    uvicorn.run("up:apiapp", host="127.0.0.1", port=port, log_level="trace")