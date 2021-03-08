import sqlite3

try:
    db = sqlite3.connect("skill_jobs_students.db")
    if db:
        print("Database created successfully")
    else:
        print("Database not created")

    # student table = id, name, course_name, start_data, start_time_schedule
    sql = "CREATE TABLE student(id int auto increment primary key," \
          " stu_name text, course_name text, start_date_schedule text, end_date_schedule text)"

    exist_table_exception = "DROP TABLE if exists student"
    db.execute(exist_table_exception)

    table_create = db.execute(sql)
    if table_create:
        print("student table created")
    else:
        print("Table is not created")

    data1 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (0, 'Mahadi Hasan', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    data2 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (1, 'Warid Hasan', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    data3 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (2, 'Sourav Roy', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    data4 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (3, 'Abdul Manna', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    data5 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (4, 'Anjal Paul', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    data6 = "INSERT INTO student(id, stu_name, course_name, start_date_schedule, end_date_schedule)" \
           "values (5, 'Abdul Mannan', 'Full Stack web Dev with react', '29/01/2021', '29/05/2021')"

    student_insert = [data1, data2, data3, data4, data5, data6]
    for i in student_insert:
        db.execute(i)
        print("value inserted")
    else:
        print("Value not inserted")

    # db.execute(data2)
    # db.execute(data3)
    # db.execute(data4)
    # db.execute(data5)

    # if student_insert:
    #     print("value inserted")
    # else:
    #     print("Value not inserted")

    db.commit()

    get_data = "SELECT id, stu_name, course_name FROM student order by id desc"

    show_data = db.execute(get_data)

    if show_data:
        print("-" * 1 + "id" + "-" * 5 + "Name" + "-" * 10 + "Course Name"+"-"*10)
        for i in show_data:
            print('-'*60)
            print("|",i,"|")
            print('-' * 60)
    else:
        print("There is no data in the student table")
except Exception as e:
    print(e)
