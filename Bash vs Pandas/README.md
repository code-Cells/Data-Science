### Purpose
It was intended to show Python Pandas Library and default Bash commands regarding simple slicing of a data file, also presenting to users unfamiliar to any of the techniques an alternative.

### Data file
The target data csv file for this demonstration (**signals.csv**) is a list of Linux signals scraped from https://www.computerhope.com/unix/signals.htm using Python's Beautiful Soup.

### Results
The main difference would be the execution time of both languages, as shown in the table below.

| Time | Bash(s) | Python(s) | Ratio |
| ---- | ---- | ------ | ----- |
| Real | 0,0126	| 0,659	| 52,3 |
| User | 0,0108	| 0,588	| 54,4 |
| Sys  | 0,007	| 0,062 |	9    |

The data presented comes from the means of 5 Bash and Python's code execution, discarding the first one, where there were outlier time measurements due to caching.
Given these results, Bash code, for the scripts in question, executed basically 50 times faster. But it should be taken in consideration that either mean values must seen almost irrelevant to the user **in this example**. If used for large data files or in a production environment, this may not be the case.   
