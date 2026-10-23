# ============================================
# ASSIGNMENT 5: LISTS & DICTIONARIES
# ============================================
#
# Goal: Practice storing and organizing test data in lists and
# dictionaries — the structures you'll use to hold test cases, results
# and bug reports in real automation scripts.
#
# Instructions:
# - Replace each TODO with your own code.
# - Run the file (python assignment_5_lists_and_dictionaries.py)
#   and compare your output with the "Expected" comments.


# ---- PART A: Working with lists ----
# Lists are ordered. Positions (indexes) start at 0, and -1 is the last item.

test_cases = ["login", "logout", "search"]

# TODO: Add "checkout" to the end of test_cases using .append().
# Then print the list and its length using len().
#
# Expected:
#   ['login', 'logout', 'search', 'checkout']
#   Total test cases: 4

# TODO: Print the first and the last test case using indexes.
#
# Expected:
#   First: login
#   Last: checkout

# TODO: Use the "in" keyword with an if/else to check whether "payment"
# is in test_cases. Print "payment is covered." or
# "payment is not covered yet."
#
# Expected:
#   payment is not covered yet.


# ---- PART B: Dictionary basics ----
# A dictionary stores key: value pairs, so you look values up by name.

test_run = {"tester": "Aditya", "total": 50, "passed": 46, "failed": 4}

# TODO: Print the tester's name and the number of passed tests by
# looking them up with their keys, e.g. test_run["tester"].
#
# Expected:
#   Tester: Aditya Passed: 46

# TODO: Add a new key "build" with the value "v2.3", then print the
# whole dictionary.
#
# Expected:
#   {'tester': 'Aditya', 'total': 50, 'passed': 46, 'failed': 4, 'build': 'v2.3'}


# ---- PART C: Looping over a dictionary ----

bug_counts = {"login": 0, "search": 2, "checkout": 5, "profile": 1}

# TODO: Loop over bug_counts.items() to print each module and its bug
# count, and add up the total number of bugs. Print the total at the end.
# Hint: for module, count in bug_counts.items():
#
# Expected:
#   login: 0 bug(s)
#   search: 2 bug(s)
#   checkout: 5 bug(s)
#   profile: 1 bug(s)
#   Total bugs: 8


# ---- PART D: Building a summary dictionary ----
# Turn a raw list of results into a count per status.

results = ["pass", "fail", "pass", "skip", "pass", "fail"]

# TODO: Start with an empty dictionary: summary = {}
# Loop over results. If the status is already a key in summary, add 1
# to it; otherwise set it to 1. Print summary at the end.
#
# Expected:
#   {'pass': 3, 'fail': 2, 'skip': 1}
#
# Then try adding "blocked" to results and re-run. You shouldn't need
# to change your loop.


# ---- BONUS ----
# TODO: Using bug_counts from Part C, find the module with the most
# bugs by looping and keeping track of the highest count so far.
#
# Expected:
#   Most bugs: checkout (5)
#
# In one line, when would you store test data in a dictionary instead
# of a list?
#
# Your explanation:
