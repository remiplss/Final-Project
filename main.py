# importing the modules
import requests
from bs4 import BeautifulSoup
import glob
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# Utilize this library for visualization.
import seaborn as sns
import pandas as pd

from palette import Palette
from color import MostUsedColor

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
for i in range(len(images)):
  images[i] = images[i]['img-source']

#cleaning the url
url_images = [sub.replace('!PinterestSmall.jpg', '') for sub in images]
url_images = [sub.replace('\'', '') for sub in images]
#list of images name
listName = [
  "image0", "image1", "image2", "image3", "image4", "image5", "image6",
  "image7", "image8", "image9"
]
i = 0
#dowload al the images
for url in url_images:
  response = requests.get(url)
  if response.status_code:
    fp = open(listName[i] + ".jpg", 'wb')
    fp.write(response.content)
    fp.close()
    i = i + 1

#create list of images
i = 0
list_images = []
most_used_colors = []
for filename in glob.glob('images/*'):
  im = Image.open(filename)
  list_images.append(im)
  #color palette of the artist
  df = Palette(im)
  #most used color by the artist
  most_used_colors.append(MostUsedColor(im))
  im.close()

#identify the most used colors on the different paintings

# Create a 2D array of shape (1, len(input), 3)
color_array = np.zeros((1, len(most_used_colors), 3))

# Fill the array with the RGB values of the colors
for i in range(len(most_used_colors)):
  color_array[0, i, :] = most_used_colors[i]

# Use the imshow function to display the different colors
fig, axs = plt.subplots()
plt.imshow((color_array * 255).astype(np.uint8))
plt.title("Most used color in all the paintings")
sns.pairplot(df, diag_kind='hist', markers='.', height=4, aspect=1)
plt.show()
