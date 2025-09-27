# Project 1: Time Complexity Analysis of Nested Loops

**Author:** Aryan Saxena  
**Purpose:** Analyze the time complexity of a nested while-loop algorithm both theoretically and experimentally. Compare the experimental runtime with the theoretical estimate and visualize the results.

---

## **Files Included**

1. **ComplexityExperiment.java**  
   - Java program that implements the nested loops snippet.  
   - Measures runtime for various input sizes (`n`) by repeating the snippet multiple times to get smoother measurements.  
   - Prints the experimental runtime in nanoseconds for each `n`.

2. **plot_results.py**  
   - Python script to visualize the experimental results against the adjusted theoretical values.  
   - Computes theoretical values as \((\log\log n)^2\) and scales them for comparison.  
   - Plots experimental vs adjusted theoretical runtime on a log-log scale.

---

## **How to Run**

### Java Program
1. Compile the Java file:
   ```bash
   javac ComplexityExperiment.java

2. Run the program:

  ```bash
  java ComplexityExperiment

3. Output: Experimental runtime for each n in nanoseconds.

Python Plot
Ensure Python 3 is installed along with matplotlib.

Run the script:

bash
Copy code
python plot_results.py
Output: Log-log plot showing experimental vs adjusted theoretical runtime.

Purpose of This Project
Theoretical Analysis:

Outer loop: 
𝑂
(
log
⁡
log
⁡
𝑛
)
O(loglogn)

Inner loop: 
𝑂
(
log
⁡
log
⁡
𝑛
)
O(loglogn)

Total time complexity: 
𝑂
(
(
log
⁡
log
⁡
𝑛
)
2
)
O((loglogn) 
2
 )

Experimental Validation:

Measures real execution time for different n.

Scales theoretical values for direct comparison.

Confirms that the experimental trend follows the predicted theoretical growth.

GitHub Repository
All files and instructions for running the project are included here.

Link: https://github.com/YourUsername/AlgorithmTimeComplexity

Notes
The experimental runtime may vary slightly due to system performance and randomness in array initialization.

Repetition of the snippet in Java ensures smoother and more reliable measurements for small values of n.
