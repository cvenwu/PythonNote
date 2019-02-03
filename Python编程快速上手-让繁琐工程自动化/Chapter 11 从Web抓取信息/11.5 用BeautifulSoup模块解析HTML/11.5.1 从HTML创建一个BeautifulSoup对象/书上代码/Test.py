import requests, bs4
res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem %s ' % exc)


noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))

