
def MeanRGB(image, colorChannel):
  if colorChannel == 'R':
    c = 0
  elif colorChannel == 'G':
    c = 1
  elif colorChannel == 'B':
    c = 2
  width = image.size[0]
  height = image.size[1]
  sum = 0
  for i in range(0, height):  # loop through height
    for j in range(0, width):  # loop through width
      color = image.getpixel((j, i))
      sum = sum + color[c]
  mean = sum / (height * width)  # mean
  print("mean : ",mean)
  return mean
