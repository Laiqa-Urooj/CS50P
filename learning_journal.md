# 🧠 Programming Mistakes & Lessons

## CS50P Problem Set 0

### Functions

- `return` does not print automatically.
- A returned value must be stored or used.
- Functions should only take the parameters they need.

### Strings

- Strings are immutable.
- `replace()` returns a new string.
- `sep` works between multiple arguments to `print()`, not within a string.

### Python

- Not every function accepts keyword arguments.
- Read error messages carefully—they usually point to the problem.
- Spaces around operators is a good practice.

### Git
- Initialize Git in the project root.
- `git status` is the first command to run when unsure.

## CS50P Problem Set 1

### 💡 Key Learnings

- One function = one responsibility.
- `main()` handles input/output; helper functions process data.
- `return` gives a value back; `print()` only displays it.
- Parameter names can be anything; only the passed value matters.
- Use `in` instead of multiple `or` comparisons when checking several values.
- Prefer built-in string methods (`startswith()`, `endswith()`) over manual parsing when appropriate.
- `split()` returns a list; `split()` is generally better than `split(" ")` for user input.

### 🐞 Debugging Lessons

- Built-in functions like `float()` return new values; assign them back.
- Always check variable types when debugging (`type()`).
- Read error messages before changing code.
  
## CS50P Problem Set 2

### 💡 Key Learnings

- break down the problem into small steps before solving
-Think if there is need for loop or if built-in function is present
-Try to concise code and keep it readable avoid complexities
- Use helper functions for single responsibilities.
- Use Boolean flags to track program state.
- Use dictionaries for key–value lookups.
### 🐞 Debugging Lessons

-Solve a single problem than run and verify before moving to next subproblem
- Trace loops one iteration at a time.
- Test edge cases before finalizing.

## CS50P Problem Set 3

### 💡 Key Learnings

- Used `try`/`except` to handle invalid input gracefully.
- Used `while True` with `break` for input validation.
- Learned to use dictionaries for counting frequencies.
- Learned `sorted()` to iterate over dictionary keys alphabetically.
- Parsed and validated multiple input formats.

### 🐞 Debugging Lessons

- Place error-prone code inside the `try` block.
- Trace program flow to identify where exceptions occur.
- Break complex problems into smaller validation steps.