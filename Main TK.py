from tkinter import *
import tkinter as tk
from tkinter import messagebox

def verify():
    emailad = contact_entry.get()
    page = pageno_entry.get()
    count = 0

    if len(name_entry.get()) < 1:
        tk.Label(window, text="Required*", fg='red').grid(row=12, column=1, sticky=W)
        messagebox.showerror("NameError", "Enter a name (1 character or more)")
        count = count - 1
    if emailad.find("@") < 0:
        tk.Label(window, text="Required*", fg='red').grid(row=13, column=1, sticky=W)
        messagebox.showerror("EmailError", "Email format is incorrect (@ is missing)")
        count = count - 1
    if len(isbn_entry.get()) < 10:
        tk.Label(window, text="Required*", fg='red').grid(row=15, column=1, sticky=W)
        messagebox.showerror("ISBNError", "Enter exactly 10 digits")
        count = count - 1
    if not page.isdigit():
        tk.Label(window, text="Required*", fg='red').grid(row=16, column=1, sticky=W)
        messagebox.showerror("Page_Num_Error", "Page number should include numbers (only)")
        count = count - 1

    if count == 0:
        output_all_info()


def output_all_info():
    global ans
    price = 0
    undercoat = 0
    output.delete(0.0, END)
    under = undervar.get()

    output.insert('1.0', '###################################')

    output.insert('2.0', 'Name: ')
    output.insert('2.0', name_entry.get())
    output.insert(tk.END, '\n')

    output.insert('3.0', 'Email: ')
    output.insert("3.0", contact_entry.get())
    output.insert(tk.END, '\n')

    output.insert('4.0', 'ISBN: ')
    output.insert("4.0", isbn_entry.get())
    output.insert(tk.END, '\n')

    output.insert('5.0', 'Page Number: ')
    output.insert("5.0", pageno_entry.get())
    output.insert(tk.END, '\n')

    output.insert('6.0', '-----------------------------------')

    output.insert(tk.END, '\n')
    output.insert("7.0", 'Room Area: ')
    output.insert("7.0", ans)
    output.insert("7.0", ' M² ')
    output.insert(tk.END, '\n')
    paint_quality = paint_choice.get()

    if paint_quality == 1:
        price = ans * 1.75
        output.insert('8.0', 'Paint: Luxury        + £')
        output.insert('8.0', '')
        output.insert('8.0', price)
        output.insert(tk.END, '\n')


    elif paint_quality == 2:
        price = ans * 1
        output.insert('9.0', 'Paint: ')
        output.insert('9.0', 'Standard      + £')
        output.insert('9.0', price)
        output.insert(tk.END, '\n')


    elif paint_quality == 3:
        price = ans * 0.45
        output.insert('10.0', 'Paint: ')
        output.insert('10.0', 'Eco           + £')
        output.insert('10.0', price)
        output.insert(tk.END, '\n')

    if under == 1:
        undercoat = ans * 0.5
        output.insert('11.0', 'Undercoat: ')
        output.insert('11.0', 'Yes       + £')
        output.insert("11.0", undercoat)
        output.insert(tk.END, '\n')
    else:
        output.insert('11.0', 'Undercoat: ')
        output.insert('11.0', 'No        + £0 .00')
        output.insert(tk.END, '\n')
    if price > 0:
        overall = undercoat + price
        output.insert('12.0', 'Total:                 £')
        output.insert('12.0', overall)
        output.insert(tk.END, '\n')

    output.insert('13.0',
                  '###################################')


def total_area():
    global ans
    tk.Label(window, text="").grid(row=8, column=1)
    height = height_entry.get()
    length = length_entry.get()
    try:
        height_num = float(height)
        length_num = float(length)
    except:
        messagebox.showerror("HeightError", "Height & Length should only have numeric values")

    else:
        ans = height_num * length_num

        if height_num < 2 or height_num > 6:
            tk.Label(window, text="Enter a  number between 2 and 6", fg='red').grid(row=7, column=1, sticky=E)

        if length_num < 1 or length_num > 25:
            tk.Label(window, text="Enter a  number between 1 and 25", fg='red').grid(row=8, column=1, sticky=E)
        else:
            area_output.configure(state="normal")
            area_output.delete(0.0, END)
            area_output.insert('1.0', ans)
            area_output.configure(state="disabled")
        return ans


