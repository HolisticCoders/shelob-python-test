from abc import ABCMeta, abstractmethod
from typing import Any, List

from .attribute import Attribute


class Node(metaclass=ABCMeta):

    def __init__(self, name: str):
        self.name = name
        self.attributes: List[Attribute] = []
        self._attributes_by_name = {}
        self._plugs = []
        self._sockets = []

    @abstractmethod
    def evaluate(self, delta: float):
        pass

    def attribute(self, name: str) -> Attribute:
        return self._attributes_by_name[name]

    def add_attribute(self, name: str, side: Attribute.Side, value:Any = None) -> Attribute:
        attribute = Attribute(name, value, side)
        self.attributes.append(attribute)
        self._attributes_by_name[name] = attribute
        if side == Attribute.Side.plug:
            self._plugs.append(attribute)
        elif side == Attribute.Side.socket:
            self._sockets.append(attribute)
        elif side == Attribute.Side.both:
            self._plugs.append(attribute)
            self._sockets.append(attribute)
        return attribute
