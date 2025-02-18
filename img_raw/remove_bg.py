from rembg import remove
from PIL import Image
import os

# List of uploaded image file paths
image_paths = [
    'D:\\WireLinx-official\\img_raw\\20250216_205231.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_204512.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205450.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_204459.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205120.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_204536.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205758.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205131.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_204251.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205102.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205818.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205842.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205357.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205830.jpg',
    'D:\\WireLinx-official\\img_raw\\20250216_205905.jpg'
]

# Process images and save them with transparent background
output_paths = 'D:\WireLinx-official\img'
for image_path in image_paths:
    with Image.open(image_path) as img:
        img_no_bg = remove(img)
        output_path = image_path.replace(".jpg", "_transparent.png")
        img_no_bg.save(output_path, "PNG")
        #output_paths.append(output_path)
