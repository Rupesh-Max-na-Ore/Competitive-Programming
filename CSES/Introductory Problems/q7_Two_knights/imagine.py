import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_knight_attack_3x2():
    fig, ax = plt.subplots(figsize=(3, 2))

    # Draw 3x2 grid
    for y in range(2):
        for x in range(3):
            color = 'white' if (x + y) % 2 == 0 else 'lightgray'
            rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    # Positions of 4 attacking knight pairs (from top-left)
    knight_pairs = [
        ((0, 0), (1, 2)),  # Knight A bottom-left, Knight B upper-middle
        ((1, 0), (0, 2)),  # Knight A bottom-middle, Knight B upper-left
        ((2, 0), (1, 2)),  # Knight A bottom-right, Knight B upper-middle
        ((1, 0), (2, 2)),  # Knight A bottom-middle, Knight B upper-right
    ]

    for (x1, y1), (x2, y2) in knight_pairs:
        ax.text(x1 + 0.5, y1 + 0.5, '♞', fontsize=18, ha='center', va='center', color='blue')
        ax.text(x2 + 0.5, y2 + 0.5, '♞', fontsize=18, ha='center', va='center', color='red')
        # Draw arrow between them
        ax.annotate('', xy=(x2 + 0.5, y2 + 0.5), xytext=(x1 + 0.5, y1 + 0.5),
                    arrowprops=dict(arrowstyle="->", color='green', lw=1))

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.title("Knight Attack Positions in 3x2 Block")
    plt.gca().invert_yaxis()
    plt.show()

draw_knight_attack_3x2()
