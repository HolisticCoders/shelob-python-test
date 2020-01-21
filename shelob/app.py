class ShelobApp:

    def __init__(self):
        self.scenes = []
        self.active_scene = None
        self.active_graph = None
        self.is_evaluation_paused = False

    def new_scene(self):
        scene = shelob_api.Scene()  # pylint: disable=undefined-variable
        self.scenes.append(scene)
        self.load_scene(scene)

    def load_scene(self, scene):
        self.active_scene = scene
        # Load data from scene.

    def save_scene(self, path):
        text = self.active_scene.serialize()
        with open(path, 'w') as handle:
            handle.write(text)

    def process(self, delta):
        """Called by the GUI framework each frame."""
        if not self.is_evaluation_paused:
            self.active_graph.evaluate()

    def add_node(self, name, node_type):
        node = self.active_graph.add_node(name, node_type)  # pylint: disable=unused-variable
        # Create node view and add it to the graph view.

    def delete_node(self, node):
        pass

    def connect_attributes(self, plug, socket):
        # https://docs.rs/petgraph/0.5.0/petgraph/graph/struct.Graph.html#method.update_edge
        self.active_graph.connect(plug, socket)

    def disconnect_attributes(self, plug, socket):
        pass

    def set_attribute(self, attribute, value):
        pass

    def group_nodes(self, selected_nodes):
        graph = self.active_graph.group(selected_nodes)  # pylint: disable=unused-variable
        # Update view

    def ungroup_nodes(self, graph):
        pass

    def set_active_graph(self, graph):
        self.active_graph = graph
