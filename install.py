#!/usr/bin/env python3

import traceback
import shutil
import sys
import os

C:\Program Files\Blender Foundation\Blender\2.69\scripts\addons

installFolderName = "io_export_cryblend"
dirLocalInstallation = "io_export_cryblend/"
dirBlenderAddon = "C:/Program Files/Blender Foundation/Blender/{}/scripts/addons/" + installFolderName

def main():    
    print("---------------")

    VERSION = sys.version[:5].split(".")

    if VERSION[0] != "3":
        print("You need Python 3 to run this program!")

    print("Please your blender version (ex. 2.69)")
    global dirBlenderAddon
    dirBlenderAddon = dirBlenderAddon.format(input(" :: "))

    while True:
        if os.path.exists(dirBlenderAddon):
            install()
            print("---------------")
            input("Press any key to exit...")
            break
        else:
            print("Python cannot recognize a valid Blender installation on your computer.")
            print("Please enter your blender installation directory all the way to the \n" + \
                  "version folder and stop there.")
            direct = input(" :: ")
            global dirBlenderAddon
            dirBlenderAddon = os.path.join(direct, "scripts/addons/")
        

def install():
    print("Installing...")
    try:
        shutil.copytree(dirLocalInstallation, dirBlenderAddon)
        print("Installation complete!")
    except:
        print("Already installed.  Do you wish to replace the current installation with this one? ")
        choice = input(" :: ")
        if choice in ["yes", "y"]:
            uninstall()
            install()
        else:
            print("Cancelling installation...")

def uninstall():
    print("---------------")
    print("Uninstalling current version...")
    shutil.rmtree(dirBlenderAddon)
    print("Uninstallation complete!")
    print("---------------")

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Installation failed!")
        traceback.format_exc(error)
        input()
