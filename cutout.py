from rembg import remove
from PIL import Image
#input_path = 'b.jpg'
#input_path = 'c.png'
#input_path = 'P1000001.png'
input_path = 'IMG_1636.JPG'
output_path = 'P1000001_output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
