import numpy as np

rng = np.random.default_rng()

array = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10])
rng.shuffle(array)

print(array)

np.random.seed(seed=1)

fruits = np.array(["🍎", "🍍", "🍊", "🍌", "🥥"])
fruits = rng.choice(fruits, size=(3, 3))

print(fruits)