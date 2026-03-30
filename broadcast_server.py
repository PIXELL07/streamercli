import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("cmd")

args = parser.parse_args()

if args.cmd == "start":
    subprocess.run(["uvicorn", "app.main:app", "--reload"])

elif args.cmd == "connect":
    subprocess.run(["python", "client/cli.py"])