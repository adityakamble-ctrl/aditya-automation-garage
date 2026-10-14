# ============================================
# ASSIGNMENT 3: CONDITIONALS (if / elif / else)
# ============================================
#
# Goal: Practice decision-making logic with if/elif/else using QA-style
# test data — the kind of branching you'll use constantly when scripting
# checks on test results.
#
# Instructions:
# - Replace each TODO with your own code.
# - Run the file (python assignment_3_conditionals.py)
#   and check the output makes sense.


# ---- PART A: Basic if / else ----
# A test case either passes or fails. Report its status.

test_result = "fail"   # try changing this to "pass" and re-running

# TODO: If test_result is "pass", print "Test passed."
# Otherwise, print "Test failed."


# ---- PART B: if / elif / else chain ----
# QA teams often classify a build's pass percentage into a quality grade:
#   >= 95        -> "Excellent"
#   80 to 94.99  -> "Acceptable"
#   60 to 79.99  -> "Needs improvement"
#   below 60     -> "Not release-ready"

pass_percentage = 82.5   # try a few different values: 97, 88, 45

# TODO: Write an if/elif/else chain that assigns the correct grade
# string to a variable named build_grade, then print it.
# build_grade = ...


# ---- PART C: Combining conditions (and / or / not) ----
# A release is approved only if:
#   - pass_percentage is at least 90, AND
#   - there are zero critical_bugs

pass_percentage_2 = 92
critical_bugs = 0

# TODO: Use a single if/else (with 'and') to decide release approval.
# Print "Release approved." or "Release blocked." accordingly.


# ---- BONUS ----
# TODO: In one line, explain the difference between using "elif" versus
# writing multiple separate "if" statements for the grading logic in
# Part B. Why does it matter here?
#
# Your explanation:
