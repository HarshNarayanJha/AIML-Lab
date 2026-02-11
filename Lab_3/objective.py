import random

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x) + np.sin(10 * x / 3)


x = np.linspace(0, 10, 1000)
y = f(x)


def hill_climb(start, step=0.01, iters=500):
    x_curr = start
    path = [x_curr]

    for _ in range(iters):
        neigh = [x_curr - step, x_curr + step]
        neigh = [max(0, min(10, n)) for n in neigh]
        vals = [f(n) for n in neigh]

        maxv = max(vals)
        maxidx = np.argmax(vals)

        if maxv > f(x_curr):
            x_curr = neigh[maxidx]
            path.append(x_curr)
        else:
            break
    return x_curr, path


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


hcmax, hc_path = hill_climb(start=np.random.uniform(0, 10))
hc_y_path = [f(xx) for xx in hc_path]

samax, sa_path = sim_anneal(start=np.random.uniform(0, 10))
sa_y_path = [f(xx) for xx in sa_path]

print(f"Hill Climing Max: {hcmax}: f(x) = {f(hcmax)}")
print(f"Simulated Annealing Search: {samax}: f(x) = {f(samax)}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(x, y, label="Objective function f(x)", color="blue")
ax1.scatter(hc_path, hc_y_path, color="red", label="Hill Climb", s=5)
ax1.scatter(hc_path[0], hc_y_path[0], color="green", s=50, label="Start")
ax1.scatter(hc_path[-1], hc_y_path[-1], color="cyan", s=50, label="End")

ax1.set_title("Hill Climbing Search")
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.legend()

ax2.plot(x, y, label="Objective f(x)", color="blue")
ax2.scatter(sa_path, sa_y_path, color="green", label="Simulated Annealing", s=5)
ax2.scatter(sa_path[0], sa_y_path[0], color="orange", s=50, label="Start")
ax2.scatter(sa_path[-1], sa_y_path[-1], color="cyan", s=50, label="End")

ax2.set_title("Simulated Annealing Search")
ax2.set_xlabel("x")
ax2.set_ylabel("f(x)")
ax2.legend()

plt.tight_layout()
plt.show()
