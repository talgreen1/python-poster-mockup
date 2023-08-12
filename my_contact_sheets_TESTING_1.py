from PIL import Image, ImageFilter

# Parameters
output_size = 800  # Adjust as needed
x, y = 50, 50      # Paste position


img = Image.open('D:\Dropbox\My Documents\github\python-poster-mockup\photos\small.png')


# shadow_size = (img.width + 10, img.height + 10)  # Adjust shadow size as needed
shadow_size = (img.width, img.height)  # Adjust shadow size as needed
shadow_color = (0, 0, 0, 100)  # RGBA color for the shadow (adjust alpha for intensity)
shadow = Image.new('RGBA', shadow_size, shadow_color)

contact_sheet = Image.new('RGBA', (output_size, output_size), (255, 255, 255))

contact_sheet.paste(shadow, (x + 15, y + 15))  # Adjust shadow offset as needed




blurred_shadow = contact_sheet.filter(ImageFilter.GaussianBlur(10))
contact_sheet = Image.new('RGBA', (output_size, output_size), (255, 255, 255))

contact_sheet = Image.alpha_composite(contact_sheet, blurred_shadow)

contact_sheet.paste(img, (x,y))





# Display or save the contact sheet
contact_sheet.show()
# contact_sheet.save('output_contact_sheet.png')  # Save the contact sheet as an image file
