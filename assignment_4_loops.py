# ============================================
# ASSIGNMENT 4: LOOPS (for / while)
# ============================================



test_cases = ["login", "logout", "search", "checkout", "profile"]

for test_case in test_cases:
    print("Running:", test_case)

results = ["pass", "fail", "pass", "pass", "fail", "fail", "pass", "pass", "blocker", "pass", "skip"]

passed_count = 0
failed_count = 0
blocked_count = 0
skiped_count = 0

for result in results:
    if result == "pass":
        passed_count += 1
    elif result == "fail":
        failed_count += 1
    elif result == "blocker":
        blocked_count += 1
    elif result == "skip":
        skiped_count += 1    

print("Passed:", passed_count, "Failed:", failed_count, "Blocker:", blocked_count, "Skiped:", skiped_count)

for run_number in range(1, 6):
    print("Test run =", run_number)



max_retries = 4
attempt = 1
test_passed = False

while attempt <= max_retries and test_passed is False:
    print("Attempt", attempt)

    if attempt == 5:
        test_passed = True

    attempt += 1

if test_passed:
    print("Test passed after retries.")
else:
    print("Test failed after all retries.")

         








#
# In one line, when would you pick a while loop over a for loop?
#
# Your explanation:
