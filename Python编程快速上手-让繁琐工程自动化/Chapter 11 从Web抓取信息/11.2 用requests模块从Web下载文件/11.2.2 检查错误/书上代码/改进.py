import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

