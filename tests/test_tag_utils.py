# from PIL import ImageChops
# from PIL import Image, ExifTags
# from PIL.ExifTags import TAGS
# import piexif
from exif import Image

# https://pypi.org/project/exif/

my_image = Image('./photos/test_template.jpg')
# my_image.make = "Python1"
# my_image.tal = 'Tal'
my_image.set("tal", "xp_comment")

my_image.xp_comment = "My Comment"


with open('./photos/test_template1.jpg', 'wb') as new_image_file:
    new_image_file.write(my_image.get_file())



print(my_image.make)

#
# def extract_tag(image_path: str):
#     image = Image.open(image_path)
#     info_dict = {
#         "Filename": image.filename,
#         "Image Size": image.size,
#         "Image Height": image.height,
#         "Image Width": image.width,
#         "Image Format": image.format,
#         "Image Mode": image.mode,
#         "Image is Animated": getattr(image, "is_animated", False),
#         "Frames in Image": getattr(image, "n_frames", 1)
#     }
#
#     for label, value in info_dict.items():
#         print(f"{label:25}: {value}")
#
#     exifdata = image.getexif()
#
#     for tag_id in exifdata:
#         # get the tag name, instead of human unreadable tag id
#         tag = TAGS.get(tag_id, tag_id)
#         data = exifdata.get(tag_id)
#         # decode bytes
#         if isinstance(data, bytes):
#             data = data.decode()
#         print(f"{tag:25}: {data}")
#
#
#
#
# def save_tags(image_path: str):
#     metadata = {
#         'Author': 'John Doe',
#         'Description': 'A beautiful landscape',
#         'Location': 'New York'
#     }
#
#     image = Image.open(image_path)
#     image.info.update(metadata)
#
#     # Save the image with metadata
#     image.save(image_path)
#     pass
#
# # save_tags('./photos/test_template.jpg')
# # extract_tag('./photos/test_template.jpg')
#
#
# def write_metadata_to_jpg(image_path, metadata):
#     exif_dict = piexif.load(image_path)
#
#     # Convert metadata to EXIF format
#     exif_bytes = piexif.dump({"Exif": metadata})
#
#     # Update the EXIF data in the image
#     piexif.insert(exif_bytes, image_path)
#
# # Usage example:
# jpg_file = './photos/test_template.jpg'
# metadata = {
#     piexif.ExifIFD.UserComment: "This is a comment.",
#     piexif.ImageIFD.Make: "Camera Manufacturer",
#     piexif.ImageIFD.Model: "Camera Model",
#     piexif.ImageIFD.Software: "Image Editing Software"
# }
#
# write_metadata_to_jpg(jpg_file, metadata)