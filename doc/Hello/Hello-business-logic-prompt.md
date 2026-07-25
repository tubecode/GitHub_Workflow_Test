### Business Logic Summary
The script calculates academic performance metrics for a group of students. It processes individual test scores to compute each student's average score, displays a summary report, and identifies the top-performing student.

---

### Main Operations
1. **Average Calculation:** Computes the arithmetic mean for a given set of numeric scores.
2. **Per-Student Score Processing:** Iterates through student records, calculates each student's average grade, and formats the output to two decimal places.
3. **Top Performer Identification:** Evaluates all calculated averages to determine which student achieved the highest overall average score.

---

### How the Code Works
1. **Defines Helper Function:** The `calculate_average` function takes a list of numbers, sums them, and divides by the count of numbers.
2. **Stores Data:** A dictionary (`students`) maps student names to their respective list of test scores.
3. **Generates Report:** A `for` loop iterates through the dictionary, calls `calculate_average` for each student's score list, and prints the student's name alongside their average score.
4. **Finds Maximum Average:** The `max()` function utilizes a key lambda function to evaluate every student's average via `calculate_average`, identifying and printing the name of the highest performer.