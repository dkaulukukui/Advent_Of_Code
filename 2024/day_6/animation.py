import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a 2D list or array
rows, cols = 10, 10  # Dimensions of the grid
grid = np.random.randint(0, 2, size=(rows, cols))  # Random binary grid (0s and 1s)

# Function to update the grid for animation
def update_grid(frame, grid, img):
    # Example: Randomly toggle values between 0 and 1
    new_grid = np.random.randint(0, 2, size=grid.shape)
    img.set_array(new_grid)  # Update the image data
    return [img]

# Create the figure and axis
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary")  # Initial display of the grid
ax.axis("off")  # Hide axis

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update_grid,
    fargs=(grid, img),
    frames=100,  # Number of frames
    interval=200,  # Time between frames in milliseconds
    blit=True  # Only re-draw the parts that have changed
)

# Display the animation
plt.show()
