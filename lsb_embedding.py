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
from rgb_types import RGBStream, RGBTuple

def lsb_embedding(host: Image.Image, secret: Image.Image) -> Image.Image:
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
    with Image.open('./images/snake.png') as host, Image.open('./images/one_bit_image.png') as secret:
        embedded: Image.Image = lsb_embedding(host, secret)
        embedded.save('./images/lsb_embedding_output.png')