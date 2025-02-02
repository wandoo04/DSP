import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Input file path
input_file = 'F:/MSC IT/Practical/DS/prac3/content/d.jpg'

# Read the image
image = cv.imread(input_file, cv.IMREAD_COLOR)

# Get image dimensions
height, width, channels = image.shape
print(f'Image Dimensions: {height}x{width}, Channels: {channels}')

# Flatten the image and create DataFrame
flattened_data = image.flatten()
columns = ['XAxis', 'YAxis', 'Red', 'Green', 'Blue']
x = flattened_data.shape[0] // (channels + 2)
image_data = pd.DataFrame(np.reshape(flattened_data, (x, channels + 2)), columns=columns)

# Plot the image
plt.imshow(image)
plt.show()

# Output file path
output_file = 'F:/MSC IT/Practical/DS/prac3/content/d1.csv'
image_data.to_csv(output_file, index=False)

print("Image data saved to CSV - Done")
