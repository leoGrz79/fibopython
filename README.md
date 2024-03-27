# FIBOPYTHON
A Fibonacci approach written in Python

## Stacks
- Python
## Project description
<p>
This small project consists of 3 functions as follow:
<details>
<summary>
<strong>fibonacci_up_to</strong>
</summary>
<p>Given an integer > 0 as an argument, generates a Fibonacci sequence up to a given limit number.</p>
<p>i.e. if the user inputs <code>35</code>, the function will generate the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34</p>
</details>

<details>
<summary>
<strong>fibonacci_classic</strong>
</summary>
<p>Given an integer > 0 as an argument, generates a Fibonacci sequence with x numbers</p>
<p>i.e. if the user inputs <code>15</code>, the function will generate the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377</p>
</details>

<details>
<summary>
<strong>fibonacci_ranged</strong>
</summary>
<p>Given two integers > 0 as arguments, generates a Fibonacci sequence between both given numbers, starting from the first argument up to the last argument.</p>
<p>i.e. if the user inputs <code>8, 30</code>, the function will generate the Fibonacci sequence: 8, 13, 21</p>
As well as, if the first argument is <strong><i>NOT</i></strong> a valid Fibonacci number, the function throws a message and will generate from the next valid Fibonacci number.
</details>

</p>


## Requirements
Python 3.8 or higher

## Getting started
* Clone the repository
```
git clone <git template url> <project_name>
In this case: git clone git@github.com:leoGrz79/fibopython.git
```

* Run
```
python3 fibopython.py
```
## To-do
- Refactor
- Fix some bugs (functions are still accepting integers < 0 )
- Unit tests
