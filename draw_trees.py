from bst import BST
from avl import AVL
from tree_visualization import draw_tree
import random
import matplotlib.pyplot as plt
import os


def show_trees(size=20):

    data = random.sample(range(1, size * 10), size)

    # BST TREE
    bst = BST()
    root_bst = None
    for x in data:
        root_bst = bst.insert(root_bst, x)

    # AVL TREE
    avl = AVL()
    root_avl = None
    for x in data:
        root_avl = avl.insert(root_avl, x)

    os.makedirs("results", exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))
    draw_tree(root_bst, "BST Tree", ax=axes[0])
    draw_tree(root_avl, "AVL Tree", ax=axes[1])
    plt.tight_layout()
    plt.savefig("results/trees.png", bbox_inches="tight", dpi=140)
    plt.show()