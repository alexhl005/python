#!/usr/bin/env python3
import shutil
import sys
import os
import subprocess

def ejecutar_script():
    script = "hello.sh"
    try: 
      comando = subprocess.run(["bash", script], capture_output=True, text=True, check=True)
      print(comando.stdout)
    except subprocess.CalledProcess as e:
      print("\nError al ejecutar el script", e.stderr)
    return 0

def main(args):
    escript=ejecutar_script()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
