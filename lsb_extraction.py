from PIL import Image
from typing import cast
from rgb_types import RGBStream

def lsb_extraction(image: Image.Image) -> Image.Image:
    image.convert(mode='RGB')
    size: tuple[int, int] = image.size
    in_stream: RGBStream = cast(RGBStream, image.get_flattened_data())
    bin_image: Image.Image = Image.new(mode='1', size=size)
    bin_stream: list[int] = []
    for (_, green, _) in in_stream:
        green &= 1
        bin_stream.append(green)
    bin_image.putdata(bin_stream)
    return bin_image

if __name__ == "__main__":
    image: Image.Image
    with Image.open('./images/snake.png') as image:
        secret: Image.Image = lsb_extraction(image)
        secret.save('./images/lsb_extraction_output.png')