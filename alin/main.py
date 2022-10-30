import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('module3_2.db')

my_cursor = conn.cursor()

try:
    my_cursor.execute("""
    CREATE TABLE system_password(
    pass_id INTEGER primary key,
    sys_pass TEXT
    )""")

    my_cursor.execute("""
    create table login_history(
    login_id INTEGER primary key,
    login_time TEXT,
    armed_disarmed BLOB
    );""")

    my_cursor.execute("""create table camera_history(
    reg_id INTEGER primary key,
    start_time TEXT,
    end_time TEXT,
    duration_sec INTEGER,
    file_location TEXT,
    file_name TEXT
    );""")

    my_cursor.execute("""insert
    into
    system_password
    values(1, '002289');""")

    my_cursor.execute("""insert
    into
    login_history(login_id, login_time, armed_disarmed)
    values('1', '2022-08-01 12:08:05', true),
    ('2', '2022-08-02 15:03:07', false),
    ('3', '2022-08-03 12:08:05', true),
    ('4', '2022-08-05 15:08:07', false),
    ('5', '2022-08-07 11:08:05', true),
    ('6', '2022-08-08 12:03:07', false),
    ('7', '2022-08-09 17:08:05', true),
    ('8', '2022-08-11 15:03:07', false),
    ('9', '2022-08-12 22:08:05', true),
    ('10', '2022-08-15 15:03:07', false),
    ('11', '2022-08-19 23:08:05', true),
    ('12', '2022-08-21 15:03:07', false),
    ('13', '2022-08-23 10:08:05', true),
    ('14', '2022-08-27 15:03:07', false);""")

    my_cursor.execute("""insert
    into
    camera_history(reg_id, start_time, end_time, duration_sec, file_location, file_name)
    values
    ('1', '2022-08-03 15:03:07', '2022-08-03 15:05:00', 113, 'C:\\Users\\Alin-PC\\Desktop\\exam 3.2\\October',
     '1 2022-08-03 15:03:07.mp4')
    ;""")


except:
    pass

conn.commit()


class SecuritySystem:
    expression= ""
    def __init__(self):
        self.login_window()


    def login_window(self):
        self.root = Tk()
        self.root.title("Security System")
        self.root.config(width=600, height=600)
        canvas = Canvas(width=200, height=200)
        lock_img = PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=lock_img)
        canvas.grid(row=0, column=1)
        password_label = ttk.Label(text="Insert Pincode :", font=("Arial",30,"bold"))
        password_label.grid(row=1, column=1)

        self.password_entry = ttk.Entry(width=60)
        self.password_entry.grid(row=2, column=0, columnspan= 2)

        self.enter_button=Button(text="Enter", font=("Arial",15, "bold"), command=self.enter_func)
        self.enter_button.grid(row=2,column=2)

        button_7 =Button(text="7", font=("Arial",30,"bold"), padx=20)
        button_7.grid(row=3, column=0)

        button_8 = Button(text="8", font=("Arial",30,"bold"), padx=20)
        button_8.grid(row=3, column=1)

        button_9 = Button(text="9", font=("Arial",30,"bold"), padx=20)
        button_9.grid(row=3, column=2)

        button_4 = Button(text="4", font=("Arial",30,"bold"), padx=20)
        button_4.grid(row=4, column=0)

        button_5 = Button(text="5", font=("Arial",30,"bold"), padx=20)
        button_5.grid(row=4, column=1)

        button_6 = Button(text="6", font=("Arial",30,"bold"), padx=20)
        button_6.grid(row=4, column=2)

        button_1 = Button(text="1", font=("Arial",30,"bold"), padx=20)
        button_1.grid(row=5, column=0)

        button_2 = Button(text="2", font=("Arial",30,"bold"), padx=20)
        button_2.grid(row=5, column=1)

        button_3 = Button(text="3", font=("Arial",30,"bold"), padx=20)
        button_3.grid(row=5, column=2)
        self.root.mainloop()



    def get_db_password(self):
        get_password ="SELECT sys_pass FROM system_password WHERE pass_id=1;"
        my_cursor.execute(get_password)
        db_pass = my_cursor.fetchone()
        return db_pass[0]

    def enter_func(self):
        inserted_password = self.password_entry.get()
        if inserted_password == self.get_db_password():
            self.create_main_menu()
        else:
            messagebox.showerror(title="Error", message="Wrong password")

    def create_main_menu(self):

        self.main_menu = Toplevel()
        self.main_menu.title = "Security"
        self.main_menu.geometry("600x600")
        title = Label(self.main_menu, text="Security System", font=("Arial", 30, "bold"), padx=20, pady=20)
        title.grid(row=0, column=0)

        self.change_pass_button = Button(self.main_menu, text="Change Password", font=("Arial",20,"bold"), padx=20, pady=20, command=self.change_pass_window)
        self.change_pass_button.grid(row=1, column=0)

        self.history_button= Button(self.main_menu, text="Show History", font=("Arial",20,"bold"), padx=20, pady=20, command=self.history_tab)
        self.history_button.grid(row=2, column=0)

        self.arm_button= Button(self.main_menu, text="Arm System", font=("Arial",20,"bold"), padx=20, pady=20, command=self.arm_func)
        self.arm_button.grid(row=3, column=0)

    def arm_func(self):
        messagebox.showinfo(title="System Armed", message="System armed Successfully")
        self.main_menu.destroy()

    def change_pass_window(self):
        self.change_window = Toplevel(self.root)
        self.change_window.title("Change Password")
        self.change_window.geometry("400x200")

        self.current_pass_label = ttk.Label(self.change_window, text="Current password: ")
        self.current_pass_label.grid(row=0, column=0)

        self.current_pass_entry = Entry(self.change_window)
        self.current_pass_entry.grid(row=0, column=1)

        self.new_pass_label =ttk.Label(self.change_window, text="New password: ")
        self.new_pass_label.grid(row=1, column=0)

        self.new_pass_entry = Entry(self.change_window)
        self.new_pass_entry.grid(row=1, column=1)

        self.submit_button = Button(self.change_window, text="Submit", command=self.submit_new_pass)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def submit_new_pass(self):
        new_pass = self.new_pass_entry.get()
        current_pass = self.current_pass_entry.get()
        if current_pass == self.get_db_password():
            update_db = f"UPDATE system_password SET sys_pass = {new_pass} WHERE (`pass_id` = '1');"
            my_cursor.execute(update_db)
            conn.commit()
            messagebox.showinfo(title="Password changed", message="Password changed successfully")
            self.main_menu.destroy()

    def history_tab(self):
        self.history = Toplevel()
        self.history.title("Login History")

        self.login_history = Frame(self.history)
        self.login_history.grid(row=0, column=0)

        get_history = "SELECT * FROM login_history;"
        my_cursor.execute(get_history)
        db_history = my_cursor.fetchall()
        txt = ''
        for x in db_history:
            txt += f"{x}\n"
        history_label = ttk.Label(self.login_history,
                                  text=f"login id, login time, armed/disarmed\n{txt}")
        history_label.pack()

        self.recording_history = Frame(self.history)
        self.recording_history.grid(row=1,column=0)

        get_records = "SELECT * FROM camera_history;"
        my_cursor.execute(get_records)
        db_records = my_cursor.fetchall()
        lines=''
        for record in db_records:
            lines += f"{record[5]},{record[4]}"
        records_label= ttk.Label(self.recording_history,text=f"Name,                                       Location\n{lines}")
        records_label.pack()



if __name__ == '__main__':
    window = SecuritySystem()
