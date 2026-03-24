import matplotlib.pyplot as plt
from die import Die

die = Die()

results = [die.roll() for _ in range(1000)]
poss_results = range(1, die.num_sides + 1)
frequencies = [results.count(value) for value in poss_results]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)

ax.set_title("D6 Results with Matplotlib", fontsize=20)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.tick_params(labelsize=12)

plt.show()
#LD
