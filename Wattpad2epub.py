#! /usr/bin/python3
"""
# Python Script to Scrape Wattpad Story and convert to Epub and html file.
# By Architrixs, Created Nov 5, 2020.
# This program will create:
# 1. A html file of the entire Wattpad Book AND (You can directly Use this one to read, Images are preserved in this format.)
# 2. A Epub file of the entire Wattpad Book.(The Epub will have separate marked Chapters instead of all chapters as one whole.)

HOW TO USE :
1. Just copy the URL of any Chapter of the Wattpad Book. I repeat copy URL of any "Chapter"... you got it!
2. Either Directly Run 
	>>Wattpad2epub.py
   or	>>Wattpad2epub.py Story_url
   
   Yes it can take 1 Commandline Argument as the copied url of the Chapter.
3. You got html and epub saved in the same location.
"""
import bs4, sys, requests, pyperclip, re, pypandoc, string

if len(sys.argv) > 1:
	#getting address from command line.
	address = ''.join(sys.argv[1:])
else:
	#getting address from clipboard.
	address = pyperclip.paste()

#Using regex to get ID
search_id = re.compile(r'\d{9,}')
id_no = search_id.search(address)

#getting json data from Wattpad api

res = requests.get("https://www.wattpad.com/apiv2/info?id=" + id_no.group(), headers={'User-Agent': 'Mozilla/5.0'})

#Checking for Bad download
try:
	res.raise_for_status()
except Exception as exc:
	print("There was a problem: %s" % (exc))

#extracting Useful data
summary = res.json()['description']
tags = res.json()['tags']
chapters = res.json()['group']
name = res.json()['url']
author = res.json()['author']

#Using regex to get Name
search_name = re.compile(r"[\w]+['][\w]+|\w+")
name= requests.utils.unquote(name)
name = search_name.findall(name)
story_name = string.capwords(' '.join(name[2:]))


#Opening/Creating HTML file
file = open(story_name+".html", 'w')
file.write("<html><head></head><body>")

file.write("<br><h1>" + story_name +"</h1><br>BY  <h4>"+author+"</h4><br><b>Tags:</b> "+tags+"<br><br>"+summary+"<br>")
file.write("<br><br><div align='left'><h6>* If chapter number or names are Jumbled up, its definetely author's fault.(Author-san please Number them correctly and in order.)<br>* Converted using Wattpad2epub By Architrixs<br></h6></div>")

#Looping through each chapter
for i in range(len(chapters)):
	#getting the chapters using the ID
	print("Getting Chapter", i+1, "....")
	story = requests.get("https://www.wattpad.com/apiv2/storytext?id=" + str(chapters[i]['ID']), headers={'User-Agent': 'Mozilla/5.0'})

	try:
		story.raise_for_status()
	except Exception as exc:
		print("There was a problem: %s" % (exc))
	
	#Creating soup
	soup_res = bs4.BeautifulSoup(story.text, 'html.parser')
	contents = soup_res.find_all('p')
	
	#Adding Content of chapters to the file
	file.write("<br><br><h2>Chapter "+str(i+1)+" : '"+ chapters[i]['TITLE'] +"'</h2><br><br>")
	file.write(soup_res.prettify())

file.write("</body></html>")

#closing the file
file.close()

#Output
print("saved "+ story_name+".html")
print("Generating Epub...")

#Using Pypandoc to convert html to epub
output = pypandoc.convert_file(story_name+".html", 'epub3', outputfile=story_name+".epub", extra_args=['--epub-chapter-level=2'])
assert output == ""
print("saved "+ story_name+".epub")
