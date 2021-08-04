#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: sudo python3 warp.py <on/off>")
    sys.exit()

username = os.getlogin()
home = f"/home/{username}"
dir_path = os.path.dirname(os.path.realpath(__file__))
option = sys.argv[1]

def copy_current():
    os.system(f"mkdir -p {home}/.config/warper/resolv_copy")
    os.system(f"cp -i /etc/resolv.conf {home}/.config/warper/resolv_copy/resolv.conf")

def open_warp():
    resolv = '/etc/resolv.conf'
    with open(resolv, "w") as resolvconf:
        resolvconf.write("nameserver 1.0.0.1\nnameserver 1.1.1.1\n")
        resolvconf.close()

def close_warp():
    os.system("rm /etc/resolv.conf")
    os.system(f"cp {home}/.config/warper/resolv_copy/resolv.conf /etc/resolv.conf")


if option.lower() == "on":
    copy_current()
    open_warp()

elif option.lower() == "off":
    close_warp()
    os.system(f"rm {home}/.config/warper/resolv_copy/resolv.conf")
else:
    print("Usage: sudo python3 warp.py <on/off>")
