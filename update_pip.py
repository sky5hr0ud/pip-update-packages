#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Thanks to ActiveState for most of this code.
# https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/

import sys
import subprocess


def main():
    try:
        packages = package_check()
        if packages is False:
            print('No outdated packages!')
        else:
            package_update(packages)
    except Exception as e:
        print(e)


def package_check():
    packages = subprocess.check_output(
        [sys.executable, '-m', 'pip', 'list', '-o', '--format=freeze'])
    if len(packages) > 0:
        print('Outdated packages:')
        subprocess.check_call([sys.executable, '-m', 'pip', 'list', '-o'])
        return packages
    else:
        return False


def package_update(packages):
    update_packages = []
    for package in packages.split():
        update_packages.append(package.decode().split('==')[0])
    for update in update_packages:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', update, '--upgrade'])
    print('Updated', len(packages), 'packages!')


if __name__ == '__main__':
    main()
