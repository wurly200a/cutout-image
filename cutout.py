import sys
import os
from rembg import remove
from PIL import Image

if len(sys.argv) < 2:
    print("使用法: python script.py <入力ファイル> [出力ファイル]")
    sys.exit(1)

input_path = sys.argv[1]

if len(sys.argv) >= 3:
    output_path = sys.argv[2]
else:
    base, _ = os.path.splitext(input_path)
    output_path = base + "_result.png"

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print(f"完了: {output_path}")
