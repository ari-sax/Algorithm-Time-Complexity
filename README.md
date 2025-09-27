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
   '''bash
   javac ComplexityExperiment.java

2. Run the program:
   '''bash
   java ComplexityExperiment

4. Output: Experimental runtime for each n in nanoseconds.

Python Plot
1.Ensure Python 3 is installed along with matplotlib.
2.Run the script:
   '''bash
   python plot_results.py
3. Output: Log-log plot showing experimental vs adjusted theoretical runtime.

Purpose of This Project

Theoretical Analysis:
- Outer loop: 𝑂(log log 𝑛)
- Inner loop: 𝑂(log log 𝑛)
- Total time complexity: 𝑂((log log 𝑛)^2)

Experimental Validation:
- Measures real execution time for different n.
- Scales theoretical values for direct comparison.
- Confirms that the experimental trend follows the predicted theoretical growth.

Conclusions:
- The theoretical analysis predicted 𝑂((log log 𝑛)^2) time complexity.
- Experimental results validated the theoretical hypothesis.
- Adjusted theoretical values closely follow experimental results on a log-log plot.
- Minor fluctuations in experimental runtimes are normal due to system variability.

GitHub Code Repository:
The Java and Python files for this project can be accessed at:
https://github.com/ari-sax/AlgorithmTimeComplexity.git

Notes:
- Experimental runtime may vary slightly depending on system performance.
- Repetition of the snippet in Java ensures smoother and more reliable measurements.
