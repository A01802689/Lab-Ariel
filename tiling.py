#----------------------------------------------------------
# Lab #1: Image Processing
#
# Date: 25-Aug-2026
# Authors:
#           0A01803181 Alexander Mejia Tovar.
#           A01801589 Pablo Alejandro Ortiz Montes.
#----------------------------------------------------------

from PIL import Image
from typing import cast
from rgb_types import RGBMatrix

SCALE: int = 2

rutas = ['images/tree.png','images/woman.png', 'images/snake.png', 'images/puppy.png']
imagenesNuevas= []
new_width: int = 0
new_height: int = 0

def shrink(output_path: str) -> None:
    in_img: Image.Image
    new_width: int = 0
    new_height: int = 0
    for i in rutas:
            with Image.open(i) as in_img:
                in_img = in_img.convert('RGB')
                size: tuple[int, int] = in_img.size
                in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())
            width: int
            height: int
            width, height = size
            new_width: int = width // SCALE 
            new_height: int = height // SCALE
            out_img: Image.Image = Image.new('RGB', (new_width, new_height))
            out_grid: RGBMatrix = cast(RGBMatrix, out_img.load())

            for y in range(new_height):
                for x in range(new_width):
                    out_grid[x, y] = in_grid[x * SCALE, y * SCALE]
            imagenesNuevas.append(out_grid)

    lienzo_og: tuple[int, int] = (2 * new_width,  2 * new_height)
    out_img: Image.Image = Image.new('RGB',lienzo_og )
    OUTgrid_lienzo: RGBMatrix = cast(RGBMatrix, out_img.load())

    for ind in range(len(imagenesNuevas)):
        for y in range(new_height):
            for x in range(new_width):
                pixel = imagenesNuevas[ind][x, y] 
                if ind == 0:
                    OUTgrid_lienzo[x + 0,y + 0] = pixel
                elif ind == 1:
                    OUTgrid_lienzo[x + new_width,y + 0] = pixel
                elif ind == 2:
                    OUTgrid_lienzo[x + 0,y + new_height] = pixel
                else:
                    OUTgrid_lienzo[x + new_width,y + new_height] = pixel
    out_img.save(output_path)

if __name__ == '__main__':
    shrink('images/tiling_output.png')
    print('Done!') 