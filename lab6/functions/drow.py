import matplotlib.pyplot as plt


def plot_solutions(x, y_numerical, y_exact, title="Сравнение решений", xlabel="x", ylabel="y"):
    plt.figure(figsize=(10, 6))

    plt.plot(x, y_numerical, 'b-', linewidth=2, label="Численное решение")
    plt.plot(x, y_numerical, 'bo', markersize=5)  # Узлы сетки

    plt.plot(x, y_exact, 'r--', linewidth=2, label="Точное решение")

    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()

    plt.show()

