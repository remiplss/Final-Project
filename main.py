# importing the modules
import requests
from bs4 import BeautifulSoup
  
# providing url
url = 'https://www.wikiart.org/en/claude-monet'
  
# creating request object
req = requests.get(url)
  
# creating soup object
data = BeautifulSoup(req.text, 'lxml')
  
# finding all li tags in ul and printing the text within it
images = data.find_all('img')
#delete irrelevant images
images = images[3:]
images = images[:10]
#get the url
for i in range( len(images)):
  images[i] = images[i]['img-source']

#cleaning the url
url_images = [sub.replace('!PinterestSmall.jpg', '') for sub in images]
url_images = [sub.replace('\'', '') for sub in images]
#list of images name
listName=["image0","image1","image2","image3","image4","image5","image6","image7","image8","image9"]
i=0
#dowload al the images
for url in url_images:
  response = requests.get(url)
  if response.status_code:
    fp = open(listName[i]+".jpg", 'wb')
    fp.write(response.content)
    fp.close()
    i = i+1