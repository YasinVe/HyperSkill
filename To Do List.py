import sqlite3 as sql
from datetime import date, datetime, timedelta

menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
""".strip().lower()

def create_database():
    conn = sql.connect("todo.db")
    data = conn.cursor()
    data.execute(f"""CREATE TABLE IF NOT EXISTS task
        (
        id INTEGER PRIMARY KEY,
        task VARCHAR,
        deadline DATE DEFAULT({date.today()})
        )""")
create_database()




def add_task(task,deadline):
    conn = sql.connect("todo.db")
    data = conn.cursor()
    data.execute("""
    INSERT INTO task (task,deadline) VALUES(?,?)""",
                 (task, date(*deadline))
                 )
    data.close()
    conn.commit()
    print("The task has been added!")

def delete_task(id):
    conn = sql.connect("todo.db")
    data = conn.cursor()
    data.execute(f"DELETE FROM task WHERE id='{id}'")
    data.close()
    conn.commit()

def print_task(veri):
    for _, k in enumerate(veri, 1):
        today = date(*(int(_) for _ in k [2].split("-")))
        print(str(_) + ".", k [1] + ".", str(today.day).rjust(2, '0'), today.strftime("%b"))
    print()


def show_weeks_task():
    conn = sql.connect("todo.db")
    data = conn.cursor()
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(0, 7):
        today = date.today() + timedelta(days=i)
        data.execute(f"""SELECT task,deadline FROM task WHERE deadline='{date.today()+timedelta(days=i)}'""")
        veri = data.fetchall()
        print(weekday[today.weekday()], today.day, today.strftime("%b")+':')
        if veri:
            for _, k in enumerate(veri, 1):
                print(str(_) + ".", k[0])
            print()
        else:
            print("Nothing to do!\n")
    data.close()
    conn.commit()

def show_all_task(query):
    conn = sql.connect("todo.db")
    data = conn.cursor()
    data.execute(query)
    return data.fetchall()


def show_missed_task():
    veri=show_all_task(f"SELECT * FROM task WHERE deadline<'{date.today}'")
    if veri:
        print("Missed tasks:")
        return veri
    else:
        return "Nothing is missed!"


def show_todays_task():
    conn = sql.connect("todo.db")
    data = conn.cursor()
    data.execute(f"""SELECT task FROM task WHERE deadline='{date.today}'""")
    veri = data.fetchall()
    print("Today:")
    if veri:
        for i, k in enumerate(veri, 1):
            print(str(i) + '.', *k)
        print()
    else:
        print("Nothing to do!\n")


while True:
    print(menu)
    ask = input()
    if ask == "1":
        show_todays_task()
    elif ask == '2':
        show_weeks_task()
    elif ask == '3':
        veri=show_all_task("""SELECT * FROM task ORDER BY deadline ASC""")
        print("All tasks:")
        print_task(veri)
    elif ask == '4':
        print_task(show_missed_task())
    elif ask == '5':
        task = input("Enter task\n")
        deadline = (int(i) for i in input("Enter deadline\n").split("-"))
        add_task(task, deadline)
    elif ask == '6':
        print("Choose the number of the task you want to delete:")
        veri = show_all_task("""SELECT * FROM task ORDER BY deadline ASC""")
        print_task(veri)
        delete_task(veri[int(input())-1][0])
    else:
        print("\nBye!")
        break
