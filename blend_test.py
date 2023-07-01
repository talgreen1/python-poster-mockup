from PIL import Image
import numpy
from blend_modes import soft_light

# Import background image
background_img_raw = Image.open('./photos/template.rgba')  # RGBA image
# background_img_raw.putalpha(1)
background_img = numpy.array(background_img_raw)  # Inputs to blend_modes need to be numpy arrays.

background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.


# Import foreground image
foreground_img_raw = Image.open('./photos/item1.png') # RGBA image
foreground_img = numpy.array(foreground_img_raw)  # Inputs to blend_modes need to be numpy arrays.
foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.

# Blend images
opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
blended_img_float = soft_light(background_img_float, foreground_img_float, opacity)

# Convert blended image back into PIL image
blended_img = numpy.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
blended_img_raw = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
# This behavior is difficult to change (although possible).
# If you have alpha channels in your images, then you should give
# OpenCV a try.

# Display blended image
blended_img_raw.show()

# # import OpenCV
# import cv2  # import OpenCV
# import numpy
# from blend_modes import soft_light
#
# # Import background image
# background_img_float = cv2.imread('./photos/template.jpg',-1).astype(float)
#
# # Import foreground image
# foreground_img_float = cv2.imread('./photos/item1.png',-1).astype(float)
#
# # Blend images
# opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
# blended_img_float = soft_light(background_img_float, foreground_img_float, opacity)
#
# # Display blended image
# blended_img_uint8 = blended_img_float.astype(numpy.uint8)  # Convert image to OpenCV native display format
# cv2.imshow('window', blended_img_uint8)
# cv2.waitKey()  # Press a key to close window with the image.
