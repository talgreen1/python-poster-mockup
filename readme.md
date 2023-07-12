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
