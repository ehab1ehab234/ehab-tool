#!/usr/bin/env python3
# DRAGON V4.1 - KING EHAB - FULL FIXED

import os, sys, requests, time, json

LOCAL_VER = "4.1"
REPO_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"
FILE_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/ehab_dragon_v4_full.py"
CODES_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/codes.json"

R="\033[1;31m"; G="\033[1;32m"; Y="\033[1;33m"; C="\033[1;36m"; P="\033[1;35m"; W="\033[1;37m"; RST="\033[0m"

def banner():
    os.system('clear')
    print(f"""{R}
██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
{Y}     KING EHAB V4.1 - DELUXE EDITION 👑🔥{RST}""")

def check_update():
    print(f"{C}[+] Checking Dragon Update...{RST}")
    try:
        r = requests.get(REPO_RAW, timeout=5)
        remote_ver = r.json().get("version", LOCAL_VER)
        print(f"[+] Local: {LOCAL_VER} | GitHub: {remote_ver}")
        if remote_ver != LOCAL_VER:
            print(f"{Y}[!] New version {remote_ver}! Updating...{RST}")
            new_code = requests.get(FILE_RAW, timeout=10).text
            with open(__file__, 'w') as f:
                f.write(new_code)
            print(f"{G}Updated! Run again{RST}")
            sys.exit()
        else:
            print(f"{G}[+] You have latest version V4.1 ✅{RST}")
    except Exception as e:
        print(f"{R}[-] Update check failed{RST}")

def check_code():
    print(f"{C}[*] Checking activation...{RST}")
    try:
        r = requests.get(CODES_RAW, timeout=5)
        data = r.json()
        valid = []
        if isinstance(data, list):
            valid = data
        elif isinstance(data, dict):
            valid = list(data.keys()) + list(data.values())
        
        code = input(f"{P}🔑 ENTER DRAGON CODE ➤ {RST}").strip()
        if code in valid:
            print(f"{G}[+] Code OK! Welcome King Ehab 👑{RST}")
            time.sleep(1)
        else:
            print(f"{R}[-] Invalid Code! Contact @Ehab Al-Dabai{RST}")
            sys.exit()
    except Exception as e:
        print(f"{R}[-] Code server error: {e}{RST}")
        sys.exit()

def menu():
    print(f"""
{Y}[01] 🔥 IP Tracker        [07] 📧 Email Bomber
[02] 📱 Phone Tracker      [08] 🔑 Password Gen
[03] 🌐 Port Scanner       [09] 📷 Cam Phisher
[04] 👤 User Finder        [10] ℹ️ Site Info
[05] 💣 SMS Bomber         [11] 👑 Admin Panel Finder
[06] 💥 DDOS Tool          [12] 🎨 Deluxe UI
{R}[00] 🚪 EXIT{W}
""")
    choice = input(f"{C}Dragon > {RST}")
    
    if choice == "00":
        print(f"{Y}Bye King! 👑{RST}")
        sys.exit()
    else:
        print(f"{G}You chose {choice} -> ضع كود أداتك هنا{RST}")
        # هنا تحط: if choice == "01": ip_tracker() الخ
        input("Press Enter...")

# --- هذا هو الترتيب الصحيح اللي كان ناقص عندك ---
if __name__ == "__main__":
    banner()
    check_update()
    check_code()
    menu()
