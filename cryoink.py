# Modules
import sys
import requests
from termcolor import colored

# args variable for readability
args = sys.argv

# Verbose arg handling
if "-v" in args: verbose = True
else: verbose = False

if "-s" in args: supression = True
else: supression = False

if not supression and verbose: 
    print(f"{colored('[ INFO ]', 'grey')} Running CRYoink version 1.0.2, updated on 7/28/24")

helpmessage = """CRYoink version 1.0.2

-h[elp] [ Shows this help message.                                    ]
-i[d]   [ The extension ID you would like to yoink.                   ]
-o[ut]  [ The file to be written into. e.x extension.crx.             ]
-O[D]   [ The directory to write the crx file into. e.x extensions/.  ]
-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary. ]
-v      [ Enables verbose mode. Prints debug statements like warnings ]
-s      [ Disables/Supresses print statements.                        ]
-b      [ Lets you enter multiple extension IDs. Must be used at end. ]
"""

# Help arg handling
if "-h" in args:
    if not supression:
        print(helpmessage)
        sys.exit(0)
    else:
        sys.exit(1)
elif "-help" in args:
    if not supression:
        print(helpmessage)
        sys.exit(0)
    else:
        sys.exit(1)
elif "--help" in args:
    if not supression:
        print(helpmessage)
        sys.exit(0)
    else:
        sys.exit(1)

# ID arg handling
if "-i" in args:
    id = args[args.index("-i")+1]
elif "-id" in args:
    id = args[args.index("-id")+1]
elif "--id" in args:
    id = args[args.index("--id")+1]
else:
    if not "-b":
        if not supression: 
            print(f"{colored('[ WARNING ]', 'yellow')} ID not given. Using stdin instead...")
            id = input("Enter ID: ")
        else:
            sys.exit(1)

# Output arg handling
if "-o" in args:
    of = args[args.index("-o")+1]
elif "-out" in args:
    of = args[args.index("-out")+1]
elif "--out" in args:
    of = args[args.index("--out")+1]
else:
    if not supression:
        if verbose and not "-b" in args: print(f"{colored('[ INFO ]', 'grey')} Argument \"-o\" not found. Defaulting output file to \"extension.crx\"...")
        elif "-b" in args: print(f"{colored('[ INFO ]', 'grey')} Argument \"-o\" not found. Defaulting output file to the extension ID...")
    of = "extension.crx"

if "-u" in args:
    url = args[args.index("-u")+1]
    url.replace("{id}", id)
    url.replace("\"", "")
elif "-url" in args:
    url = args[args.index("-url")+1]
    url.replace("{id}", id)
    url.replace("\"", "")
elif "--url" in args:
    url = args[args.index("--url")+1]
    url.replace("{id}", id)
    url.replace("\"", "")
else:
    url = f"https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{id}%26installsource%3Dondemand%26uc"

# Send Request
try:
    if not "-b" in args:
        request = requests.get(url, stream=True)
    else:
        batch_index = args.index("-b")
        extensions = args[batch_index+1:]
        for extension in extensions:
            request = requests.get(f"https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{extension}%26installsource%3Dondemand%26uc", stream=True)
            if request.status_code != 200:
                if not supression:
                    print(f"{colored('[ ERROR ]', 'red')} Hm. Couldn't find extension {extension}.")
                sys.exit(1)
            else:
                if verbose:
                    print(f"{colored('[ INFO ]', 'grey')} Found extension {extension}.")
                    with open(f"{extension}.crx", "wb") as f:
                        if not supression: print("Downloading...", end='')
                        f.write(request.content)
                        if not supression: print("      Done!")
                        f.close()
except requests.exceptions.MissingSchema:
    if not supression:
        if verbose: print(f"{colored('[ ERROR ]', 'red')} Schema missing. You probably want to use https.")
    sys.exit(1)
except requests.exceptions.InvalidSchema:
    if not supression:
        if verbose: print(f"{colored('[ ERROR ]', 'red')} Schema invalid. Did you mean to use https?")
    sys.exit(1)

# Error handling
if request.status_code != 200:
    if not supression:
        print(f"{colored('[ ERROR ]', 'red')} Hm. Couldn't find that extension.")
    sys.exit(1)

if not supression and verbose:
    if verbose: print(f"{colored('[ INFO ]', 'grey')} Extension found!")

# Writes the extension data to the file.
if not "-b" in args:
    with open(of, 'wb') as f:
        if not supression: print("Downloading...", end='')
        f.write(request.content)
        if not supression: print("      Done!")
        f.close()