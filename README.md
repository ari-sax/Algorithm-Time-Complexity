# Project 1: Time Complexity Analysis of Nested Loops

**Author:** Aryan Saxena  
**Purpose:** Analyze the time complexity of a nested while-loop algorithm both theoretically and experimentally. Compare the experimental runtime with the theoretical estimate and visualize the results.

---

## Files Included

### 1. ComplexityExperiment.java
- Java program that implements the nested while-loops.  
- Measures runtime for a range of input sizes (`n`), repeating the snippet multiple times for smoother, more reliable measurements.  
- Prints the experimental runtime in nanoseconds for each input size.

### 2. plot_results.py
- Python script used to visualize the experimental Java results.  
- Computes theoretical values proportional to ((log log n)^2) and scales them to match experimental magnitudes.  
- Produces a log-log plot comparing experimental vs. adjusted theoretical runtime.

---

## How to Run

### Java Program

1. Compile the Java file:
   ```bash
   javac ComplexityExperiment.java
   ```

2. Run the program:
   ```bash
   java ComplexityExperiment
   ```

3. Output:
- Prints experimental runtime for each value of `n` in nanoseconds.

---

### Python Plot

1. Ensure Python 3 and matplotlib are installed.  
2. Run the script:
   ```bash
   python plot_results.py
   ```
3. Output:
- A log-log plot showing experimental vs. adjusted theoretical runtime.

---

## Purpose of This Project

### Theoretical Analysis
- Outer loop: O(log log n)  
- Inner loop: O(log log n)  
- Overall complexity: O((log log n)^2)

### Experimental Validation
- Measures true execution time for increasing values of `n`.  
- Computes theoretical values manually using the ((log log n)^2) formula.  
- Adjusts (scales) theoretical values to match experimental scale for direct comparison.  
- Confirms that experimental growth follows the predicted theoretical trend.

---

## Conclusions
- The theoretical analysis predicted a time complexity of O((log log n)^2).  
- Experimental results strongly validate the theoretical prediction.  
- The adjusted theoretical curve closely follows the experimental results on a log-log scale.  
- Minor fluctuations in runtime occur due to hardware, OS scheduling, and JVM warm-up, which is normal for micro-benchmarks.

---

## GitHub Code Repository

The Java and Python files for this project are available at:  
https://github.com/ari-sax/Algorithm-Time-Complexity.git

---

## Notes
- Runtime measurements may vary depending on system performance and background activity.  
- Loop repetition inside the Java code helps reduce noise and produce more stable timing results.