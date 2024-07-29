# CRYoink
## What is this?
CRYoink is a chrome extension installer. If it's on the chrome web store, you can insert the ID into this, and download the .crx file.
## How do I use this? 
You can run it normally, just like some other python app. However, it also has some argument handling.
```
-h[elp] [ Shows the help message.                                    ]
-i[d]   [ The extension ID you would like to yoink.                   ]
-o[ut]  [ The file to be written into. e.x extension.crx.             ]
-O[D]   [ The directory to write the crx file into. e.x extensions/.  ]
-u[rl]  [ Select a URL to be used. Insert {id} where ID is necessary. ]
-v      [ Enables verbose mode. Prints debug statements like warnings ]
-s      [ Disables/Supresses print statements.                        ]
-b      [ Lets you enter multiple extension IDs. Must be used at end. ]
```
### Examples
```
$ python cryoink.py -i <insert chrome extension ID here>

Extension found!
Downloading...      Done!

$ ls
cryoink.py
extension.crx <-- what just got downloaded!

$ python cryoink.py -s -i <insert chrome extension ID here>

$ ls
cryoink.py
extension.crx <-- what just got downloaded!

$ python cryoink.py -v -O extensions -i <insert chrome extension ID here>
[ INFO ] CRYoink version 1.0.2, updated on 7/28/24
[ INFO ] Argument "-o" not found. Defaulting to extension.crx...
[ INFO ] Extension found!
Downloading...      Done!

$ ls
cryoink.py
extensions/extension.crx <-- what just got downloaded!

$ python cryoink.py -b <extension id #1> <extension id #2> <extension id #3> <extension id #4>

Downloading...      Done!
Downloading...      Done!
Downloading...      Done!
Downloading...      Done!

$ ls
cryoink.py
<extension id #1>
<extension id #2>
<extension id #3>
<extension id #4>
```