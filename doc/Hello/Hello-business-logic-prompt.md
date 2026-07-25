### Business Logic Summary
The script calculates individual average scores for a set of students, reports those averages, and identifies the overall top-performing student based on their calculated average score.

---

### Main Operations
1. **Average Calculation**: Computes the arithmetic mean of a given list of numerical scores.
2. **Score Reporting**: Iterates through student records to compute and display each student's name alongside their average score (formatted to two decimal places).
3. **Top Performer Identification**: Evaluates all students to find and print the student with the highest average score.

---

### How the Code Works
1. **`calculate_average` Function**: Takes a list of numerical values and returns the sum divided by the total count (`sum / length`).
2. **Data Source**: Stores student names as keys and lists of test scores as values in a Python dictionary (`students`).
3. **Display Averages**: Loops through the dictionary entries, calls `calculate_average` for each student's scores, and prints the result.
4. **Determine Top Student**: Uses the built-in `max()` function with a custom lambda key (which computes each student's average score) to extract the name of the top-performing student and print it.