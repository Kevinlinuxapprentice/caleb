#!/usr/bin/env python3
import os
import sys

def escolhendoComando(comando):
    if comando=="open firefox":
        os.system("sh firefox.sh")
    elif comando=="open tibia":
        os.system("sh tibia.sh")
    elif comando=="shutdown":
        os.system("sh shutdown.sh")

    elif comando=="teamspeak" or comando=="team speak":
        os.system("sh ts.sh")

    elif comando=="reboot now" or comando=="reboot":
        os.system("sh reboot.sh")

    elif comando=="show ip":
        os.system("sh ip.sh")

    else:
        print("nao entendi, espero que nao seja um comando...")

