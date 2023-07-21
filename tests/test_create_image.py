from PIL import Image

img = Image.new("RGB", (800, 1280), (255, 255, 255))
p = Image.open('../photos/items/4/1/WB-Drum.jpg')
p=p.resize((10,10))
img.paste(p)
img.save("./image.png", "PNG")