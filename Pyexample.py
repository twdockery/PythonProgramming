# Written by Jonathan Zaharin in CSC121, Not Tyler Dockery
import tkinter
from tkinter import * #allows import

root=tkinter.Tk()
root.title("Grade Calculator")

def submit():
    final_lab_total= float(lab_entry_1.get()) * 55 / 300  + float(lab_entry_2.get()) * 55 / 300 + float(lab_entry_3.get()) * 55 / 300
    total_lab_score.insert(END, "=" + str(final_lab_total))


########################################################################################################################

label_lab_1=Label(root,text="Lab Score 1")
label_lab_1.grid(row=0,column=0)

label_lab_2=Label(root,text="Lab Score 2")
label_lab_2.grid(row=1,column=0)

label_lab_3=Label(root,text="Lab Score 3")
label_lab_3.grid(row=2,column=0)


lab_entry_1=Entry(root)
lab_entry_1.grid(row=0,column=1)

lab_entry_2=Entry(root)
lab_entry_2.grid(row=1,column=1)

lab_entry_3=Entry(root)
lab_entry_3.grid(row=2,column=1)

########################################################################################################################


submit_button=Button(root,text="Calculate Results",width=30,command=submit)
submit_button.grid(row=5,column=0,columnspan=2)

total_lab_score_label=Label(root,text="total lab score")
total_lab_score_label.grid(row=4,column=0)

total_lab_score=Entry(root)
total_lab_score.grid(row=4,column=1)

root.mainloop()