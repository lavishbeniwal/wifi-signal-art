import matplotlib.pyplot as plt
import numpy as np

def render_art(visuals):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_facecolor("black")
    ax.axis("off")

    for v in visuals:
        x, y = np.random.rand(2)
        size = 300 + v["strength"] * 2000
        alpha = 0.3 + v["strength"] * 0.6

        if v["freq"] == 2.4:
            color = (1.0, v["strength"], 0.2)
        else:
            color = (0.2, v["strength"], 1.0)

        ax.scatter(x, y, s=size, c=[color], alpha=alpha)

    plt.savefig("wifi_art.png", dpi=300, bbox_inches="tight")
    plt.show()
