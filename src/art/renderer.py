import matplotlib.pyplot as plt
import numpy as np

def render_art(visuals):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Dark background (huge upgrade)
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.axis("off")

    for v in visuals:
        # Polar layout: signals orbit center
        angle = np.random.uniform(0, 2 * np.pi)
        radius = 0.15 + v["strength"] * 0.45

        x = 0.5 + radius * np.cos(angle)
        y = 0.5 + radius * np.sin(angle)

        size = 300 + v["strength"] * 2500
        alpha = 0.25 + v["strength"] * 0.6

        # Color by frequency
        if v["freq"] == 2.4:
            color = (0.2, 1.0, 0.8)   # cyan/green
        else:
            color = (0.5, 0.6, 1.0)   # blue/purple

        # Glow layer (big + faint)
        ax.scatter(
            x, y,
            s=size * 1.8,
            c=[color],
            alpha=alpha * 0.25,
            linewidths=0
        )

        # Core layer (small + bright)
        ax.scatter(
            x, y,
            s=size,
            c=[color],
            alpha=alpha,
            linewidths=0
        )

    plt.savefig("wifi_art.png", dpi=300, bbox_inches="tight")
    plt.show()
