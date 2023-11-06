import os
import subprocess
from io import BytesIO
from PIL import Image  # pip install pillow
import mozjpeg_lossless_optimization

def optimize_png(image_path, output_path):
    """
    Optimize a PNG image using pngquant. (Assuming pngquant is installed)
    
    Parameters:
    - image_path (str): Path to the PNG image.
    - output_path (str): Where to save the optimized image.
    """
    subprocess.run(['pngquant', '--force', '--output', output_path, image_path])

def optimize_jpeg(input_path, output_path):
    jpeg_io = BytesIO()

    with Image.open(input_path, "r") as image:
        image.convert("RGB").save(jpeg_io, format="JPEG", quality=90)

    jpeg_io.seek(0)
    jpeg_bytes = jpeg_io.read()

    optimized_jpeg_bytes = mozjpeg_lossless_optimization.optimize(jpeg_bytes)

    with open(output_path, "wb") as output_file:
        output_file.write(optimized_jpeg_bytes)
        
# def optimize_jpeg(image_path, output_path):
#     """
#     Optimize a JPEG image using mozjpeg_lossless_optimization.
    
#     Parameters:
#     - image_path (str): Path to the JPEG image.
#     - output_path (str): Where to save the optimized image.
#     """
#     with open(image_path, "rb") as input_jpeg_file:
#         input_jpeg_bytes = input_jpeg_file.read()

#     output_jpeg_bytes = mozjpeg_optimize(input_jpeg_bytes)

#     with open(output_path, "wb") as output_jpeg_file:
#         output_jpeg_file.write(output_jpeg_bytes)

def main():
    folder_path = input("Enter the path to the root folder: ")

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(dirpath, filename)
                print(f"Optimizing {image_path}...")

                if filename.lower().endswith('.png'):
                    optimize_png(image_path, image_path)
                else:
                    optimize_jpeg(image_path, image_path)

    print("Optimization completed!")

if __name__ == '__main__':
    main()
