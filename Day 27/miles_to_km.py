import tkinter

window=tkinter.Tk()
window.title("MILES TO KM CONVERTER")
window.minsize(width=500,height=300)
window.config(padx=200,pady=200)

def converter():
    km_lable.config(text=round(int(input.get())*1.609,3))

#mile entry
input=tkinter.Entry()
input.grid(column=1,row=0)

km_lable=tkinter.Label(text="",font=("Arial",10,"bold"))
km_lable.grid(row=1,column=1)

button=tkinter.Button(text="convert",command=converter)
button.grid(column=1,row=2)

mile_label=tkinter.Label(text="Miles")
mile_label.grid(column=2,row=0)

km_label=tkinter.Label(text="Km")
km_label.grid(column=2,row=1)

is_equ_label=tkinter.Label(text="is equal to")
is_equ_label.grid(row=1,column=0)




window.mainloop()