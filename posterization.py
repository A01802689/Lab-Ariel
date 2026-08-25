
from PIL import Image
from typing import cast
from rgb_types import RGBStream, RGBTuple


def poli(input_path:str, out_path:str)->None:
    in_image: Image.Image
    with Image.open(input_path) as hola:
        in_image = hola.convert('RGB')
        size: tuple[int,int] = hola.size
        in_stream = cast(RGBStream, in_image.get_flattened_data())
    out_stream: list[RGBTuple] = [] 
    red: int
    green: int
    blue:int
   
    for(red, green, blue) in in_stream:
            Y: int = (red + green + blue)//3
            if( Y < 50):
                 out_stream.append((120, 41, 15))
            elif( Y < 130):
                 out_stream.append((255, 125, 0))
            else:
                 out_stream.append((255, 236, 209))

    out_img: Image.Image = Image.new('RGB', size)
    out_img.putdata(out_stream)
    out_img.save(out_path)

    
if __name__ == '__main__':
    poli('images/velvet_underground.png', 'images/posterization_output.png')
    print('Done!')