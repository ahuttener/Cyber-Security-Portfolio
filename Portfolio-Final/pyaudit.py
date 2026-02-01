import hashlib
import sys
import argparse
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

BANNER = f"""
{Fore.CYAN}
 ██████╗ ██╗   ██╗ █████╗ ██╗   ██╗██████╗ ██╗████████╗
 ██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
 ██████╔╝ ╚████╔╝ ███████║██║   ██║██║  ██║██║   ██║   
 ██╔═══╝   ╚██╔╝  ██╔══██║██║   ██║██║  ██║██║   ██║   
 ██║        ██║   ██║  ██║╚██████╔╝██████╔╝██║   ██║   
 ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   
{Style.RESET_ALL}
 {Fore.RED}🔥 ELITE PASSWORD AUDIT TOOL 🔥{Style.RESET_ALL}
 {Fore.CYAN}{'-' * 50}{Style.RESET_ALL}
"""

def crack_hash(target_hash, wordlist_path, hash_type):
    print(BANNER)
    print(f"[*] Target: {target_hash}")
    print(f"[*] Wordlist: {wordlist_path}")
    print(f"[*] Mode: {Fore.RED}ATTACK{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-' * 50}{Style.RESET_ALL}\n")

    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()

                if hash_type == 'md5':
                    hashed_pass = hashlib.md5(password.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
                else:
                    print(f"{Fore.YELLOW}[!] Hash type not supported.{Style.RESET_ALL}")
                    return

                if hashed_pass == target_hash:
                    print(f"[*] Cracking {target_hash[:10]}... ({hash_type.upper()}) -> {Fore.GREEN}PASSWORD FOUND: {password}{Style.RESET_ALL}")
                    return password

            print(f"\n{Fore.RED}[!] Password not found in wordlist.{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}[!] Error: Wordlist file not found.{Style.RESET_ALL}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyAudit - Advanced Password Cracker")
    parser.add_argument("-hash", help="The target hash string", required=True)
    parser.add_argument("-w", help="Path to the wordlist file", required=True)
    parser.add_argument("-t", help="Hash type (md5, sha256)", required=True)

    args = parser.parse_args()
    crack_hash(args.hash, args.w, args.t)
