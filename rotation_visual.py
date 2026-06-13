import os
import matplotlib.pyplot as plt

from node import Node
from rotations import left_rotate, right_rotate
from tree_visualization import draw_tree


def clone_tree(root):
    if root is None:
        return None

    node = Node(root.key)
    node.height = root.height
    node.left = clone_tree(root.left)
    node.right = clone_tree(root.right)
    return node


def save_rotation(before_root, after_root, title, filename):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    rotation_type = title.split()[0]
    style_by_rotation = {
        "LL": {"node": "#ffd6a5", "edge": "#c77d3b", "title": "#8c4b11"},
        "LR": {"node": "#cdeac0", "edge": "#4f8f3a", "title": "#2f5d25"},
        "RR": {"node": "#bde0fe", "edge": "#3a86c8", "title": "#1e4f7a"},
        "RL": {"node": "#f1c0e8", "edge": "#b565a7", "title": "#7d356e"},
    }
    style = style_by_rotation.get(
        rotation_type,
        {"node": "#a8d8ea", "edge": "#444444", "title": "#111111"}
    )

    draw_tree(
        before_root,
        f"{rotation_type}: Before",
        ax=ax1,
        node_color=style["node"],
        edge_color=style["edge"],
        title_color=style["title"]
    )
    draw_tree(
        after_root,
        f"{rotation_type}: After",
        ax=ax2,
        node_color=style["node"],
        edge_color=style["edge"],
        title_color=style["title"]
    )

    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight", dpi=140)
    plt.close(fig)


def build_ll_before():
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    return root


def build_rr_before():
    root = Node(10)
    root.right = Node(20)
    root.right.right = Node(30)
    return root


def build_lr_before():
    root = Node(30)
    root.left = Node(10)
    root.left.right = Node(20)
    return root


def build_rl_before():
    root = Node(10)
    root.right = Node(30)
    root.right.left = Node(20)
    return root


def generate_rotation_images(output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)

    ll_before = build_ll_before()
    ll_after = right_rotate(clone_tree(ll_before))
    save_rotation(
        ll_before,
        ll_after,
        "LL Rotation",
        os.path.join(output_dir, "rotation_LL.png")
    )

    rr_before = build_rr_before()
    rr_after = left_rotate(clone_tree(rr_before))
    save_rotation(
        rr_before,
        rr_after,
        "RR Rotation",
        os.path.join(output_dir, "rotation_RR.png")
    )

    lr_before = build_lr_before()
    lr_after = clone_tree(lr_before)
    lr_after.left = left_rotate(lr_after.left)
    lr_after = right_rotate(lr_after)
    save_rotation(
        lr_before,
        lr_after,
        "LR Rotation",
        os.path.join(output_dir, "rotation_LR.png")
    )

    rl_before = build_rl_before()
    rl_after = clone_tree(rl_before)
    rl_after.right = right_rotate(rl_after.right)
    rl_after = left_rotate(rl_after)
    save_rotation(
        rl_before,
        rl_after,
        "RL Rotation",
        os.path.join(output_dir, "rotation_RL.png")
    )