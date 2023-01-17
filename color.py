from collections import Counter

def MostUsedColor(image):
  # Convert the image to RGB format
  rgb_im = image.convert('RGB')
  
  # Get the width and height of the image
  width, height = image.size
  
  # Initialize an empty list to store the colors
  colors = []
  
  # Iterate through the pixels in the image
  for x in range(width):
      for y in range(height):
          # Get the RGB values for the pixel
          r, g, b = rgb_im.getpixel((x, y))
          # Add the color to the list
          colors.append((r, g, b))
  
  # Count the occurrences of each color in the list
  color_counts = Counter(colors)
  
  # Get the most common color
  most_common_color = color_counts.most_common(1)
  rgb = most_common_color[0][0][:3]
  print(rgb)
  return rgb