#data ingestion
#batch processing images

from PIL import Image
import pathlib
def resize_images_Pillow(leftMax, rightMax, directory):
    maxsize = (leftMax, rightMax)
    for input_img_path in pathlib.Path("input").iterdir():
        output_img_path = str(input_img_path).replace("input","output")
        with Image.open(input_img_path) as im:
            im.thumbnail(maxsize)
            im.save(output_img_path, "JPEG", dpi=(300,300))
            print(f"processing file {input_img_path} done...")
#data cleaning

#library import

#json-dictionary

#json-dataframe

#json-csv


