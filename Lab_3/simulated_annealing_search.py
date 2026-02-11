import random

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) + np.sin(10 * x / 3)


x = np.linspace(0, 10, 1000)
y = f(x)


def sim_anneal(start, step_size=0.2, iters=1000, T0=1.0, cooling=0.99):
    x_curr = start
    path = [x_curr]
    temp = T0

    for i in range(iters):
        T = T0 * (1 - i / iters)
        x_new = x_curr + random.uniform(-step_size, step_size)
        x_new = np.clip(x_new, 0, 10)

        dE = f(x_new) - f(x_curr)
        if dE > 0 or random.random() < np.exp(dE / T if T > 0 else 0):
            x_curr = x_new
            path.append(x_curr)

        temp *= cooling
        if temp < 1e-3:
            break

    return x_curr, path


samax, sa_path = sim_anneal(start=np.random.uniform(0, 10))
sa_y_path = [f(xx) for xx in sa_path]

print(f"Simulated Annealing Search: {samax}: f(x) = {f(samax)}")

plt.plot(x, y, label="Objective f(x)", color="blue")
plt.scatter(sa_path, sa_y_path, color="green", label="Simulated Annealing", s=5)
plt.scatter(sa_path[0], sa_y_path[0], color="orange", s=50, label="Start")
plt.scatter(sa_path[-1], sa_y_path[-1], color="cyan", s=50, label="End")

plt.title("Simulated Annealing Search")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.tight_layout()
plt.show()
