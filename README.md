# Wattpad2Epub
### By Architrixs, created Nov 5, 2020.
Python Script to Scrape Wattpad Story and convert to Epub and html file.
### This program will create:
1. A html file of the entire Wattpad Book AND (You can directly Use this one to read, Images are preserved in this format.)
2. A Epub file of the entire Wattpad Book.(The Epub will have separate marked Chapters instead of all chapters as one whole. *Images included*.)

### Libraries used : 
1. Pyperclip
2. Requests 
3. BeautifulSoup4 
4. re
5. Pypandoc
6. String

### Note: Pypandoc uses pandoc, so it needs an available installation of pandoc.
### Installing pandoc via pypandoc
Installing via pypandoc is possible on Windows, Mac OS X or Linux (Intel-based, 64-bit):
```
# expects an installed pypandoc: pip install pypandoc
from pypandoc.pandoc_download import download_pandoc
# see the documentation how to customize the installation path
# but be aware that you then need to include it in the `PATH`
download_pandoc()
```
The default install location is included in the search path for pandoc, so you don't need to add it to the PATH.

### HOW TO USE :
1. Just copy the URL of any Chapter of the Wattpad Book. I repeat copy URL of any "Chapter"... you got it!
2. Either Directly Run

        Wattpad2epub.py
        or
        Wattpad2epub.py Story_url     #Pyperclip library not needed for this.
   
   Yes, it can take 1 Commandline Argument as the copied url of the Chapter.
3. You got html and epub saved in the same location.

![Image of Wattpad2Epub](https://github.com/Architrixs/Wattpad2Epub/blob/main/Image_wattpad2Epub.png)
![Image of Wattpad2epub Windows](https://github.com/Architrixs/Wattpad2Epub/blob/main/wattpad2epub-windows.JPG)

### I found my script easy to use, but feel free to point out mistakes. I'm new to this.
