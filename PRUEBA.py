#!/usr/bin/env python
def main(args):
    with open('vars.yml', 'r') as fichero:
        doc=yaml.load(fichero)

    type(doc)
dict

if __name__ == '__main__':
    import os
    import yaml
    import subprocess
    import sys
    sys.exit(main(sys.argv))
