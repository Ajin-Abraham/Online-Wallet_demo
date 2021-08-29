import psycopg2
from tkinter import messagebox


def registerDb(username, email, age, ph, password):
    try:
        db_name = "euwpundj"
        db_user = "euwpundj"
        db_pass = "7qn7J2u4TvroHViI889U2pMnOopIr1S1"
        db_host = "rosie.db.elephantsql.com"
        db_port = "5432"
        conn = psycopg2.connect(database=db_name,
                                user=db_user,
                                password=db_pass,
                                host=db_host,
                                port=db_port
                                )
        cur = conn.cursor()
        cur.execute(
            "insert into details(username,email,age,ph,password) values (%s,%s,%s,%s,%s);", (username, email, age, ph, password))
        conn.commit()
        cur.close()
        conn.close()
        print("done")
        return 1

    except Exception as e:
        messagebox.showerror("Error", "Database Error ")
