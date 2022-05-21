import requests

url = 'https://www.minecraft-schematics.com/schematic/14886/download/action/?type=schematic'

cookies = {
    '__cfduid=d41b3fc66eb7642f1e24a95838988add01595608894&PHPSESSID=d480jrh774nhl1r6vthbdca8al&CookieScriptConsent=%7B%22action%22%3A%22accept%22%7D&uid=953570&ukey=ubbv284xm5gftvm8e9np87ez0r425cx4pw0x1emrdyicu&utoken=gcw0yo4vtjlivpkr5hr4'
}

headers = {
    'Host: www.minecraft-schematics.com',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language: de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding: gzip, deflate, br',
    'DNT: 1',
    'Connection: keep-alive',
    'Referer: https://www.minecraft-schematics.com/schematic/14886/download/',
    'Cookie: __cfduid=d41b3fc66eb7642f1e24a95838988add01595608894; PHPSESSID=d480jrh774nhl1r6vthbdca8al; CookieScriptConsent={"action":"accept"}; uid=953570; ukey=ubbv284xm5gftvm8e9np87ez0r425cx4pw0x1emrdyicu; utoken=gcw0yo4vtjlivpkr5hr4',
    'Upgrade-Insecure-Requests: 1',
    'TE: Trailers'
}

request = requests.get(url=url, cookies=cookies, headers=headers)

print(request)