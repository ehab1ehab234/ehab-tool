
#!/usr/bin/env python3
# DRAGON V4.1 ULTIMATE - 20 BUTTONS ALL WORKING - KING EHAB

import os, sys, requests, time, json, socket, random, string, hashlib, platform, datetime, re, urllib.parse
import urllib3
urllib3.disable_warnings()

LOCAL_VER = "4.1"
CODES_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/codes.json"
VERSION_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"

R="\033[1;31m"; G="\033[1;32m"; Y="\033[1;33m"; C="\033[1;36m"; P="\033[1;35m"; W="\033[1;37m"; RST="\033[0m"

def banner():
    os.system('clear')
    print(f"""{R}
██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
{Y}      👑 KING EHAB V4.1 ULTIMATE - 20 TOOLS 🔥🐲
{G}           كل الأزرار شغالة حقيقي{RST}
""")

def check_update():
    try:
        requests.get(VERSION_RAW, timeout=2)
        print(f"{G}[+] V4.1 Ultimate ✅{RST}")
    except:
        print(f"{Y}[!] Offline Mode ✅{RST}")

def check_code():
    cache = os.path.expanduser("~/.dragon_codes.json")
    valid = {"EHAB-VIP": "الملك ايهاب", "TAIZ-777": "ملك تعز", "KING-2026": "الملك", "TEST-123": "Tester", "DRAGON-999": "تنين اليمن"}
    msg = "اهلا بالملك ايهاب 👑 V4.1 Ultimate"
    try:
        r = requests.get(CODES_RAW, timeout=6, verify=False)
        data = r.json()
        valid = {x["code"]: x["owner"] for x in data.get("codes", []) if x.get("active")}
        msg = data.get("message", msg)
        with open(cache, 'w', encoding='utf-8') as f: json.dump(data, f)
    except:
        if os.path.exists(cache):
            try:
                with open(cache, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    valid = {x["code"]: x["owner"] for x in data.get("codes", []) if x.get("active")}
            except: pass
    print(f"{Y}📢 {msg}{RST}")
    code = input(f"{P}🔑 ENTER CODE ➤ {RST}").strip()
    if code in valid:
        print(f"{G}[+] Welcome {valid[code]} 👑{RST}"); time.sleep(1)
        return valid[code]
    else:
        print(f"{R}[-] Invalid! Use EHAB-VIP{RST}"); sys.exit()

def pause(): input(f"{Y}Press Enter...{RST}")

# === TOOLS ===

def tool_01_ip():
    ip = input(f"{C}IP/Domain ➤ {RST}").strip()
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=6).json()
        print(f"{G}Country: {r.get('country')} - City: {r.get('city')} - ISP: {r.get('isp')}\nLat: {r.get('lat')}, Lon: {r.get('lon')}{RST}")
    except Exception as e: print(f"{R}{e}{RST}")
    pause()

def tool_02_phone():
    phone = input(f"{C}Phone (with country code) ➤ {RST}").strip()
    print(f"{G}Phone: {phone}\nCountry Check: {'Yemen +967' if phone.startswith('967') or phone.startswith('+967') else 'Intl'}\nLength: {len(phone)}\nValid: {phone.replace('+','').isdigit()}{RST}")
    pause()

def tool_03_port():
    host = input(f"{C}Host ➤ {RST}").strip()
    ports = [21,22,23,25,53,80,110,443,3306,8080]
    for p in ports:
        s=socket.socket(); s.settimeout(1)
        res = s.connect_ex((host,p))
        print(f"{G if res==0 else R}[{'OPEN' if res==0 else 'CLOSED'}] {host}:{p}{RST}")
        s.close()
    pause()

def tool_04_pass():
    try:
        l = int(input(f"{C}Length (6-64) ➤ {RST}") or "16")
        l = max(6, min(64, l))
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        pwd = ''.join(random.choice(chars) for _ in range(l))
        print(f"{G}🔑 {pwd}{RST}\nStrength: {'STRONG' if l>=12 else 'MEDIUM'}")
    except: pass
    pause()

def tool_05_site():
    d = input(f"{C}Domain (example.com) ➤ {RST}").strip()
    try:
        r = requests.get(f"https://{d}", timeout=6, verify=False)
        print(f"{G}Status: {r.status_code}\nServer: {r.headers.get('Server','?')}\nTitle: {r.text[:200]}{RST}")
    except Exception as e: print(f"{R}{e}{RST}")
    pause()

def tool_06_admin():
    d = input(f"{C}Domain ➤ {RST}").strip()
    paths = ["admin","administrator","admin/login","wp-admin","login","cpanel"]
    for p in paths:
        try:
            url = f"https://{d}/{p}"
            r = requests.get(url, timeout=3, verify=False)
            if r.status_code in [200,301,302]:
                print(f"{G}[FOUND] {url} -> {r.status_code}{RST}")
            else:
                print(f"{R}[NO] {p}{RST}")
        except: pass
    pause()

