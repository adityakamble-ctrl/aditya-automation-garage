# ============================================
# ASSIGNMENT 4: LOOPS (for / while)
# ============================================
#
# Goal: Practice repeating work with for and while loops using QA-style
# test data — looping over test results is how you turn one check into
# a whole test run.
#
# Instructions:
# - Replace each TODO with your own code.
# - Run the file (python assignment_4_loops.py)
#   and compare your output with the "Expected" comments.


# ---- PART A: Looping over a list with for ----
# A list holds several values in order, inside square brackets.

test_cases = ["login", "logout", "search", "checkout", "profile"]

# TODO: Use a for loop to print each test case name with a prefix, e.g.
#   Running: login
#
# Expected (first two lines):
#   Running: login
#   Running: logout


# ---- PART B: Counting with a loop + if ----
# Combine a loop with what you learned in Assignment 3.

results = ["pass", "fail", "pass", "pass", "fail", "pass"]

# TODO: Start passed_count and failed_count at 0.
# Loop over results and add 1 to the right counter for each item.
# Then print both counts with labels.
#
# Expected:
#   Passed: 4 Failed: 2


# ---- PART C: Using range() ----
# range(1, 6) gives the numbers 1, 2, 3, 4, 5 (the end value is excluded).

# TODO: Use a for loop with range() to print 5 test run numbers, e.g.
#   Test run #1
#   ...
#   Test run #5


# ---- PART D: while loop (retry logic) ----
# Flaky tests are often retried a few times before being marked failed.

max_retries = 3
attempt = 1
test_passed = False   # pretend the test only passes on the 3rd attempt

# TODO: Write a while loop that keeps going while attempt <= max_retries
# and test_passed is False. Inside the loop:
#   - print "Attempt", attempt
#   - if attempt == 3, set test_passed = True
#   - add 1 to attempt  (forgetting this makes the loop run forever!)
# After the loop, print "Test passed after retries." or
# "Test failed after all retries." depending on test_passed.
#
# Expected:
#   Attempt 1
#   Attempt 2
#   Attempt 3
#   Test passed after retries.
#
# Then try changing the pass condition to attempt == 5 and re-run.


# ---- BONUS ----
# TODO: Loop over results (from Part B) and stop at the first "fail"
# using break. Print the position of that first failure.
# Hint: keep your own counter, starting at 1, or look up enumerate().
#
# Expected:
#   First failure at test 2
#
# In one line, when would you pick a while loop over a for loop?
#
# Your explanation:
