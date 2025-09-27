import math
import matplotlib.pyplot as plt

# n values and experimental times (from repeated snippet)
n_values = [
    1000, 3000, 10000, 30000, 100000, 300000, 
    1000000, 3000000, 10000000, 30000000, 100000000
]

experimental_times = [
    6802900, 5309600, 7624000, 8327700, 8523400,
    11992800, 9652900, 19009100, 12706800, 17114600, 18508100
]

# Step 1: Theoretical values (log log n)^2
theoretical_values = [(math.log(math.log(n)))**2 for n in n_values]

# Step 2: Scaling factor using average to bring curves closer
scale = sum(experimental_times) / sum(theoretical_values)

# Step 3: Adjusted theoretical values
adjusted_theoretical = [val * scale for val in theoretical_values]

# Step 4: Print table for reference
print("n\tExperimental (ns)\tTheoretical\tAdjusted Theoretical (ns)")
for n, exp, theo, adj in zip(n_values, experimental_times, theoretical_values, adjusted_theoretical):
    print(f"{n}\t{exp}\t{theo:.6f}\t{adj:.2f}")

# Step 5: Plot both curves
plt.figure(figsize=(9,6))
plt.plot(n_values, experimental_times, 'o-', label="Experimental (ns)", color='red')
plt.plot(n_values, adjusted_theoretical, 's--', label="Adjusted Theoretical (ns, O((log log n)^2)))", color='blue')

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Input Size n (log scale)")
plt.ylabel("Time (ns, log scale)")
plt.title("Experimental vs Adjusted Theoretical Runtime (Aryan Saxena)")
plt.legend()
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.tight_layout()
plt.show()
