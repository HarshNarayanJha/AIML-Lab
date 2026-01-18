# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib>=3.10.8",
#     "networkx>=3.6.1",
#     "numpy>=2.4.1",
#     "scipy>=1.17.0",
# ]
# ///

# %%
# Question 1

grades = {"Alice": 85, "Bob": 92, "Charlie": 78}


def getGrade(name):
    return grades.get(name.title(), "Not Found")


print(getGrade("Alice"))
print(getGrade("bob"))
print(getGrade("noone"))

# %%
# Question 2
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

arr = np.random.normal(0, 1, 1000)
x = np.linspace(-4, 4, 200)
pdf = norm.pdf(x, 0, 1)

plt.hist(arr, bins=30, density=True, label="Normal Dist.")
plt.plot(x, pdf, label="Bell Curve")

plt.grid()
plt.title("Bell Curve Comparision")
plt.legend()
plt.show()

# %%
# Quetion 3

import numpy as np

arr = np.arange(1, 500 + 1)
np.random.shuffle(arr)


def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            steps += 1

        arr[j + 1] = key
    return arr, steps


def merge_sort(arr, steps):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, steps)
        merge_sort(R, steps)

        i = j = k = 0
        while i < len(L) and j < len(R):
            steps[0] += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


iarr, isteps = insertion_sort(arr.copy())
msteps = [0]
merge_sort(arr.copy(), msteps)

print("Insertion Sort:", isteps, "Steps")
print("Merge Sort:", msteps[0], "Steps")


# %%

# Question 4

from pprint import pprint

adj_list = {
    "A": ["B", "C"],
    "B": ["A", "C", "E"],
    "C": ["A", "B", "D"],
    "D": ["C", "F"],
    "E": ["B", "F"],
    "F": ["D", "E"],
}

pprint(adj_list)


# %%

# Question 5

from pprint import pprint

adj_matrix = [
    # A  B  C  D  E  F
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 1, 0, 1, 0],  # B
    [1, 1, 0, 1, 0, 0],  # C
    [0, 0, 1, 0, 0, 1],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 0, 1, 1, 0],  # F
]

pprint(adj_matrix)


# %%
# Question 6

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

glist = nx.Graph()
for n, ne in adj_list.items():
    for nei in ne:
        glist.add_edge(n, nei)

nodes = list("ABCDEF")

gmat = nx.Graph()
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if adj_matrix[i][j] == 1:
            gmat.add_edge(nodes[i], nodes[j])

plt.figure(figsize=(12, 5))
pos = nx.spring_layout(glist)

plt.subplot(1, 2, 1)
nx.draw(glist, pos, with_labels=True, node_color="lightblue")
plt.title("Adjacency List")

plt.subplot(1, 2, 2)
nx.draw(gmat, pos, with_labels=True, node_color="pink")
plt.title("Adjacency Matrix")

plt.show()
