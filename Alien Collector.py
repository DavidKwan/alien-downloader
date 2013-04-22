# coded in python

"""Reddit Alien Banner Downloader
This is a simple script to download the alien image banner for a given subreddit
url to a local directory called 'images'. To use it, call the function 
download_alien with the parameter as a string containing the URL.
For example, calling download_alien("http://www.reddit.com/") creates a folder
called 'images' in the directory where this file is (if it is not already
there). The folder will contain the image of the alien banner on the reddit
homepage.

Author: David Kwan
Produced for: FlyerFlo
"""

from urllib2 import urlopen
from bs4 import BeautifulSoup
import urllib
import os


## get_image_url: str -> str
## Purpose: consumes a URL string, subreddit_url, and searches it's html
## document for the html line containing the subreddit banner image.
## Returns the URL of the image.
#  Example: get_image_url("http://www.reddit.com/r/politics/") returns
#  "http://c.thumbs.redditmedia.com/RI-za15l9NVMVtlz.png", which is a link to
#  the banner.
def get_image_url (subreddit_url):
    html = urlopen(subreddit_url).read()
    soup = BeautifulSoup(html, "lxml")
    alien = soup.find(id = "header-img")
    alien_url = alien['src']
    return alien_url

## save_image: str -> None
## Purpose: consumes a URL string, img_url, and saves the image associated
## with the URL to a local folder called "images"
#  Example: save_image("http://c.thumbs.redditmedia.com/RI-za15l9NVMVtlz.png") 
#  produces None, and the image associated with the URL will be in the folder
#  "images" where this program was saved.
def save_image (img_url):
    d = os.path.dirname("images")
    if not os.path.exists("images"):
        os.makedirs("images")
        
    start = index_highest(img_url, '/')
    urllib.urlretrieve(img_url, "images/%s" %(img_url[start+1:]))

## download_alien str -> None
## Purpose: uses both the save_image and get_image_url functions to consume the
## subreddit URL and save its associated alien image banner to a local folder.
#  Example: download_alien ("http://www.reddit.com/r/uwaterloo/") saves the UW-
#  themed alien image to a local folder called "images".
def download_alien (reddit_URL):
    try:
        save_image(get_image_url (reddit_URL))
    except:
        print "Error: URL does not have an alien image banner to download."
        print "If the URL is indeed a subreddit URL, please try again as the \
server may have had too much traffic."

## index_highest: str str[len = 1] -> num[>=0]
## Purpose: consumes a string and a character to look for in the string.
## Returns the latest index of the character in the string. Returns -1 if not
## found. The motivation for this function was that the index() method only
## returns the earliest index.
#  Example: index_highest ('http://c.thumbs.redditmedia.com/ckbE4tDmf6xcPaVz.png',
#  '/') returns 31, since it is the index of the latest occurence of '/' in 
#  the given string.
def index_highest (string, char):
    index = 0
    file_start = -1
    while index < len(string):
        if string[index] == char:
            file_start = index
        index += 1
    return file_start
