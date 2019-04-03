# Autoreload script when a python file is updated
# Original: https://github.com/stevekrenzel/autoreload

import os
import sys
import subprocess
import signal
import time


PATH = '.'
COMMAND = ' '.join(sys.argv[1:])
WAIT = 1


def file_filter(name):
    ''' Determine is a filename should be watched or not '''
    return name.endswith('.py')


def _interesting_files(path):
    ''' Lists all the interesting files in a directory tree '''
    for root, _, files in os.walk(path):
        for file in filter(file_filter, files):
            yield os.path.join(root, file)


def file_times(files):
    ''' Iterates over the edit time of a set of files '''
    for file in files:
        yield os.stat(file).st_mtime


def print_stdout(process):
    ''' Pipes the standard output of a process to the console '''
    stdout = process.stdout
    if stdout != None:
        print(stdout)


def print_text(text):
    print(os.path.splitext(PATH)[0])


def main():

    print_text("hi")
    try:

        print('Autorestart enabled')

        interesting_files = list(_interesting_files(PATH))
        process = subprocess.Popen(COMMAND, shell=True, preexec_fn=os.setsid)
        last_mtime = max(file_times(interesting_files), default=0)
        is_running = True

        while True:
                max_mtime = max(file_times(interesting_files), default=0)
                print_stdout(process)
                if is_running and process.poll() is not None:
                    is_running = False
                    print('Autoreload: Process Terminated')
                if max_mtime > last_mtime:
                    last_mtime = max_mtime
                    print('Autoreload: Restarting Process')
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                    time.sleep(1)
                    process = subprocess.Popen(
                        COMMAND, shell=True, preexec_fn=os.setsid)
                    is_running = True
                time.sleep(WAIT)

    except Exception as e:
        print('Hit exception {e}; Shutting Down Autoreload'.format(e=e.with_traceback))
        time.sleep(1)

    finally:
        if process and process.poll() is not None:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)


main()
