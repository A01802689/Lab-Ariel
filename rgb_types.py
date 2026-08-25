# RGB Matrix protocol and type definitions for handling RGB pixel
# operations and streams.

from typing import Protocol

type RGBTuple = tuple[int, int, int]
type RGBStream = tuple[RGBTuple, ...]

class RGBMatrix(Protocol):
    def __getitem__(self, xy: tuple[int, int]) -> RGBTuple: ...
    def __setitem__(self, xy: tuple[int, int], value: RGBTuple) -> None: ...