window = Tk()
window.geometry("450x620")
window.title("Paint Cost Calculator")
window.configure(bg='#3C84F4')

undervar = IntVar()
length_number = DoubleVar()
paint_choice = IntVar()
paint_choice.set(2)

tk.Label(window, text="Select a paint type (Undercoat is optional) ", bg="#3C84F4", font=('bold')).grid(row=0, column=0,
                                                                                                        ipady=10)

Radiobutton(window, text="Luxury (£1.75/M²)", bg='#3C84F4', variable=paint_choice, value=1).grid(row=1, column=0,
                                                                                                 sticky=W)

Radiobutton(window, text="Standard (£1.00/M²)", bg='#3C84F4', variable=paint_choice, value=2).grid(row=2, column=0,
                                                                                                   sticky=W)

Radiobutton(window, text="Economy (£0.45/M²)", bg='#3C84F4', variable=paint_choice, value=3).grid(row=3, column=0,
                                                                                                  sticky=W)

undercoat = tk.Checkbutton(window, text="Undercoat (£0.50/M²)", bg='#3C84F4', variable=undervar).grid(row=5, column=0,
                                                                                                      sticky=W)

tk.Label(window, text="Enter Room Dimensions (Meters)", bg="#3C84F4", font=('bold')).grid(row=6, column=0, ipady=10,
                                                                                          sticky=W)


tk.Label(window, text="Height", bg='#3C84F4').grid(row=7, column=0, sticky=W)
height_entry = Entry(window, width=4)
height_entry.grid(row=7, column=0, sticky=S)
height_entry.insert(0, 0)

length = tk.Label(window, text="Length", bg='#3C84F4').grid(row=8, column=0, sticky=W)
length_entry = Entry(window, width=4)
length_entry.grid(row=8, column=0, sticky=S)
length_entry.insert(0, 0)

tk.Label(window, text="Total Area", bg='#3C84F4').grid(row=9, column=0, sticky=W)
area_output = Text(window, width=5, height=1, wrap=WORD)
area_output.grid(row=9, column=0, sticky=S)
area_output.configure(state="disabled")
area_output.config(background="lightgrey")

tk.Label(window, text="Details (Contact & Colour)", bg='#3C84F4', font=('bold')).grid(row=11, column=0, ipady=10,
                                                                                      sticky=W)

tk.Label(window, text="Name", bg='#3C84F4').grid(row=12, sticky=W)
name_entry = Entry(window, width=25)
name_entry.grid(row=12, column=0, sticky=E)

tk.Label(window, text="Email", bg='#3C84F4').grid(row=13, sticky=W)
contact_entry = Entry(window, width=25)
contact_entry.grid(row=13, column=0, sticky=E)

tk.Label(window, text="ISBN", bg='#3C84F4').grid(row=15, sticky=W)
isbn_entry = Entry(window, width=25)
isbn_entry.grid(row=15, column=0, sticky=E)

tk.Label(window, text="Page Number", bg='#3C84F4').grid(row=16, sticky=W)
pageno_entry = Entry(window, width=25)
pageno_entry.grid(row=16, column=0, sticky=E)



calculate = Button(window, text="Calculate area", bg="#3C84F4", width=15, command=total_area, state=NORMAL).grid(row=10,
                                                                                                                column=0,
                                                                                                                sticky=W)


confirmation = Button(window, text="Submit", font=("Arial", 15), bg="#4CAF50", width=7, command=verify,
                      state=NORMAL).grid(row=17, column=0, sticky=W)

output = Text(window, width=35, height=7, wrap=WORD, fg="black")
output.grid(row=18, column=0, columnspan=2, sticky=W, ipady=30)

output.config(background="#A9A9A9")

window.mainloop()
