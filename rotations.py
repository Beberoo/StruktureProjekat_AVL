def left_rotate(x):
    if x is None or x.right is None:
        return x  # ništa ne radi

    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    return y


def right_rotate(y):
    if y is None or y.left is None:
        return y  # ništa ne radi

    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    return x