#!/usr/bin/env python3
# DRAGON V4.1 DELUXE - KING EHAB - 20 BUTTONS - FINAL FIXED

import os, sys, requests, time, json, socket, random, string, hashlib

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
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
{Y}      👑 KING EHAB V4.1 - 20 TOOLS DELUXE 🔥🐲
{G}           التنين اليمني المطور - بدون أخطاء{RST}
""")

def check_update():
    print(f"{C}[+] Checking Dragon Update...{RST}")
    try:
        r = requests.get(REPO_RAW, timeout=5)
        remote_ver = r.json().get("version", LOCAL_VER)
        print(f"{W}[+] Local: {LOCAL_VER} | GitHub: {remote_ver}{RST}")
        if remote_ver != LOCAL_VER:
            print(f"{Y}[!] New version {remote_ver}! Updating...{RST}")
            new_code = requests.get(FILE_RAW, timeout=10).text
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(new_code)
            print(f"{G}Updated! Run again{RST}")
            sys.exit()
        else:
            print(f"{G}[+] You have latest version V4.1 ✅{RST}")
    except:
        print(f"{R}[-] Update check skipped (no internet){RST}")

def check_code():
    print(f"{C}[*] Checking activation...{RST}")
    try:
        r = requests.get(CODES_RAW, timeout=7)
        data = r.json()
        
        valid_codes = {}
        if "codes" in data:
            for item in data["codes"]:
                if item.get("active") == True:
                    valid_codes[item.get("code")] = item.get("owner", "King")

        # رسالة الترحيب من ملفك
        if "message" in data:
            print(f"{Y}📢 {data['message']}{RST}")

        if not valid_codes:
            print(f"{R}[-] No active codes in server!{RST}")
            sys.exit()

        code = input(f"{P}🔑 ENTER DRAGON CODE ➤ {RST}").strip()
        
        if code in valid_codes:
            owner = valid_codes[code]
            print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}")
            print(f"{G}[+] Code OK! ✅{RST}")
            print(f"{Y}🐲 Welcome King: {owner} 👑{RST}")
            print(f"{Y}🔥 Code: {code}{RST}")
            print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RST}")
            time.sleep(1.5)
            return owner
        else:
            print(f"{R}[-] Invalid Code! Contact @Ehab Al-Dabai{RST}")
            sys.exit()
    except Exception as e:
        print(f"{R}[-] Code server error: {e}{RST}")
        sys.exit()

# --- أدوات آمنة 100% ---

def tool_ip():
    ip = input(f"{C}Enter IP/Domain ➤ {RST}").strip()
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        print(f"{G}{json.dumps(r, indent=2, ensure_ascii=False)}{RST}")
    except Exception as e:
        print(f"{R}Error: {e}{RST}")
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

def tool_site():
    domain = input(f"{C}Enter Domain ➤ {RST}").strip()
    try:
        r = requests.get(f"https://{domain}", timeout=5)
        print(f"{G}[+] Status: {r.status_code}{RST}")
        print(f"{G}[+] Server: {r.headers.get('Server','Unknown')}{RST}")
    except Exception as e:
        print(f"{R}{e}{RST}")
    input(f"{Y}Press Enter...{RST}")

def not_ready():
    print(f"{Y}[!] هذه الأداة قيد التطوير - ضيف كودك هنا يا ملك{RST}")
    input(f"{Y}Press Enter...{RST}")

def menu(owner):
    while True:
        banner()
        print(f"{P}👑 Logged as: {owner} | V4.1 DELUXE{RST}\n")
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
        elif choice == "02": not_ready()
        elif choice == "03": tool_port()
        elif choice == "04": tool_pass()
        elif choice == "05": tool_site()
        elif choice == "06": not_ready()
        elif choice == "07": not_ready()
        elif choice == "14": tool_hash()
        elif choice == "10": os.system('clear')
        elif choice in [str(i).zfill(2) for i in range(1,21)]:
            not_ready()
        else:
            print(f"{R}Invalid Choice!{RST}"); time.sleep(1)

if __name__ == "__main__":
    banner()
    check_update()
    king_name = check_code()
    menu(king_name)
