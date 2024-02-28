from tkinter import *
from tkinter import messagebox  # Import the messagebox module
from PIL import ImageTk
import mysql.connector


def saveData():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="customerdata"
    )

    mycursor = conn.cursor()
    sql = "INSERT INTO student_reg (username, email, password) VALUES (%s, %s, %s)"

    


    username_value = usernameEntry.get()
    email_value = emailEntry.get()
    password_value = passwordEntry.get()

    # Execute the SQL query with the values
    mycursor.execute(sql, (username_value, email_value, password_value))

    conn.commit()

    # Display a success message box
    messagebox.showinfo("Success", "Data inserted successfully!")


# Create the main window
window = Tk()
window.title("My App")

# Set up the background image
background_image = ImageTk.PhotoImage(file='doraemon.jpg')
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a frame for other widgets
frame = Frame(window, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n')

# Create labels and entry widgets
usernameLabel = Label(frame, text="Username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
usernameLabel.grid(row=0, column=0, padx=10, pady=5)

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="Email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
emailLabel.grid(row=1, column=0)

emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="Password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
passwordLabel.grid(row=2, column=0, padx=10, pady=5)

passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=2, column=1)

submitButton = Button(frame, text="Submit", command=saveData)
submitButton.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()
