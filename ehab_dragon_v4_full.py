#!/usr/bin/env python3
# DRAGON V4.1 - KING EHAB EDITION 🐲👑
# 12 Tools + Deluxe UI + Auto Update + Code System

import os, sys, time, requests, json

LOCAL_VER = "4.1"
REPO_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"
FILE_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/ehab_dragon_v4_full.py"
CODES_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/codes.json"

# Colors
R="\033[1;31m"; G="\033[1;32m"; Y="\033[1;33m"; B="\033[1;34m"
C="\033[1;36m"; W="\033[1;37m"; P="\033[1;35m"; RESET="\033[0m"

def banner():
    os.system('clear')
    print(f"""{R}
  EHAB
     {Y}Ehab Al-Dabai YE | Android 15 {W}
  DRAGON
     KING EHAB V{LOCAL_VER} - DELUXE EDITION 👑{RESET}""")

def check_update():
    print(f"{C}[+] Checking Dragon Update...{RESET}")
    try:
        r = requests.get(REPO_RAW, timeout=5)
        remote_ver = r.json().get("version", LOCAL_VER)
        if remote_ver != LOCAL_VER:
            print(f"{Y}[!] New version {remote_ver} found! Current {LOCAL_VER}{RESET}")
            ans = input(f"{Y}UPDATE? [y/n] > {RESET}").lower()
            if ans == 'y':
                print(f"{G}[+] Downloading V{remote_ver}.... 🚀{RESET}")
                new_code = requests.get(FILE_RAW, timeout=10).text
                with open(__file__, 'w') as f:
                    f.write(new_code)
                print(f"{G}~ Updated! Run again!{RESET}")
                sys.exit()
        else:
            print(f"{G}[+] You have latest version V{LOCAL_VER} ✅{RESET}")
    except Exception as e:
        print(f"{R}[-] Update check failed: {e}{RESET}")

def check_code():
    print(f"{C}[*] Checking activation...{RESET}")
    try:
        r = requests.get(CODES_RAW, timeout=5)
        data = r.json()  # مثلا: ["EHAB-123", "DRAGON-VIP"]
        # يدعم list أو dict
        valid = []
        if isinstance(data, list):
            valid = data
        elif isinstance(data, dict):
            valid = list(data.values()) + list(data.keys())

        code = input(f"{P}🔑 ENTER DRAGON CODE ➤ {RESET}").strip()
        if code in valid:
            print(f"{G}[+] Code OK! Welcome King 👑{RESET}")
            time.sleep(1)
            return True
        else:
            print(f"{R}[-] Invalid Code! Contact Ehab Al-Dabai{RESET}")
            sys.exit()
    except Exception as e:
        print(f"{R}[-] Code server error: {e}{RESET}")
        sys.exit()

def menu():
    banner()
    print(f"""
{Y}[01] IP Tracker       [07] Tool 7
[02] Phone Tracker     [08] Tool 8
[03] Port Scanner      [09] Tool 9
[04] User Finder       [10] Tool 10
[05] Tool 5            [11] Tool 11
[06] Tool 6            [12] Deluxe UI{W}
""")
    choice = input(f"{C}Dragon > {RESET}")
    # هنا تحط دوال أدواتك الخاصة
    print(f"{Y}You chose {choice} - ضع كود أداتك هنا{RESET}")

# --- التشغيل الرئيسي مرة واحدة ---
if __name__ == "__main__":
    banner()
    check_update()
    check_code()
    menu()
