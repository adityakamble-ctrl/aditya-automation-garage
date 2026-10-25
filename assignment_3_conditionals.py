#
# ASSIGNMENT 3: CONDITIONALS (if / elif / else)

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
test_result = "pass"   # try changing this to "fail" and re-running

# If test_result is "pass", print "Test passed." Otherwise, print "Test failed."
if test_result == "pass":
    print("Test passed.")
else:
    print("Test failed.")


# ---- PART B: if / elif / else chain ----
# QA teams often classify a build's pass percentage into a quality grade:
#   >= 95        -> "Excellent"
#   80 to 94.99  -> "Acceptable"
#   60 to 79.99  -> "Needs improvement"
#   below 60     -> "Not release-ready"

pass_percentage = 82.5   # try a few different values: 97, 88, 45

# Assign the correct grade to build_grade and print it.
if pass_percentage >= 95:
    build_grade = "Excellent"
elif pass_percentage >= 80:
    build_grade = "Acceptable"
elif pass_percentage >= 60:
    build_grade = "Needs improvement"
else:
    build_grade = "Not release-ready"

print(build_grade)


# ---- PART C: Combining conditions (and / or / not) ----
# A release is approved only if:
#   - pass_percentage is at least 90, AND
#   - there are zero critical_bugs

pass_percentage_2 = 92
critical_bugs = 0

# Use a single if/else (with 'and') to decide release approval.
if pass_percentage_2 >= 90 and critical_bugs == 0:
    print("Release approved.")
else:
    print("Release blocked.")


# ---- BONUS ----
# elif checks the next condition only when the previous condition is false,
# and only the first matching block runs. Separate if statements are checked
# independently, so multiple blocks may execute. This matters here because we
# want exactly one grade assigned to each build.
