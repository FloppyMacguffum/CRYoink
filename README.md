# CRYoink
## What is this?
CRYoink is a chrome extension installer. If it's on the chrome web store, you can insert the ID into this, and download the .crx file.
## How do I use this? 
You can run it normally, just like some other python app. However, it also has some argument handling.
```
-h[elp] [ Shows this help message.                       ]
-i[d]   [ The extension ID you would like to yoink.      ]
-o[ut]  [ The file to be written into. e.x extension.crx ]
```
### Examples
```
$ python cryoink.py -i <insert chrome extension ID here>

Extension found!
Downloading...      Done!

$ ls
cryoink.py
extension.crx <-- what just got downloaded!
```