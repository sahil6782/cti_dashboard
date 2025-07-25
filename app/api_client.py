import requests, os

def check_virustotal(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {"x-apikey": os.getenv("VIRUSTOTAL_API_KEY")}
    response = requests.get(url, headers=headers)
    return response.json()

def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": os.getenv("ABUSEIPDB_API_KEY")}
    params = {"ipAddress": ip}
    response = requests.get(url, headers=headers, params=params)
    return response.json()
