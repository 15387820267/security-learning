import requests

urls = [
    "http://scanme.nmap.org",
    "http://scanme.nmap.org/notexit",
    "http://scanme.nmap.org/index.html",
]

def check_url(url):
    try:
        r = requests.get(url,timeout=5)
        return f"{url} -> {r.status_code}"
    except requests.RequestException as e:
        return f"{url} -> 错误：{e}"

def main():
    for url in urls:
        print(check_url(url))

main()