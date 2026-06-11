import time
from bst import BST
from avl import AVL


def measure_search(tree, root, data):
    start = time.time()

    for x in data:
        tree.search(root, x)

    return time.time() - start


def run_benchmark(data):

    # ------------------
    # BST INSERT
    # ------------------
    bst = BST()
    root_bst = None

    start = time.time()
    for x in data:
        root_bst = bst.insert(root_bst, x)
    bst_insert_time = time.time() - start

    # ------------------
    # AVL INSERT
    # ------------------
    avl = AVL()
    root_avl = None

    start = time.time()
    for x in data:
        root_avl = avl.insert(root_avl, x)
    avl_insert_time = time.time() - start

    # ------------------
    # SEARCH TEST
    # ------------------
    search_data = data[:]  # tražimo sve elemente

    bst_search_time = measure_search(bst, root_bst, search_data)
    avl_search_time = measure_search(avl, root_avl, search_data)

    return (
        bst_insert_time,
        avl_insert_time,
        bst_search_time,
        avl_search_time
    )