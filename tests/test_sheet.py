from PIL import Image, ImageDraw


def create_contact_sheet(photos, cols=5, thumbnail_size=(200, 200), padding=10, background_color=(255, 255, 255)):
    num_photos = len(photos)
    rows = (num_photos + cols - 1) // cols

    # Calculate the size of the contact sheet
    sheet_width = cols * (thumbnail_size[0] + padding) - padding
    sheet_height = rows * (thumbnail_size[1] + padding) - padding

    # Create a new blank image for the contact sheet
    contact_sheet = Image.new('RGB', (sheet_width, sheet_height), background_color)

    # Create a draw object to draw thumbnails onto the contact sheet
    draw = ImageDraw.Draw(contact_sheet)

    # Iterate over the photos and paste them onto the contact sheet
    for i, photo in enumerate(photos):
        # Open the photo and resize it to the thumbnail size
        image = Image.open(photo)
        image.thumbnail(thumbnail_size)

        # Calculate the position to paste the thumbnail onto the contact sheet
        row = i // cols
        col = i % cols
        x = col * (thumbnail_size[0] + padding)
        y = row * (thumbnail_size[1] + padding)

        # Paste the thumbnail onto the contact sheet
        contact_sheet.paste(image, (x, y))

        # Draw a rectangle around the thumbnail
        draw.rectangle([(x, y), (x + thumbnail_size[0], y + thumbnail_size[1])], outline=(0, 0, 0))
        contact_sheet.save('../photos/output/contact.png')

    return contact_sheet


photos = ['../photos/items/WB-Piano.jpg', '../photos/items/WB-Sax.jpg']
contact_sheet = create_contact_sheet(photos, cols=3)
