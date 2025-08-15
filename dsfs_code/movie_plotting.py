import matplotlib.pyplot as plt

movies = ['movie1', 'movie2', 'movie3']
awards = [5, 2, 10]

plt.plot(movies, awards, color='green', marker='o', linestyle='solid')
plt.show("Movie rating")
plt.show()

plt.bar(range(len(movies)), awards)