.\venv\Scripts\activate

python ./main.py set-placeholders -i -p




python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\Bed - Blue Wall - 1 Frame.jpg" -p "930,210,687,924"
python ./main.py set-placeholders -i "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies\Bed - 2 Frames.jpg" -p "624,145,340,479;1174,145,340,479"
python ./main.py add-images-to-mockups -m "\\GreenNas\Backup\Etsy\Mockups Template\3x4 - With Placeholders\Babies" -i "./photos/items" -o "./photos/output" -t "{counter:02d}-Mockup{counter}.jpg"

python ./main.py add-images-to-mockups -m mm -i ii -o oo -t tt
