import requests

proxy_port = 9050  # cámbialo por el puerto que estás probando
channel = "nachix"

proxies = {
    'http': f'socks5h://127.0.0.1:{proxy_port}',
    'https': f'socks5h://127.0.0.1:{proxy_port}'
}

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Referer': f'https://kick.com/{channel}'
}

url = f"https://kick.com/api/v1/channels/{channel}"

r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
print("Status:", r.status_code)
print("Respuesta JSON:", r.json())
