import matplotlib.pyplot as plt
import os

def plot_results(sizes, bst_times, avl_times, name="result"):

    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(8, 5), dpi=140)

    plt.plot(sizes, bst_times, marker="o", linewidth=2.2, label="BST", color="#1f77b4")
    plt.plot(sizes, avl_times, marker="o", linewidth=2.2, label="AVL", color="#ff7f0e")

    plt.xlabel("Broj elemenata")
    plt.ylabel("Vrijeme (s)")
    plt.title(name)

    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.ylim(bottom=0)
    plt.tight_layout()

    plt.savefig(f"results/{name}.png", bbox_inches="tight")
    plt.close()