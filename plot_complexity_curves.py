import numpy as np
import matplotlib.pyplot as plt
# Enable interactive mode
plt.ion()

# Generate n values from 0 to 100
n = np.linspace(0, 30, 3)

# Calculate different time complexities
o_1 = np.ones_like(n)  # O(1)
o_log_n = np.log2(n + 1)  # O(log n), adding 1 to avoid log(0)
o_n = n  # O(n)
o_n_log_n = n * np.log2(n + 1)  # O(n log n)
o_n_squared = n ** 2  # O(n^2)

# Create the plot with a specific figure name
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(n, o_1, label='O(1)', linewidth=2)
ax.plot(n, o_log_n, label='O(log n)', linewidth=2)
ax.plot(n, o_n, label='O(n)', linewidth=2)
ax.plot(n, o_n_log_n, label='O(n log n)', linewidth=2)
ax.plot(n, o_n_squared, label='O(n²)', linewidth=2)

# Customize the plot
ax.set_xlabel('n')
ax.set_ylabel('Operations')
ax.set_title('Time Complexity Curves')
ax.legend()
ax.grid(True)

# Enable zoom and pan
plt.gcf().canvas.toolbar.pan()
plt.gcf().canvas.toolbar.zoom()

# Show the plot (it will be interactive)
plt.show(block=True)

# Save the plot as a PNG file with high DPI for better quality
plt.savefig('complexity_curves.png', dpi=300, bbox_inches='tight')
