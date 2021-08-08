# importing the modules needed for all questions
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Question N.1
s=np.random.rand(1000,2)

#Question N.2

#Scatter plot
x = s[:,0]
y = s[:,1]
plt.scatter(x,y)
plt.title("Scatter plot between $X$ and $Y$")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

#change colour to green
plt.scatter(x, y, c="green")
plt.title("Scatter plot in green colour")
plt.xlabel("$X$ axis")
plt.ylabel("$Y$ axis")
plt.show()

#change size to very small and colour to red
plt.scatter(x, y, c='red', s=10)
plt.title("Small size scatter plots")
plt.xlabel("$X axis$")
plt.ylabel("$Y axis$")
plt.show()

#now we add a legend and we change the shape and the edgecolours of the points on the scatter plot, while changing more factors such as colour and size
plt.scatter(x, y, c='purple', s=45, label='random x and y coordinates', marker='^', edgecolors="b")
plt.title("Scatter plot")
plt.xlabel("$X axis$")
plt.ylabel("$Y axis$")
plt.legend()
plt.show()

#Line plot with more variations
x1=s[:5,0]
y1=s[:5,1]
y2=s[5:10,1]
x2=s[5:10,0]
plt.plot(x1,y1, c="purple", label="x1 to y1", linestyle="dashed", linewidth=7)
plt.scatter(x2,y2, c="green", label="x2 to y2")
plt.title("Line plot example")
plt.xlabel("$X$ axis")
plt.ylabel("$Y$ axis")
plt.xticks([0,0.5,1])
plt.yticks([0,0.5,1])
plt.legend()
plt.show()