# ============================================
# ASSIGNMENT 2: OPERATORS & TYPE CONVERSION
# ============================================
#
# Goal: Practice arithmetic/comparison operators and converting between
# data types (str, int, float) using QA-style test data.
#
# Instructions:
# - Replace each TODO with your own code.
# - Run the file (python assignment_2_operators_and_type_conversion.py)
#   and check the output makes sense.


# ---- PART A: Arithmetic operators ----

# TODO: Create two variables, total_tests and failed_tests, with sample values.
# total_tests = ...
# failed_tests = ...

# TODO: Calculate passed_tests using total_tests and failed_tests.
# passed_tests = ...

# TODO: Calculate pass_percentage as a percentage (float).
# Hint: (passed_tests / total_tests) * 100
# pass_percentage = ...

# TODO: Print all four values with labels, e.g.
# print("Total:", total_tests, "Passed:", passed_tests, "Failed:", failed_tests, "Pass %:", pass_percentage)


# ---- PART B: Comparison operators ----

# TODO: Set a variable pass_threshold = 90
# (the minimum pass percentage required to approve a release)

# TODO: Use a comparison operator to check if pass_percentage meets or
# exceeds pass_threshold. The result should be True or False.
# is_release_ready = ...

# TODO: Print is_release_ready


# ---- PART C: Type conversion ----
# Test data often arrives as text (e.g. from a config file, CLI argument, or CSV).

test_count_str = "150"
duration_str = "12.5"

# TODO: Convert test_count_str to an integer.
# test_count_int = ...

# TODO: Convert duration_str to a float.
# duration_seconds = ...

# TODO: Build a single sentence combining both converted values, e.g.
# "Executed 150 test cases in 12.5 seconds"
# summary = ...
# print(summary)


# ---- BONUS ----
# TODO: Try running int("12.5") in a separate line (or in the Python shell).
# It will raise an error. Write one line below explaining, in your own words,
# why int() fails on that string but float() does not.
#
# Your explanation:
