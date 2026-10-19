#!/usr/bin/env python3
# DRAGON V4.1 - KING EHAB EDITION 🐉🔥
# 12 Tools + Deluxe UI + Auto Update

import os, sys, time, requests, json, subprocess

LOCAL_VER = "4.1"
REPO_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"
FILE_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/ehab_dragon_v4_full.py"

# Colors
R="\033[1;31m"; G="\033[1;32m"; Y="\033[1;33m"; B="\033[1;34m"; C="\033[1;36m"; W="\033[1;37m"; P="\033[1;35m"; RESET="\033[0m"

def banner():
    os.system('clear')
    print(f"""{R}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
{C}             KING EHAB V{LOCAL_VER} - DELUXE EDITION 👑🔥{RESET}
{Y}═══════════════════════════════════════════════════════{RESET}
""")

def check_update():
    print(f"{C}[+] Checking Dragon Update...{RESET}")
    try:
        r = requests.get(REPO_RAW, timeout=5)
        if r.status_code != 200:
            print(f"{R}[-] version.json not found (404){RESET}")
            time.sleep(1)
            return
        data = r.json()
        remote = str(data.get("latest_version", LOCAL_VER))
        msg = data.get("update_msg", "")
        print(f"{Y}Local: {LOCAL_VER} | GitHub: {remote}{RESET}")
        if remote != LOCAL_VER and remote > LOCAL_VER:
            print(f"""{R}
🔔🔔🔔🔔🔔🔔🔔🔔🔔🔔🔔🔔
🔔 DRAGON UPDATE FOUND! 🔔
🔔 YOU: V{LOCAL_VER} -> NEW: V{remote} 🔔
🔔 {msg} 🔔
🔔 KING EHAB, UPDATE NOW! 🔔
🔔🔔🔔🔔🔔🔔🔔🔔{RESET}
{Y}[Y] YES 🔥  [N] NO 😴{RESET}""")
            ch = input(f"{C}UPDATE? ➤ {RESET}").lower()
            if ch == 'y':
                print(f"{G}[+] Downloading V{remote}... 🚀{RESET}")
                nr = requests.get(FILE_RAW, timeout=15)
                if nr.status_code == 200:
                    open(__file__, 'w', encoding='utf-8').write(nr.text)
                    print(f"{G}[+] DONE! Run again: python {os.path.basename(__file__)}{RESET}")
                    sys.exit()
                else:
                    print(f"{R}[-] File not found on GitHub! Upload {os.path.basename(__file__)} first!{RESET}")
                    time.sleep(2)
        else:
            print(f"{G}[+] You have latest version V{LOCAL_VER} ✅{RESET}")
            time.sleep(1)
    except Exception as e:
        print(f"{R}[-] Update check error: {e}{RESET}")
        time.sleep(1)

def menu():
    banner()
    print(f"""{G}
[01] 🔥 IP Tracker          [07] 📧 Email Bomber
[02] 📱 Phone Tracker       [08] 🔑 Password Gen
[03] 🌐 Port Scanner        [09] 📷 Cam Phisher
[04] 🔍 User Finder         [10] 🌍 Site Info
[05] 💣 SMS Bomber          [11] 👑 Admin Panel Finder
[06] 📡 DDOS Tool           [12] 🎨 Deluxe UI
{Y}═══════════════════════════════════════════════════════
[00] 🚪 EXIT{RESET}""")

def main():
    check_update()
    while True:
        menu()
        c = input(f"{C}\nDragon ➤ {RESET}")
        if c == "00" or c == "0":
            print(f"{Y}Bye King! 👑{RESET}"); break
        elif c in [str(i) for i in range(1,13)]:
            print(f"{G}[*] Tool {c} - Coming Soon in V4.2! 🔥{RESET}")
            input(f"{Y}Press Enter...{RESET}")
        else:
            print(f"{R}Invalid!{RESET}"); time.sleep(0.5)

if __name__ == "__main__":
    main()
