import pandas as pd
import numpy as np

def Palette(image):
# print the nested list or tuples to ther user
  image_data = np.array(image)
  R, G, B = image_data[:,:,0].flatten(), image_data[:,:,1].flatten(), image_data[:,:,2].flatten()
  # Create a DataFrame from the R, G, B channels
  df = pd.DataFrame({'R': R, 'G': G, 'B': B})
  return df