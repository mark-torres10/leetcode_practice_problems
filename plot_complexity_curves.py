import numpy as np
import matplotlib.pyplot as plt

# Generate n values from 0 to 100000
n = np.linspace(0, 100000, 1000)

# Calculate different time complexities
o_1 = np.ones_like(n)  # O(1)
o_log_n = np.log2(n + 1)  # O(log n), adding 1 to avoid log(0)
o_n = n  # O(n)
o_n_log_n = n * np.log2(n + 1)  # O(n log n)
o_n_squared = n ** 2  # O(n^2)

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(n, o_1, label='O(1)', linewidth=2)
plt.plot(n, o_log_n, label='O(log n)', linewidth=2)
plt.plot(n, o_n, label='O(n)', linewidth=2)
plt.plot(n, o_n_log_n, label='O(n log n)', linewidth=2)
plt.plot(n, o_n_squared, label='O(n²)', linewidth=2)

# Customize the plot
plt.xlabel('n')
plt.ylabel('Operations')
plt.title('Time Complexity Curves')
plt.legend()
plt.grid(True)

# Add some padding to y-axis to make the lower curves more visible
plt.ylim(-100, 2000)

# Show the plot
plt.show()

# Save the plot as a PNG file with high DPI for better quality
plt.savefig('complexity_curves.png', dpi=300, bbox_inches='tight')
