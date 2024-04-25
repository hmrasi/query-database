import sqlite3

conn = sqlite3.connect("database_example.db")
cursor = conn.cursor()

# table = """
#     create table student_info(student_name varchar(25),
#                                 class varchar(25),
#                                 section varchar(25));
# """

# cursor.execute(table)

# cursor.execute('''Insert into student_info values('Harish', 'Data Science', 'A')''')
# cursor.execute('''Insert into student_info values('MR', 'Data Science', 'A')''')
# cursor.execute('''Insert into student_info values('Jag', 'Data Science', 'A')''')
# cursor.execute('''Insert into student_info values('Deg', 'Data Science', 'A')''')
# cursor.execute('''Insert into student_info values('Sai', 'Data Science', 'A')''')

# print("records inserted ")
data = cursor.execute('''select * from student_info;''')
print(data.fetchall())
# for i in data:
#     print(i)
    

conn.commit()
conn.close()
