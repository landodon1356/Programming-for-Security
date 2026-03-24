import matplotlib.pyplot as plt

# First 5 cubes
x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

ax.set_title("First Five Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
#LD
