#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 3:
    print("Usage: python3 install.py --shell <shell>")
    sys.exit()

shell = sys.argv[2]
username = os.getlogin()
home = f"/home/{username}"
dir_path = os.path.dirname(os.path.realpath(__file__))


if shell.lower() == "zsh":
    config = f"{home}/.zshrc"

elif shell.lower() == "bash":
    config = f"{home}/.bashrc"

elif shell.lower() == "fish":
    config = f"{home}/.config/fish/config.fish"

else:
    print("Your shell is not supported. Supported shells: bash, zsh, fish")
    sys.exit()
def add_alias():
    print(f"Your config file is {config}.")
    print("This program is gonna add an alias to your shell's config file.")
    print("Please backup your file before get proceed")
    confirm = input("Are you sure? (y/n) ")
    if confirm.lower() == "n":
        print("Aborting...")
        sys.exit()
    elif confirm.lower() == "y":
        exist = os.system(f"cat {config} &> /dev/null")
        if exist != 0:
            print(f"{config} file doesn't exist. Please enter your config file manually.")
            manual_config = input("Enter Config file's full location: ")
            with open(f"{manual_config}", "a") as manual_add:
                print(f"Adding alias to {manual_config}")
                manual_add.write(f"alias 'warper'='sudo python3 {dir_path}/warper.py'")
                manual_add.close()
        elif exist == 0:
            print(f"Adding alias to {config}.")
            with open(f"{config}","a") as alias_add:
                alias_add.write(f"alias 'warper'='sudo python3 {dir_path}/warper.py'")
                alias_add.close()


if __name__ == '__main__':
    add_alias()
