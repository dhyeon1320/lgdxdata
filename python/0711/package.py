import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,7))
plt.boxplot(([100,23,34,4,2],[23,35,6,2,143]))
plt.grid()
plt.show()
fig.savefig("graph.png")

print(int('20',5))