from PIL import Image


def add_description(image_path, description):
    image = Image.open(image_path)

    XPComment = 0x9C9C
    # XPKeywords = 0x9C9E
    exifdata = image.getexif()
    exifdata[XPComment] = description.encode("utf16")
    # exifdata[XPKeywords] = "new keyword;".encode("utf16")

    image.save(image_path, exif=exifdata)


def get_comment(image_page):
    image = Image.open(image_page)

    XPComment = 0x9C9C

    exifdata = image.getexif()

    return exifdata[XPComment].decode('utf16')

add_description('./photos/template.jpg', 'New desk')
print(get_comment('./photos/template.jpg'))