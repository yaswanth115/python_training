def student_result(name, **subjects):
    total = sum(subjects.values())
    average = total / len(subjects)

    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)

    # Assuming 40 marks is the pass mark
    passed = all(mark >= 40 for mark in subjects.values())

    print("Name:", name)
    print("Total Marks:", total)
    print("Average:", average)
    print("Highest Scoring Subject:", highest_subject)
    print("Lowest Scoring Subject:", lowest_subject)

    if passed:
        print("Result: Pass")
    else:
        print("Result: Fail")


student_result(
    "Rahul",
    Python=85,
    SQL=72,
    AWS=91,
    Airflow=68
)