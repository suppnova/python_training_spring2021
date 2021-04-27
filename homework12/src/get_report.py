import csv

from homework12.src.task01 import create_session

with create_session() as session:
    stmt = """
            SELECT
            students.last_name, students.first_name, homework_results.created, teachers.last_name, teachers.first_name
            FROM homework_results
            JOIN students
            ON homework_results.author_id = students.id
            JOIN homeworks
            ON homework_results.homework_id = homeworks.id
            JOIN teachers
            ON homeworks.author_id = teachers.id
        """
    result_proxy = session.execute(stmt)
    results = result_proxy.fetchall()

    with open("report.csv", "w", newline="") as csv_file:
        fieldnames = [
            "student_last_name",
            "student_first_name",
            "creation_date",
            "teacher_last_name",
            "teacher_first_name",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({k: v for k, v in zip(fieldnames, result)})