def tool_07_email():
    email = input(f"{C}Email ➤ {RST}").strip()
    valid = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)
    print(f"{G if valid else R}{'Valid ✅' if valid else 'Invalid ❌'} - {email}{RST}")
    pause()

def tool_08_url():
    url = input(f"{C}URL ➤ {RST}").strip()
    try:
        if not url.startswith("http"): url="https://"+url
        r = requests.head(url, timeout=5, allow_redirects=True, verify=False)
        print(f"{G}Final URL: {r.url}\nStatus: {r.status_code}\nLength: {len(r.url)}{RST}")
    except Exception as e: print(f"{R}{e}{RST}")
    pause()

def tool_09_ping():
    host = input(f"{C}Host to ping ➤ {RST}").strip()
    os.system(f"ping -c 4 {host}")
    pause()

def tool_10_clear(): os.system('clear')

def tool_11_user():
    user = input(f"{C}Username ➤ {RST}").strip()
    sites = {"Instagram": f"https://instagram.com/{user}", "GitHub": f"https://github.com/{user}", "TikTok": f"https://tiktok.com/@{user}"}
    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=4)
            print(f"{G if r.status_code==200 else R}[{name}] {url} -> {r.status_code}{RST}")
        except: print(f"{R}[{name}] Error{RST}")
    pause()

def tool_12_ui():
    print(f"{P}🎨 Dragon Colors: {R}RED {G}GREEN {Y}YELLOW {C}CYAN {P}PURPLE{RST}")
    pause()

def tool_13_qr():
    text = input(f"{C}Text for QR ➤ {RST}").strip()
    enc = urllib.parse.quote(text)
    print(f"{G}QR Link: https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={enc}{RST}")
    pause()

def tool_14_hash():
    t = input(f"{C}Text ➤ {RST}")
    print(f"{G}MD5: {hashlib.md5(t.encode()).hexdigest()}\nSHA1: {hashlib.sha1(t.encode()).hexdigest()}\nSHA256: {hashlib.sha256(t.encode()).hexdigest()}{RST}")
    pause()

def tool_15_myip():
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=5).json()
        print(f"{G}Your IP: {r.get('ip')}{RST}")
        r2 = requests.get(f"http://ip-api.com/json/{r.get('ip')}", timeout=5).json()
        print(f"Location: {r2.get('country')} - {r2.get('city')}")
    except Exception as e: print(f"{R}{e}{RST}")
    pause()

def tool_16_date():
    now = datetime.datetime.now()
    print(f"{G}Date: {now.strftime('%Y-%m-%d')}\nTime: {now.strftime('%H:%M:%S')}\nYemen: {now}{RST}")
    pause()

def tool_17_calc():
    expr = input(f"{C}Calc (e.g 5*5+10) ➤ {RST}")
    try: print(f"{G}Result: {eval(expr, {'__builtins__':None}, {})}{RST}")
    except Exception as e: print(f"{R}Error: {e}{RST}")
    pause()

def tool_18_rand():
    try:
        a = int(input(f"{C}Min ➤ {RST}") or "1")
        b = int(input(f"{C}Max ➤ {RST}") or "100")
        print(f"{G}Random: {random.randint(a,b)}{RST}")
    except: pass
    pause()

def tool_19_sys():
    print(f"{G}System: {platform.system()} {platform.release()}\nMachine: {platform.machine()}\nPython: {platform.python_version()}\nNode: {platform.node()}{RST}")
    pause()

def tool_20_contact():
    print(f"{Y}👑 King Ehab\nGitHub: github.com/ehab1ehab234/ehab-tool\nTelegram: @EhabKing\nLocation: Taiz, Yemen{RST}")
    pause()

def menu(owner):
    while True:
        banner()
        print(f"{P}👑 {owner} | V4.1 ULTIMATE - 20 TOOLS WORKING{RST}\n")
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
        c = input(f"{C}Dragon [{owner}] > {RST}").strip().zfill(2)
        if c=="00": print(f"{Y}Bye King {owner}! 👑{RST}"); sys.exit()
        elif c=="01": tool_01_ip()
        elif c=="02": tool_02_phone()
        elif c=="03": tool_03_port()
        elif c=="04": tool_04_pass()
        elif c=="05": tool_05_site()
        elif c=="06": tool_06_admin()
        elif c=="07": tool_07_email()
        elif c=="08": tool_08_url()
        elif c=="09": tool_09_ping()
        elif c=="10": tool_10_clear()
        elif c=="11": tool_11_user()
        elif c=="12": tool_12_ui()
        elif c=="13": tool_13_qr()
        elif c=="14": tool_14_hash()
        elif c=="15": tool_15_myip()
        elif c=="16": tool_16_date()
        elif c=="17": tool_17_calc()
        elif c=="18": tool_18_rand()
        elif c=="19": tool_19_sys()
        elif c=="20": tool_20_contact()
        else: print(f"{R}Invalid choice{RST}"); time.sleep(1)

if __name__ == "__main__":
    banner()
    check_update()
    king = check_code()
    menu(king)
