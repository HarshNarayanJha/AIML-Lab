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


hcmax, hc_path = hill_climb(start=np.random.uniform(0, 10))
hc_y_path = [f(xx) for xx in hc_path]

print(f"Hill Climing Max: {hcmax}: f(x) = {f(hcmax)}")

plt.plot(x, y, label="Objective function f(x)", color="blue")
plt.scatter(hc_path, hc_y_path, color="red", label="Hill Climb", s=5)
plt.scatter(hc_path[0], hc_y_path[0], color="green", s=50, label="Start")
plt.scatter(hc_path[-1], hc_y_path[-1], color="cyan", s=50, label="End")

plt.title("Hill Climbing Search")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.tight_layout()
plt.show()
