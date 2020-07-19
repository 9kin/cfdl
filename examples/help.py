import subprocess
import sys
import time

command  = sys.argv[1]


PROMPT = "❯"

def slowprint(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def show(command, execute=True):
    print(PROMPT, end=" ")
    slowprint(command)
    if execute:
        subprocess.call('python3 -m ' + command, shell=True)


if command == "download":
    show('cfdl download 1380A # download task')
    show('cfdl download 1380A --pdf # download task with pdf')
    show('cfdl download 1371 # download one contest with submition in tutorial')

    show("cfdl download 1380A --debug # don't show progress bar.", execute=False)

    show('cfdl download 1380-1382 --debug # download contest-range', execute=False)
    show('cfdl download 1380A 1380-1382 1385 --debug # download contest + contest-range + task',  execute=False)
    show('cfdl download 1380A --debug --clean # download task + clean database', execute=False)
    show("cfdl download 1380A -t --debug # download with tutorial.", execute=False)
# termtosvg examples/help.svg --command='python3 examples/generate.py' --screen-geometry=80x20 -t examples/window.svg
