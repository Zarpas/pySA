import subprocess
subprocess.call("sudo python3 setup.py install", shell=True)
subprocess.call("sudo cp pySA /usr/share/man/man1/pySA.1", shell=True)
subprocess.call("sudo gzip /usr/share/man/man1/pySA.1", shell=True)
