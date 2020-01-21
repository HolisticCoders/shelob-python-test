from shelob.api.node import Node
from shelob.api.attribute import Attribute


class AddNode(Node):

    def __init__(self, name: str):
        super().__init__(name)
        self.add_attribute('socket1', Attribute.Side.socket, 0)
        self.add_attribute('socket2', Attribute.Side.socket, 0)
        self.add_attribute('sum', Attribute.Side.plug, 0)

    def evaluate(self, delta: float):
        result = sum([attr.value for attr in self._sockets])
        self._attributes_by_name['sum'].value = result
