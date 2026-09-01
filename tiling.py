#----------------------------------------------------------
# Lab #1: Image Processing
#
# Date: 25-Aug-2026
# Authors:
#           A01803181 Alexander Mejia Tovar.
#           A01801589 Pablo Alejandro Ortiz Montes.
#----------------------------------------------------------

from PIL import Image
from typing import cast
from rgb_types import RGBMatrix

def move_pixels(image: Image.Image, canvas_grid: RGBMatrix, delta: tuple[int, int]) -> RGBMatrix:
    width, height = image.size
    image_grid: RGBMatrix = cast(RGBMatrix, image.load())
    for y in range(height):
        for x in range(width):
            canvas_grid[x + delta[0], y + delta[1]] = image_grid[x, y]
    return canvas_grid

def tiling(images: list[Image.Image], deltas: list[tuple[int,int]]) -> Image.Image:
    sub_width, sub_height = images[0].size
    canvas: Image.Image = Image.new(mode='RGB', size=(2 * sub_width, 2 * sub_height))
    canvas_grid: RGBMatrix = cast(RGBMatrix, canvas.load())
    for image, delta in zip(images, deltas):
        canvas_grid = move_pixels(image, canvas_grid, delta)
    return canvas

if __name__ == "__main__":
    image_paths: list[str] = [
        './images/tree.png',
        './images/puppy.png',
        './images/snake.png',
        './images/woman.png'
    ]
    with Image.open(image_paths[0]) as img1, Image.open(image_paths[1]) as img2, Image.open(image_paths[2]) as img3, Image.open(image_paths[3]) as img4:
        images: list[Image.Image] = [img1, img2, img3, img4]
        width, height = img1.size
        deltas: list[tuple[int, int]] = [ (0,0), (width, 0), (0, height), (width, height) ]
        output_image: Image.Image = tiling(images, deltas)
        output_image.save('./images/tiling_output.png')