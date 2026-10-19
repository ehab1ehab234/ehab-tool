#!/usr/bin/env python3
# DRAGON V4.1 FIXED - ALL WORKING - KING EHAB

import os, sys, requests, time, json, socket, random, string, hashlib, platform, datetime, re
import urllib.parse, urllib3
urllib3.disable_warnings()

LOCAL_VER = "4.1"
CODES_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/codes.json"
VERSION_RAW = "https://raw.githubusercontent.com/ehab1ehab234/ehab-tool/main/version.json"

R="\033[1;31m"
G="\033[1;32m"
Y="\033[1;33m"
C="\033[1;36m"
P="\033[1;35m"
W="\033[1;37m"
RST="\033[0m"

def banner():
    os.system('clear')
    print(R + "██████╗ ██████╗  █████╗  ██████╗  ██████╗" + RST)
    print(Y + "  👑 KING EHAB V4.1 FIXED - 20 TOOLS 🔥" + RST)
    print(G + "       كل الازرار شغالة" + RST)

def check_code():
    cache = os.path.expanduser("~/.dragon_codes.json")
    valid = {"EHAB-VIP":"الملك ايهاب","TAIZ-777":"ملك تعز","KING-2026":"الملك","TEST-123":"Tester","DRAGON-999":"تنين اليمن"}
    try:
        r = requests.get(CODES_RAW, timeout=6, verify=False)
        data = r.json()
        valid = {}
        for x in data.get("codes", []):
            if x.get("active"):
                valid[x["code"]] = x["owner"]
        with open(cache, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(G + "[+] Online" + RST)
    except:
        print(Y + "[!] Offline - cache" + RST)
    code = input(P + "🔑 CODE ➤ " + RST).strip()
    if code in valid:
        print(G + "Welcome " + valid[code] + RST)
        time.sleep(1)
        return valid[code]
    else:
        print(R + "Invalid! Try EHAB-VIP" + RST)
        sys.exit()

def pause():
    input(Y + "Enter to continue..." + RST)

def menu(owner):
    while True:
        banner()
        print(P + "👑 " + owner + " | V4.1 FIXED" + RST + "\n")
        print(Y + "[01] IP Tracker     [11] Username Finder" + RST)
        print(Y + "[02] Phone Info     [12] Colors Test" + RST)
        print(Y + "[03] Port Scanner   [13] QR Link" + RST)
        print(Y + "[04] Pass Gen       [14] Hash Gen" + RST)
        print(Y + "[05] Site Info      [15] My IP" + RST)
        print(Y + "[06] Admin Finder   [16] Date Time" + RST)
        print(Y + "[07] Email Check    [17] Calculator" + RST)
        print(Y + "[08] URL Check      [18] Random Num" + RST)
        print(Y + "[09] Ping           [19] Sys Info" + RST)
        print(Y + "[10] Clear          [20] Contact" + RST)
        print(R + "[00] EXIT" + RST)

        c = input(C + "Dragon > " + RST).strip()
        if len(c) == 1:
            c = "0" + c

        if c == "00":
            sys.exit()

        elif c == "01":
            ip = input(C + "IP: " + RST).strip()
            try:
                r = requests.get("http://ip-api.com/json/" + ip, timeout=6).json()
                print(G + str(r) + RST)
            except Exception as e:
                print(R + str(e) + RST)
            pause()

        elif c == "02":
            phone = input(C + "Phone: " + RST).strip()
            print(G + "Phone: " + phone + " | Digits: " + str(phone.replace("+","").isdigit()) + RST)
            pause()

        elif c == "03":
            host = input(C + "Host: " + RST).strip()
            for port in [21,22,80,443,8080]:
                s = socket.socket()
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(G + "[OPEN] " + str(port) + RST)
                else:
                    print(R + "[CLOSED] " + str(port) + RST)
                s.close()
            pause()

        elif c == "04":
            length = input(C + "Length: " + RST).strip()
            if not length:
                length = "12"
            length = int(length)
            chars = string.ascii_letters + string.digits + "!@#$%"
            pwd = ""
            for i in range(length):
                pwd += random.choice(chars)
            print(G + pwd + RST)
            pause()

        elif c == "05":
            d = input(C + "Domain: " + RST).strip()
            try:
                r = requests.get("https://" + d, timeout=6, verify=False)
                print(G + "Status: " + str(r.status_code) + RST)
            except Exception as e:
                print(R + str(e) + RST)
            pause()

        elif c == "06":
            d = input(C + "Domain: " + RST).strip()
            paths = ["admin","wp-admin","login"]
            for p in paths:
                try:
                    url = "https://" + d + "/" + p
                    r = requests.get(url, timeout=4, verify=False)
                    print(G + url + " -> " + str(r.status_code) + RST)
                except:
                    pass
            pause()

        elif c == "07":
            email = input(C + "Email: " + RST).strip()
            ok = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)
            print(G + "Valid" + RST if ok else R + "Invalid" + RST)
            pause()

        elif c == "08":
            url = input(C + "URL: " + RST).strip()
            if not url.startswith("http"):
                url = "https://" + url
            try:
                r = requests.head(url, timeout=5, verify=False, allow_redirects=True)
                print(G + r.url + " | " + str(r.status_code) + RST)
            except Exception as e:
                print(R + str(e) + RST)
            pause()

        elif c == "09":
            host = input(C + "Host: " + RST).strip()
            os.system("ping -c 4 " + host)
            pause()

        elif c == "10":
            os.system('clear')

        elif c == "11":
            user = input(C + "Username: " + RST).strip()
            for site in ["https://github.com/"+user, "https://instagram.com/"+user]:
                try:
                    r = requests.get(site, timeout=4)
                    print(G + site + " " + str(r.status_code) + RST)
                except:
                    pass
            pause()

        elif c == "12":
            print(R + "RED " + G + "GREEN " + Y + "YELLOW " + C + "CYAN" + RST)
            pause()

        elif c == "13":
            text = input(C + "Text: " + RST).strip()
            enc = urllib.parse.quote(text)
            link = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=" + enc
            print(G + link + RST)
            pause()

        elif c == "14":
            t = input(C + "Text: " + RST)
            print(G + "MD5: " + hashlib.md5(t.encode()).hexdigest() + RST)
            print(G + "SHA256: " + hashlib.sha256(t.encode()).hexdigest() + RST)
            pause()

        elif c == "15":
            try:
                r = requests.get("https://api.ipify.org?format=json", timeout=5).json()
                print(G + str(r) + RST)
            except Exception as e:
                print(R + str(e) + RST)
            pause()

        elif c == "16":
            print(G + str(datetime.datetime.now()) + RST)
            pause()

        elif c == "17":
            expr = input(C + "Calc: " + RST).strip()
            try:
                print(G + str(eval(expr)) + RST)
            except Exception as e:
                print(R + str(e) + RST)
            pause()

        elif c == "18":
            print(G + str(random.randint(1,100)) + RST)
            pause()

        elif c == "19":
            print(G + platform.platform() + RST)
            pause()

        elif c == "20":
            print(Y + "King Ehab - Taiz - github.com/ehab1ehab234/ehab-tool" + RST)
            pause()

if __name__ == "__main__":
    banner()
    king = check_code()
    menu(king)
