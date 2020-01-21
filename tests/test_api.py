def test_add_node():
    from shelob.api.graph import Graph
    from shelob.lib.nodes import AddNode

    graph = Graph('root')
    node = graph.add_node('add', AddNode)

    assert node.attribute('sum').value == 0

    node.attribute('socket1').value = 1
    node.attribute('socket2').value = 4

    assert node.attribute('sum').value == 0

    graph.evaluate(0.016)

    assert node.attribute('sum').value == 5


def test_add_node_more_sockets():
    from shelob.api.graph import Graph
    from shelob.api.attribute import Attribute
    from shelob.lib.nodes import AddNode

    graph = Graph('root')
    node = graph.add_node('add', AddNode)

    assert node.attribute('sum').value == 0

    node.attribute('socket1').value = 1
    node.attribute('socket2').value = 4

    attribute = node.add_attribute('socket3', Attribute.Side.socket)
    attribute.value = 9

    assert node.attribute('sum').value == 0

    graph.evaluate(0.016)

    assert node.attribute('sum').value == 14
