import matplotlib.pyplot as plt


def get_positions(root):
    positions = {}
    index = [0]

    def traverse(node, depth):
        if node is None:
            return

        traverse(node.left, depth + 1)
        positions[node.key] = (index[0], -depth)
        index[0] += 1
        traverse(node.right, depth + 1)

    traverse(root, 0)
    return positions


def add_edges(graph, root):
    if root is None:
        return

    if root.left:
        graph.add_edge(root.key, root.left.key)
        add_edges(graph, root.left)

    if root.right:
        graph.add_edge(root.key, root.right.key)
        add_edges(graph, root.right)


def draw_tree(
    root,
    title="Tree",
    ax=None,
    node_color="#a8d8ea",
    edge_color="#444444",
    title_color="#111111"
):
    import networkx as nx

    G = nx.DiGraph()
    add_edges(G, root)

    pos = get_positions(root)

    if ax is None:
        _, ax = plt.subplots(figsize=(12, 7))

    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_size=1400,
        node_color=node_color,
        edge_color=edge_color,
        font_size=11,
        font_weight="bold",
        linewidths=1.2,
        arrows=False
    )

    ax.set_title(title, fontsize=14, color=title_color)
    ax.margins(0.15)
    ax.set_axis_off()