import sys
import uvicorn
import subprocess

pkg = "complexoperations-iperoyg"
noindex = "--no-index"
folder = "--find-links=dep/"
params = [sys.executable, "-m", "pip", "install", noindex, folder, pkg]
subprocess.check_call(params)
config_port = int(sys.argv[1])

if __name__ == "__main__":
    print('port', config_port)
    local = "0.0.0.0"
    log = "trace"
    uvicorn.run("main:app", host=local, port=config_port, log_level=log)
