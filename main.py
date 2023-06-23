import sys, requests, re, os
from bs4 import BeautifulSoup
import http.client as httplib
from inputimeout import inputimeout, TimeoutOccurred


yes = {'yes','y', 'ye', ''}
no = {'no','n'}

def hav_da_internetz() -> bool:
    con = httplib.HTTPSConnection("1.1.1.1", timeout=5)
    try:
        con.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        con.close()



# checks for args
if len(sys.argv) <= 1:
    print("apparently no command was entered????")
    exit()

# check for network connection
if hav_da_internetz() == False:
    print(f"no internetz detected, try this url lol: https://command-not-found.com/{sys.argv[1]}")
    exit()


link = f"https://command-not-found.com/{sys.argv[1]}"
req = requests.get(link)

# check if command even exists on da site
# by checking if redirected to the main page
if req.url == "https://command-not-found.com/":
    print("command not found on site, exiting...")
    exit()


site = req.content
soup = BeautifulSoup(site, 'html.parser')



# check for if there is a pacman command in the site
if soup.find(string=re.compile("pacman")) == None:
    print("pacman command not found on site, exiting...")
    exit()

else:
    print(f"command: 'sudo {soup.find(string=re.compile('pacman'))}'")
    pass


try:
    run_comm = inputimeout(prompt='do you wish to install dat package? [y/N]\n> ', timeout=3).lower()
except TimeoutOccurred:
    print("you took too long to answer you slow fat fuck, we defaulted to no AKA, we exited")
    run_comm = 'no'


if run_comm in yes:
    os.system(f"sudo {soup.find(string=re.compile('pacman'))} --noconfirm")

elif run_comm in no:
    exit()
