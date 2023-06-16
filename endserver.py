#!/usr/bin/env python3
import os
import signal


def compile_dme_to_dmb():
    # Compile .dmb in linux using WW13.dme
    dme_file_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "WW13.dme"))
    os.system(f'DreamMaker {dme_file_path}') 


def kill_server():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            name = open(os.path.join('/proc', pid, 'cmdline'), 'r').read()
            if "WW13.dmb" in name and "sudo" not in name:
                os.kill(int(pid), signal.SIGKILL)
        except IOError:
            continue


if __name__ == "__main__":
    kill_server()
    compile_dme_to_dmb()
