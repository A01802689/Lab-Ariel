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


SCALE: int = 2 

rutas = ['images/woman.png','images/woman.png', 'images/woman.png', 'images/woman.png']
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
         
    contador: int = -1
    for c in imagenesNuevas:
        contador += 1
        for y in range(new_height):
            for x in range(new_width):
                red, green,blue = c[x,y]
                Y = (red + green + blue) // 3

                if contador == 0 :
                    if Y < 50:
                        c[x, y] = (120, 41, 15)
                    elif Y < 130:
                        c[x, y] = (255, 125, 0)
                    else:
                        c[x, y] = (255, 236, 209)
                elif contador == 1:
                     if Y < 50:
                        c[x, y] = (13, 27, 62)  
                     elif Y < 130:
                         c[x, y] = (30, 87, 153)
                     else:
                        c[x, y] = (176, 216, 255) 

                elif contador == 2:
                        if Y < 50:
                           c[x, y] = (69, 11, 11)
                        elif Y < 130:
                            c[x, y] = (178, 34, 34)
                        else:
                           c[x, y] = (255, 179, 179) 

                elif contador == 3:
                        if Y < 50:
                            c[x, y] = (14, 46, 20)    
                        elif Y < 130:
                            c[x, y] = (46, 125, 50)
                        else:
                           c[x, y] = (200, 245, 200) 

        
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
    shrink('images/warhol_effect_output.png')
    print('Done!') 