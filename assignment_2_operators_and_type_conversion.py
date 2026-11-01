
# ============================================
# ASSIGNMENT 2: OPERATORS & TYPE CONVERSION
# ============================================

# ---- PART A: Basic calculations ----

total_tests = 100
failed_tests = 15

# Calculate passed tests
passed_tests = total_tests - failed_tests

print("Total tests:", total_tests)
print("Failed tests:", failed_tests)
print("Passed tests:", passed_tests)


# ---- PART B: Calculate pass percentage ----

pass_percentage = (passed_tests / total_tests) * 100

print("Pass percentage:", pass_percentage)


# ---- PART C: Comparison operators ----

pass_threshold = 80

is_release_ready = pass_percentage >= pass_threshold

print("Release ready:", is_release_ready)


# ---- PART D: Type conversion ----

# Convert float into integer
pass_percentage_int = int(pass_percentage)

print("Pass percentage as integer:", pass_percentage_int)
print("Pass percentage type:", type(pass_percentage_int))

# Convert string into integer
failed_count_text = "12"

failed_count = int(failed_count_text)

print("Failed count:", failed_count)
print("Failed count type:", type(failed_count))

# Convert string into float
pass_rate_text = "87.5"

pass_rate = float(pass_rate_text)

print("Pass rate:", pass_rate)
print("Pass rate type:", type(pass_rate))


# ---- PART E: Release decision ----

if is_release_ready:
    print("Release approved.")
else:
    print("Release blocked.")


# ---- PART F: QA execution summary ----



print(f"Total tests: {total_tests}")
print(f"Passed tests: {passed_tests}")
print(f"Failed tests: {failed_tests}")
print(f"Pass percentage: {pass_percentage}%")
print(f"Release status: {'Approved' if is_release_ready else 'Blocked'}")



