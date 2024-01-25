import plotly.graph_objs as go
import plotly.express as px
import numpy as np

# Generating sample data
data = np.random.rand(10, 10)

# Creating a heatmap with Plotly Express
fig = px.imshow(data, color_continuous_scale='Viridis')  # 'Viridis' is a predefined colorscale
fig.show()
