# Modules
import sys
import requests
from termcolor import colored

# InvlaidSchema class
class InvalidSchema(Exception):
    def __init__(self, message, detail=None):
        super().__init__(message)
        self.detail = detail

# args variable for readability
args = sys.argv

# Verbose arg handling
if "-v" in args: verbose = True
else: verbose = False

if verbose: print(f"{colored("[ INFO ]", "grey")} Running CRYoink version 1.0.1, updated on 5/25/24")

# Help arg handling
if "-h" in args:
    print("CRYoink version 1.0.1")
    print()
    print("-h[elp] [ Shows this help message.                                    ]")
    print("-i[d]   [ The extension ID you would like to yoink.                   ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx.             ]")
    print("-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary. ]")
    print("-v      [ Enables verbose mode. Prints debug statements like warnings ]")
    sys.exit(0)
elif "-help" in args:
    print("CRYoink version 1.0.1")
    print()
    print("-h[elp] [ Shows this help message.                                    ]")
    print("-i[d]   [ The extension ID you would like to yoink.                   ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx.             ]")
    print("-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary. ]")
    print("-v      [ Enables verbose mode. Prints debug statements like warnings ]")
    sys.exit(0)
elif "--help" in args:
    print("CRYoink version 1.0.1")
    print()
    print("-h[elp] [ Shows this help message.                                    ]")
    print("-i[d]   [ The extension ID you would like to yoink.                   ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx.             ]")
    print("-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary. ]")
    print("-v      [ Enables verbose mode. Prints debug statements like warnings ]")
    sys.exit(0)

# ID arg handling
if "-i" in args:
    id = args[args.index("-i")+1]
elif "-id" in args:
    id = args[args.index("-id")+1]
elif "--id" in args:
    id = args[args.index("--id")+1]
else:
    print(f"{colored("[ WARNING ]", "yellow")} ID not given. Using stdin instead...")
    id = input("Enter ID: ")

# Output arg handling
if "-o" in args:
    of = args[args.index("-o")+1]
elif "-out" in args:
    of = args[args.index("-out")+1]
elif "--out" in args:
    of = args[args.index("--out")+1]
else:
    if verbose: print(f"{colored("[ INFO ]", "grey")} Argument \"-o\" not found. Defaulting output file to \"extension.crx\"...")
    of = "extension.crx"

if "-u" in args:
    url = args[args.index("-u")+1]
    url.replace("{id}", id)
elif "-url" in args:
    url = args[args.index("-url")+1]
    url.replace("{id}", id)
elif "--url" in args:
    url = args[args.index("--url")+1]
    url.replace("{id}", id)
else:
    url = f"https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{id}%26installsource%3Dondemand%26uc"

# Send Request
try:
    request = requests.get(url, stream=True)
except requests.exceptions.MissingSchema:
    if verbose: print(f"{colored("[ ERROR ]", "red")} Schema missing. You probably want to use https.")
    sys.exit(1)
except requests.exceptions.InvalidSchema:
    if verbose: print(f"{colored("[ ERROR ]", "red")} Schema invalid. Did you mean to use https?")
    sys.exit(1)

# Error handling
if request.status_code != 200:
    print(f"{colored("[ ERROR ]", "red")} Hm. Couldn't find that extension.")
    sys.exit(1)

if verbose: print(f"{colored("[ INFO ]", "grey")} Extension found!")

# Writes the extension data to the file.
with open(of, 'wb') as f:
    print("Downloading...", end='')
    f.write(request.content)
    print("      Done!")
    f.close()