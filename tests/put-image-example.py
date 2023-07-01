from PIL import ImageChops
from PIL import Image


def resize_and_insert_image(background_image_path, insert_image_path, output_image_path, new_size, insert_position,
                            blend_mode):
    # Open the background image
    # background_image = Image.open('./template1.jpg')
    background_image = Image.open(background_image_path)

    # Resize the insert image
    # insert_image = Image.open('./item1.png')
    insert_image = Image.open(insert_image_path)

    insert_image = insert_image.resize(new_size)

    # Create a copy of the insert image with alpha channel for transparency
    insert_image_alpha = insert_image.convert("RGBA")

    # Apply the specified blending mode
    # if blend_mode == "dissolve":
    #     # Dissolve blending mode
    #     blended_image = ImageChops.dissolve(background_image, insert_image_alpha, 0.5)
    # elif blend_mode == "transparent":
    #     # Transparent blending mode
    #     blended_image = Image.alpha_composite(background_image, insert_image_alpha)
    # else:
        # Default blending mode: normal
    # blended_image = Image.alpha_composite(background_image, insert_image_alpha)

    # Paste the blended image onto the background image at the specified position
    background_image.paste(insert_image, insert_position)

    # Save the resulting image
    background_image.save(output_image_path)


# Example usage
background_image_path = '../photos/template.jpg'  # Path to the background image
insert_image_path = '../photos/item1.png'  # Path to the image to be inserted (with alpha channel)
output_image_path = '../photos/output.jpg'  # Path to save the resulting image
new_size = (200, 200)  # New size for the insert image
insert_position = (100, 100)  # Coordinates to paste the smaller image
blend_mode = "dissolve"  # Specify the desired blending mode ("dissolve", "transparent", or "normal")

resize_and_insert_image(background_image_path, insert_image_path, output_image_path, new_size, insert_position,
                        blend_mode)
