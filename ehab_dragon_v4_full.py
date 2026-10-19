#!/usr/bin/env python3
# DRAGON V4.2 FINAL - KING EHAB - FIXED WEAK NET + OFFLINE CACHE

import os, sys, requests, time, json, socket, random, string, hashlib
import urllib3
urllib3.disable_warnings()

LOCAL_VER = "4.2"
REPO_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"
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
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
{Y}      👑 KING EHAB V4.2 - OFFLINE MODE FIX 🔥🐲
{G}           يشتغل حتى بدون نت - إصلاح تعز{RST}
""")

def check_update():
    print(f"{C}[+] Checking Dragon Update...{RST}")
    try:
        r = requests.get(REPO_RAW, timeout=3)
        remote_ver = r.json().get("version", LOCAL_VER)
        if remote_ver != LOCAL_VER:
            print(f"{Y}[!] New version {remote_ver} available!{RST}")
        else:
            print(f"{G}[+] V4.2 Latest ✅{RST}")
    except:
        print(f"{Y}[!] Offline Mode - Skipping update check 💤{RST}")
        print(f"{G}[+] Continuing with local V4.2 ✅{RST}")
        return

def check_code():
    print(f"{C}[*] Checking activation...{RST}")
    cache_file = os.path.expanduser("~/.dragon_codes.json")
    valid_codes = {}
    message = "اهلا بالملك ايهاب"

    for attempt in range(3):
        try:
            print(f"{Y}[{attempt+1}/3] Trying server...{RST}")
            r = requests.get(CODES_RAW, timeout=8, verify=False)
            data = r.json()
            if "codes" in data:
                for item in data["codes"]:
                    if item.get("active") == True:
                        valid_codes[item.get("code")] = item.get("owner", "King")
            message = data.get("message", message)
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f)
            print(f"{G}[+] Online mode ✅{RST}")
            break
        except:
            print(f"{R}[!] Weak net, retrying...{RST}")
            time.sleep(1)

    if not valid_codes:
        try:
            if os.path.exists(cache_file):
                print(f"{Y}[!] No internet - Using offline cache 💾{RST}")
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for item in data.get("codes", []):
                    if item.get("active") == True:
                        valid_codes[item.get("code")] = item.get("owner", "King")
                message = data.get("message", message)
            else:
                print(f"{Y}[!] Offline emergency mode 🔥{RST}")
                valid_codes = {"EHAB-VIP": "الملك ايهاب", "TEST-123": "Tester"}
        except:
            valid_codes = {"EHAB-VIP": "الملك ايهاب"}

    print(f"{Y}📢 {message}{RST}")
    code = input(f"{P}🔑 ENTER DRAGON CODE ➤ {RST}").strip()
    if code in valid_codes:
        owner = valid_codes[code]
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}")
        print(f"{G}[+] Code OK! Welcome {owner} 👑{RST}")
        print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}")
        time.sleep(1)
        return owner
    else:
        print(f"{R}[-] Invalid Code! Contact @Ehab{RST}")
        sys.exit()

def tool_ip():
    ip = input(f"{C}Enter IP/Domain ➤ {RST}").strip()
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        print(f"{G}{json.dumps(r, indent=2, ensure_ascii=False)}{RST}")
    except Exception as e:
        print(f"{R}Error: {e}{RST}")
    input(f"{Y}Press Enter...{RST}")

def tool_port():
    host = input(f"{C}Host (e.g google.com) ➤ {RST}").strip()
    try:
        for p in [21,22,80,443,3306,8080]:
            s = socket.socket(); s.settimeout(1)
            res = s.connect_ex((host, p))
            print(f"{G if res==0 else R}[{'OPEN' if res==0 else 'CLOSED'}] Port {p}{RST}")
            s.close()
    except Exception as e:
        print(f"{R}{e}{RST}")
    input(f"{Y}Press Enter...{RST}")

def tool_pass():
    try:
        l = int(input(f"{C}Length (8-32) ➤ {RST}") or "12")
        chars = string.ascii_letters + string.digits + "!@#$%"
        print(f"{G}🔑 Password: {''.join(random.choice(chars) for _ in range(l))}{RST}")
    except: pass
    input(f"{Y}Press Enter...{RST}")

def tool_hash():
    txt = input(f"{C}Enter Text ➤ {RST}")
    print(f"{G}MD5: {hashlib.md5(txt.encode()).hexdigest()}{RST}")
    print(f"{G}SHA256: {hashlib.sha256(txt.encode()).hexdigest()}{RST}")
    input(f"{Y}Press Enter...{RST}")

def tool_site():
    domain = input(f"{C}Enter Domain ➤ {RST}").strip()
    try:
        r = requests.get(f"https://{domain}", timeout=5, verify=False)
        print(f"{G}[+] Status: {r.status_code}{RST}")
    except Exception as e:
        print(f"{R}{e}{RST}")
    input(f"{Y}Press Enter...{RST}")

def not_ready():
    print(f"{Y}[!] Tool coming soon - ضيف كودك هنا{RST}")
    input(f"{Y}Press Enter...{RST}")

def menu(owner):
    while True:
        banner()
        print(f"{P}👑 Logged as: {owner} | V4.2 OFFLINE FIX{RST}\n")
        print(f"""{Y}[01] 🔥 IP Tracker       [11] 🔍 Username Finder
[02] 📱 Phone Info        [12] 🎨 Deluxe UI
[03] 🌐 Port Scanner      [13] 📷 QR Generator
[04] 🔑 Password Gen      [14] 🔐 Hash Generator
[05] ℹ️ Site Info         [15] 🌍 My IP
[06] 👑 Admin Finder      [16] ⏰ Date & Time
[07] 📧 Email Validator   [17] 🧮 Calculator
[08] 🔗 URL Short Check   [18] 🎲 Random Number
[09] 🛰️ Ping Tool        [19] 💾 System Info
[10] 🧹 Clear Screen      [20] 📞 Contact King
{R}[00] 🚪 EXIT{W}
""")
        choice = input(f"{C}Dragon > {RST}").strip()
        if choice == "00": 
            print(f"{Y}Bye King {owner}! 👑{RST}"); sys.exit()
        elif choice == "01": tool_ip()
        elif choice == "03": tool_port()
        elif choice == "04": tool_pass()
        elif choice == "05": tool_site()
        elif choice == "14": tool_hash()
        elif choice == "10": os.system('clear')
        else: not_ready()

if __name__ == "__main__":
    banner()
    check_update()
    king_name = check_code()
    menu(king_name)
