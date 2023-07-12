.\venv\Scripts\activate

python ./main.py set-placeholders -i -p




python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\Bed - Blue Wall - 1 Frame.jpg" -p "930,210,687,924"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\Bed - 2 Frames.jpg" -p "624,145,340,479;1174,145,340,479"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\Bed - 1 Frames.jpg" -p "840,120,442,625"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\vecteezy_empty-frame-mockup-frame-poster-in-the-children-s_9837073_713.jpg" -p "762,134,477,595"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\vecteezy_mockup-frame-poster-in-the-children-s-room-bedroom-interior__740.jpg" -p "1575,622,848,1138"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\vecteezy_mock-up-poster-frame-in-children-room-kids-room-nursery-mockup__653.jpg" -p "545,391,328,442;955,391,328,442;1366,391,328,442"

python ./main.py add-images-to-mockups -m "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg"  -mocks-not-rec
python ./main.py add-images-to-mockups -m "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\t" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg"
python ./main.py add-images-to-mockups -m "./photos/mocks" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg" --exact-num-of-placeholders "1,2,1"
                 add-images-to-mockups -m "./photos/mocks" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg" -epn "2,1,1"
                 add-images-to-mockups -m "./photos/mocks" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg" -pn "2,1"



python ./main.py add-images-to-mockups -m mm -i ii -o oo -t tt


Contact sheets:
https://github.com/cobanov/contact-sheet



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

    return contact_sheet


photos = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg']
contact_sheet = create_contact_sheet(photos, cols=3)

# Save the contact sheet to a file
contact_sheet.save('contact_sheet.jpg')

