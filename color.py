from collections import Counter

def MostUsedColor(image):
  #Convert the image to RGB format
  rgb_im = image.convert('RGB')
  width, height = image.size  
  colors = []
  
  #Iterate through the pixels in the image
  for i in range(width):
      for j in range(height):
          # Get the RGB values for the pixel
          r, g, b = rgb_im.getpixel((i, j))
          colors.append((r, g, b))
  
  #Count the occurrences of each color in the list
  color_counts = Counter(colors)
  
  #Get the most common color
  most_common_color = color_counts.most_common(1)
  #Avoid the last value, we only want the rgb values
  rgb = most_common_color[0][0][:3]
  print(rgb)
  return rgb