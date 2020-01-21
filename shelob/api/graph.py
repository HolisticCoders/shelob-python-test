from __future__ import annotations
from typing import List, Type

from networkx import DiGraph, topological_sort

from .attribute import Attribute
from .node import Node


class Graph(Node):

    def __init__(self, name: str):
        super().__init__(name)

        self.children : List[Node] = []
        self.attribute_graph = DiGraph()

    def evaluate(self, delta: float):
        for node in self.children:
            node.evaluate(delta)
        # executed_nodes = set()
        # for attribute in list(topological_sort(self.attribute_graph)):
        #     node = attribute.node
        #     if node in executed_nodes:
        #         continue
        #     node.evaluate(delta)
        #     executed_nodes.add(node)

    def add_node(self, name: str, node_type: Type[Node]) -> Node:
        node = node_type(name)
        self.children.append(node)
        return node

    def delete_node(self, node: Node):
        self.children.remove(node)

    def connect(self, plug: Attribute, socket: Attribute):
        self.attribute_graph.add_edge(plug, socket)

    def disconnect(self, plug: Attribute, socket: Attribute):
        self.attribute_graph.remove_edge(plug, socket)

    def group(self, name: str, children: List[Node]) -> Graph:
        new_graph = Graph(name)
        # TODO: move nodes and connections to ``new_graph``
        self.children.append(new_graph)
        return new_graph

    def ungroup(self) -> List[Node]:
        pass
