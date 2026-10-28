#
# ============================================
# ASSIGNMENT 2: OPERATORS AND TYPE CONVERSION
# ============================================

# ---- PART A: Variables and arithmetic ----

# Create two variables with sample values.
total_tests = 100
failed_tests = 15

# Calculate the number of passed tests.
passed_tests = total_tests - failed_tests

print("Total tests:", total_tests)
print("Failed tests:", failed_tests)
print("Passed tests:", passed_tests)


# ---- PART B: Calculate pass percentage ----

# Calculate the percentage of tests that passed.
pass_percentage = (passed_tests / total_tests) * 100

print("Pass percentage:", pass_percentage)


# ---- PART C: Comparison operator ----

# Set the minimum pass percentage required for release.
pass_threshold = 80

# Check whether the pass percentage meets the threshold.
is_release_ready = pass_percentage >= pass_threshold

print("Release ready:", is_release_ready)


# ---- PART D: Type conversion ----

# Convert the pass percentage to an integer.
pass_percentage_int = int(pass_percentage)

print("Pass percentage as integer:", pass_percentage_int)
print("Pass percentage type:", type(pass_percentage_int))


# ---- BONUS: Release decision ----

if is_release_ready:
    print("Release approved.")
else:
    print("Release blocked.")
