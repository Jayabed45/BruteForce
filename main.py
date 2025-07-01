import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = ""  # <-- Target URL
start_id = 1
end_id = 3000

for user_id in range(start_id, end_id + 1):
    full_url = f"{url}{user_id}"
    
    try:
        response = requests.get(full_url, verify=False)  # 👈 Disable SSL verification
        if response.status_code == 200:
            print(f"[+] Found: {full_url}")
            print(response.text[:200])
        else:
            print(f"[-] ID {user_id} not found ({response.status_code})")
    except Exception as e:
        print(f"[!] Error on ID {user_id}: {e}")

print("[*] Done")
