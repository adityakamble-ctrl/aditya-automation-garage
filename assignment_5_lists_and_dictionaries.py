test_cases = ["login", "logout", "search"]

test_cases.append("checkout")
test_cases.append("payment")
print(test_cases)

print("Total test cases:", len(test_cases))

print("First:", test_cases[0])
print("Last:", test_cases[-1])

if "refund" in test_cases:
    print("refund is covered.")
else:
    print("refund is not covered yet.")

    test_run = {
    "tester": "Aditya",
    "total": 50,
    "passed": 46,
    "failed": 4
}
print(test_run["tester"])
print(test_run["passed"])

bug_counts = {
    "login": 0,
    "search": 2,
    "checkout": 5,
    "profile": 1
}

highest_count = -1
most_bugs_module = ""

for module, count in bug_counts.items():
    if count > highest_count:
        highest_count = count
        most_bugs_module = module
print(f"Most bugs: {most_bugs_module} ({highest_count})")

for module, count in bug_counts.items():
    print(module, count)

    total_bugs = 0

for module, count in bug_counts.items():
    print(f"{module}: {count} bug(s)")
    total_bugs += count

print("Total bugs:", total_bugs)

results = ["pass", "fail", "pass", "skip", "pass", "fail", "blocked"]

summary = {}

for status in results:
    if status in summary:
        summary[status] += 1
    else:
        summary[status] = 1
print(summary)

results.append("blocked")

summary = {}

for status in results:
    if status in summary:
        summary[status] += 1
    else:
        summary[status] = 1

print("Updated summary:", summary)


highest_count = -1
most_bugs_module = ""

for module, count in bug_counts.items():
    if count > highest_count:
        highest_count = count
        most_bugs_module = module

print(f"Most bugs: {most_bugs_module} ({highest_count})")


# Your explanation:
# I would use a dictionary when I want to store data
# as key-value pairs and access values using their keys.


