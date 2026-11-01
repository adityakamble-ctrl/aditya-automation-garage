
test_result = "pass"   

if test_result == "pass":
    print("Test passed.")
else:
    print("Test failed.")


pass_percentage = 82.5   

if pass_percentage >= 95:
    build_grade = "Excellent"
elif pass_percentage >= 80:
    build_grade = "Acceptable"
elif pass_percentage >= 60:
    build_grade = "Needs improvement"
else:
    build_grade = "Not release-ready"

print(build_grade)

pass_percentage_2 = 92
critical_bugs = 0

if pass_percentage_2 >= 90 and critical_bugs == 0:
    print("Release approved.")
else:
    print("Release blocked.")



