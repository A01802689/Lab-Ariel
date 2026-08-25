from PIL import Image
from typing import cast
from rgb_types import RGBStream, RGBTuple

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

def lsb_embed(host: Image.Image, secret: Image.Image) -> Image.Image:
    host_stream: RGBStream = cast(RGBStream, host.get_flattened_data())
    secret_stream: list[int] = cast(list[int], secret.get_flattened_data())
    out_stream: list[RGBTuple] = []

    for (red, green, blue), secret_pixel in zip(host_stream, secret_stream):
        green &= 254
        green |= 1 if secret_pixel == 255 else 0
        embedded_pixel: RGBTuple = (red, green, blue)
        out_stream.append(embedded_pixel)

    out_image: Image.Image = Image.new(mode='RGB', size=host.size)
    out_image.putdata(out_stream)
    return out_image

if __name__ == "__main__":
    secret: Image.Image
    host: Image.Image
    with Image.open('./images/fully_flipped_tree_embedded.png') as host, Image.open('./images/secret.png') as secret:
        embedded: Image.Image = lsb_extraction(host)
        embedded.save('./images/fully_flipped_tree_secret.png')