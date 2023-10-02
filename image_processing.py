import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import convolve

# ## 2. Opening and reading the file as an array
file_path = "C:/Users/deepe/Downloads/"  # Edit file path
img_array = mpimg.imread(file_path + "input_img.png") # Edit file name

print ("The M x N x 3 array is as follows:")
print(img_array)

plt.imshow(img_array, cmap='gray') # Uncomment to verify if it displays correctly
plt.show()

## 3. Converting the file to grayscale
# Each pixel contains a value each for R, G and B channels
# There are M rows and N columns of pixels
# Hence the array is M x N x 3. To convert it to an M x N matrix we take the average of R, G and B values for each pixel
gray_img = np.mean(img_array, axis=2) # Averaging
print(gray_img)

plt.imshow(gray_img, cmap='gray') # Uncomment to verify if it displays correctly
plt.show()


# Define a blur kernel (3x3 Gaussian blur kernel)
blur_kernel = np.array([[1, 2, 2],[2, 4, 2],[1, 2, 1]], dtype=float)
sharp_kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], dtype=float)
identity_kernel = np.array([[0, 0, 0],[0, 1, 0],[0, 0, 0]], dtype=float)
emboss_kernel = np.array([[-2, 1, 0],[-1, 1, 1],[0, 1, 2]], dtype=float)

# Normalize the kernel
blur_kernel /= np.sum(blur_kernel)
sharp_kernel/= np.sum(sharp_kernel)
identity_kernel/= np.sum(sharp_kernel)
emboss_kernel/= np.sum(emboss_kernel)

# Convert the kernel to a 3D array
blur_kernel = blur_kernel[:, :, np.newaxis]
sharp_kernel= sharp_kernel[:, :, np.newaxis]
identity_kernel= identity_kernel[:, :, np.newaxis]
emboss_kernel= emboss_kernel[:, :, np.newaxis]

# Apply the convolution operation to blur the image
blurred_img = convolve(img_array, blur_kernel)
sharped_img = convolve(img_array, sharp_kernel)
identity_img = convolve(img_array, identity_kernel)
emboss_img = convolve(img_array, emboss_kernel)

# Display the blurred image
plt.subplot(223)
plt.imshow(blurred_img, cmap='gray')
plt.title('Blurred Image')
plt.show()

# Display the sharped image
plt.subplot(121)
plt.imshow(sharped_img, cmap='gray')
plt.title('Sharped Image')
plt.show()

# Display the Indentity image
plt.subplot(121)
plt.imshow(identity_img, cmap='gray')
plt.title('Indentity Image')
plt.show()

# Display the sharped image
plt.subplot(121)
plt.imshow(emboss_img, cmap='gray')
plt.title('Emboss Image')
plt.show()




## 4. Saving the grayscale image as a CSV file
np.savetxt(file_path+"img_matrix.csv", gray_img, delimiter=",")

### *** ~~~ *** ###

## 5. Reading the processed (after convolution) CSV file as an array
# UNCOMMENT AS NEEDED

processed_img = np.genfromtxt(file_path + "processed_img_matrix.csv", delimiter=",")
print(processed_img)

# ## 6. Displaying processed matrix as an image

plt.imshow(processed_img, cmap="gray")
plt.show()

# ## 7. Saving the processed image into a file

mpimg.imsave(file_path+"processed_img.png", processed_img, cmap="gray")