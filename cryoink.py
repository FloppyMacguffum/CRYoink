# Modules
import sys
termcolor = True
vers = "1.0.4"
try:
    from termcolor import colored
except ModuleNotFoundError:
    print("[ ERROR ] Module termcolor not found. We recommend installing it for a better experience using CRYoink.")
    uin = input("Would you like to continue? [y/N]: ")
    if "y" in uin.lower(): termcolor = False
    else:
        import os
        return_code = os.system("pip install termcolor")
        if return_code != 0:
            print("[ ERROR ] Failed to install requests module. Quitting...")
            sys.exit(return_code)
        else:
            print("[ INFO ] Module termcolor was *probably* installed. Please reopen the app.")
            sys.exit(0)
try:
    import requests
except ModuleNotFoundError:
    print(f"{colored('[ ERROR ]', 'red')} requests module wasn't found!" if termcolor else "[ ERROR ] requests module wasn't found!")
    uin = input("Would you like to install it? [y/N]: ")
    if "y" in uin.lower():
        print("Installing requests module...")
        import os
        return_code = os.system("pip install requests")
        if return_code != 0:
            print(f"{colored('[ ERROR ]', 'red')} Failed to install requests module. Quitting..." if termcolor else "[ ERROR ] Failed to install requests module. Quitting...")
            sys.exit(return_code)
        else:
            print(f"{colored('[ INFO ]', 'grey')} Module requests was *probably* installed. Please reopen the app." if termcolor else "[ INFO ] Module requests was *probably* installed. Please reopen the app.")
            sys.exit(0)
    else:
        print(f"{colored('[ ERROR ]', 'red')} The requests module is required. Please install it and reopen the app." if termcolor else "[ ERROR ] The requests module is required. Please install it and reopen the app.")
        sys.exit(1)

# args variable for readability
args = sys.argv

# Verbose arg handling
if "-v" in args: verbose = True
else: verbose = False

if "-s" in args: supression = True
else: supression = False

if not supression and verbose:
    print(f"{colored('[ INFO ]', 'grey')} Running CRYoink version {vers}, updated on 12/24/24" if termcolor else f"[ INFO ] Running CRYoink version {vers}, updated on 12/24/24")

helpmessage = f"""CRYoink version {vers}

-h[elp] [ Shows this help message.                                     ]
-i[d]   [ The extension ID you would like to yoink.                    ]
-o[ut]  [ The file to be written into. e.x extension.crx.              ]
-O[D]   [ The directory to write the crx file into. e.x extensions/.   ]
-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary.  ]
-U      [ Extracts inside of crx into output directory or path ran in. ]
-v      [ Enables verbose mode. Prints debug statements like warnings  ]
-s      [ Disables/Supresses print statements.                         ]
-b      [ Lets you enter multiple extension IDs. Must be used at end.  ]
"""

# Help arg handling
if "-h" in args or "-help" in args or "--help" in args:
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
            print(f"{colored('[ WARNING ]', 'yellow')} ID not given. Using stdin instead..." if termcolor else "[ WARNING ] ID not given. Using stdin instead...")
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
        if verbose and not "-b" in args: print(f"{colored('[ INFO ]', 'grey')} Argument \"-o\" not found. Defaulting output file to \"extension.crx\"..." if termcolor else "[ INFO ] Argument \"-o\" not found. Defaulting output file to \"extension.crx\"...")
        elif "-b" in args: print(f"{colored('[ INFO ]', 'grey')} Argument \"-o\" not found. Defaulting output file to the extension ID..." if termcolor else "[ INFO ] Argument \"-o\" not found. Defaulting output file to the extension ID...")
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
                    print(f"{colored('[ ERROR ]', 'red')} Hm. Couldn't find extension {extension}." if termcolor else f"[ ERROR ] Hm. Couldn't find extension {extension}.")
                sys.exit(1)
            if verbose: print(f"{colored('[ INFO ]', 'grey')} Found extension {extension}." if termcolor else f"[ INFO ] Found extension {extension}.")
            with open(f"{extension}.crx", "wb") as f:
                if not supression: print("Downloading...", end='')
                f.write(request.content)
                if not supression: print("      Done!")
                f.close()
except requests.exceptions.MissingSchema:
    if not supression and verbose:
        print(f"{colored('[ ERROR ]', 'red')} Schema missing. You probably want to use https." if termcolor else "[ ERROR ] Schema missing. You probably want to use https.")
    sys.exit(1)
except requests.exceptions.InvalidSchema:
    if not supression and verbose:
        print(f"{colored('[ ERROR ]', 'red')} Schema invalid. Did you mean to use https?" if termcolor else "[ ERROR ] Schema invalid. Did you mean to use https?")
    sys.exit(1)

# Error handling
if request.status_code != 200:
    if not supression:
        print(f"{colored('[ ERROR ]', 'red')} Hm. Couldn't find that extension." if termcolor else "[ ERROR ] Hm. Couldn't find that extension.")
    sys.exit(1)

if not supression and verbose:
    print(f"{colored('[ INFO ]', 'grey')} Extension found!" if termcolor else "[ INFO ] Extension found!")

# Writes the extension data to the file.
if not "-b" in args:
    if not "-U" in args:
        with open(of, 'wb') as f:
            if not supression: print("Downloading...", end='')
            f.write(request.content)
            if not supression: print("      Done!")
            f.close()
    else:
        print("unfinished... D:")
