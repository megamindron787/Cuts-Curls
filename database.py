import sqlite3



def appointment():
    conn = sqlite3.connect('appointment.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS appointments(
                name TEXT,
                email TEXT,
                mobile TEXT,
                gender TEXT,
                service TEXT,
                date TEXT,
                time TEXT                                            
                )""")
    conn.commit()
    conn.close()



    
    
    