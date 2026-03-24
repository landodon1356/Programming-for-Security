import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))

fig = px.scatter(
    x=rw.x_values,
    y=rw.y_values,
    color=point_numbers,
    title="Random Walk with Plotly"
)

fig.show()
#LD
