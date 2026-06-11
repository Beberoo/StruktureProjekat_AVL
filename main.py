from benchmark import run_benchmark
from visualization import plot_results
import random
from draw_trees import show_trees

show_trees()



sizes = [1000, 5000, 10000]

bst_insert_times = []
avl_insert_times = []
bst_search_times = []
avl_search_times = []

bst_times_sorted = []
avl_times_sorted = []

bst_times_reversed = []
avl_times_reversed = []

for size in sizes:

    # 1. RANDOM
    data = random.sample(range(1, size * 10), size)
    bst_i, avl_i, bst_s, avl_s = run_benchmark(data)
    bst_insert_times.append(bst_i)
    avl_insert_times.append(avl_i)
    bst_search_times.append(bst_s)
    avl_search_times.append(avl_s)

    # 2. SORTED (worst BST)
    data = list(range(1, size + 1))
    bst_i, avl_i, bst_s, avl_s = run_benchmark(data)
    bst_times_sorted.append(bst_i)
    avl_times_sorted.append(avl_i)

    # 3. REVERSED
    data = list(range(size, 0, -1))
    bst_i, avl_i, bst_s, avl_s = run_benchmark(data)
    bst_times_reversed.append(bst_i)
    avl_times_reversed.append(avl_i)


plot_results(sizes, bst_insert_times, avl_insert_times, "random_insert")
plot_results(sizes, bst_times_sorted, avl_times_sorted, "sorted_insert")
plot_results(sizes, bst_times_reversed, avl_times_reversed, "reversed_insert")
plot_results(sizes, bst_search_times, avl_search_times, "search")