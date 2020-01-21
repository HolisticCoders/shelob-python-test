from enum import Flag, auto
from typing import Any


class Attribute:

    class Side(Flag):

        plug = auto()
        socket = auto()
        both = plug | socket

    def __init__(self, name: str, value: Any, side: Side):
        self.name = name
        self.value = value
        self.side = side
