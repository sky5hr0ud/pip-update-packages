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
    outdated_packages = subprocess.check_output(
        [sys.executable, '-m', 'pip', 'list', '-o', '--format=freeze'])
    if len(outdated_packages) > 0:
        print('Outdated packages:')
        subprocess.check_call([sys.executable, '-m', 'pip', 'list', '-o'])
        return outdated_packages
    else:
        return False


def package_update(packages):
    update_packages = []
    updated_packages = 0
    for package in packages.split():
        update_packages.append(package.decode().split('==')[0])
    for update in update_packages:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', update, '--upgrade'])
            updated_packages += 1
        except subprocess.CalledProcessError as e:
            print(e)
    print('Updated', updated_packages, 'packages!')


if __name__ == '__main__':
    main()
