#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Thanks to ActiveState for lots of this code.
# https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/

import sys
import subprocess


def main():
    try:
        print('Outdated packages:')
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'list', '-o'])
        packages = subprocess.check_output(
            [sys.executable, '-m', 'pip', 'list', '-o', '--format=freeze'])
        if len(packages) > 0:
            package_update(packages)
        else:
            print('No outdated packages!')
    except Exception as e:
        print(e)


def package_update(packages):
    update_packages = []
    for package in packages.split():
        update_packages.append(package.decode().split('==')[0])
    for update in update_packages:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', update, '--upgrade'])


if __name__ == '__main__':
    main()
