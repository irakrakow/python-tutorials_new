import matplotlib.pyplot as plt

# Dummy data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Plot the histogram
plt.hist(data, bins=5)

# Add a title and labels to the x and y axes
plt.title("Histogram of Dummy Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show the plot
plt.show()
# To run this code, you'll need to have the matplotlib library installed. You can install it using pip by running the following command:

# pip install matplotlib
# Once you have matplotlib installed, you can run the code by saving it to a file (e.g. histogram.py) and then running it using Python

# python histogram.py
# This will open a window with the histogram plot.
