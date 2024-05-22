# Modules
import sys
import requests

# args variable for readability
args = sys.argv

# Help arg handling
if "-h" in args:
    print("CRYoink version 1.0.0")
    print()
    print("-h[elp] [ Shows this help message.                       ]")
    print("-i[d]   [ The extension ID you would like to yoink.      ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx ]")
    sys.exit(0)
elif "-help" in args:
    print("CRYoink version 1.0.0")
    print()
    print("-h[elp] [ Shows this help message.                       ]")
    print("-i[d]   [ The extension ID you would like to yoink.      ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx ]")
    sys.exit(0)
elif "--help" in args:
    print("CRYoink version 1.0.0")
    print()
    print("-h[elp] [ Shows this help message.                       ]")
    print("-i[d]   [ The extension ID you would like to yoink.      ]")
    print("-o[ut]  [ The file to be written into. e.x extension.crx ]")
    sys.exit(0)

# ID arg handling
if "-i" in args:
    id = args[args.index("-i")+1]
elif "-id" in args:
    id = args[args.index("-id")+1]
elif "--id" in args:
    id = args[args.index("--id")+1]
else:
    id = input("Enter ID: ")

# Output arg handling
if "-o" in args:
    of = args[args.index("-o")+1]
if "-out" in args:
    of = args[args.index("-out")+1]
if "--out" in args:
    of = args[args.index("--out")+1]
else:
    of = "extension.crx"

# URL Variable
url = f"https://clients2.google.com/service/update2/crx?response=redirect&os=linux&arch=x64&os_arch=x86_64&nacl_arch=x86-64&prod=chromium&prodchannel=unknown&prodversion=91.0.4442.4&lang=en-US&acceptformat=crx2,crx3&x=id%3D{id}%26installsource%3Dondemand%26uc"

# Send Request
request = requests.get(url, stream=True)

# Error handling
if request.status_code != 200:
    print("Hm. Couldn't find that extension.")
    sys.exit(1)

print("Extension found!")

# Writes the extension data to the file.
with open(of, 'wb') as f:
    print("Downloading...", end='')
    f.write(request.content)
    print("      Done!")
    f.close()