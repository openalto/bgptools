import requests
from pyquery import PyQuery as pq


def get_ipv4_prefixes(asn):
    fetch = requests.get('https://www.dan.me.uk/bgplookup?asn=%d' % asn)
    html = pq(fetch.text)
    rows = html('#content-left-in > div > table > tr')
    prefixes = []
    for row in rows:
        prefixes.append(pq(row).text().splitlines()[0])
    return prefixes


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: %s <asn>' % sys.argv[0])
        sys.exit(-1)
    asn = int(sys.argv[1])
    prefixes = get_ipv4_prefixes(asn)
    for prefix in prefixes:
        print(prefix)
