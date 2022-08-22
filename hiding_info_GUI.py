from tkinter import *
from stegano import lsb
from tkinter import filedialog


def imp():
    global img
    import_file_path = filedialog.askopenfilename()
    img = f"{import_file_path}"
    Label(text="Image imported").pack()


def exp():
    global img
    msg = textarea.get(1.0, END)
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    new_img = f"{export_file_path}"
    lsb.hide(img, message=msg).save(new_img)
    for item in root.winfo_children():
        item.destroy()
    Label(text="HIDING DONE, PLEASE CHECK THE RESPECTIVE DIRECTORY",
          font="helvetica 16 bold").pack(pady=20)
    Label(text="THANK YOU, FOR USING THE APPLICATION",
          font="helvetica 16 bold").pack(pady=20)
    Label(text="Created by:", font="helvetica 10").pack(pady=12)
    Label(text="Shrish Shrinath Vaidya", font="helvetica 10").pack(pady=12)


def hide_pressed(bh1):
    bh1.pack_forget()
    global textarea
    Label(text="Now write the text you want to hide in this image:",
          font="helvetica 14").pack(pady=10)
    textarea = Text(root, font="lucida 13", height=15, width=60)
    textarea.pack()
    bh2 = Button(text="Hide", pady=10, padx=10,
                 font="helvetica 12", command=exp)
    bh2.pack(pady=10)


def reveal_pressed():
    message = lsb.reveal(img)
    for item in root.winfo_children():
        item.destroy()
    try:
        if message == None:
            Label(text="There is no hidden info in this image",
                  font="helvetica 16 bold").pack(pady=20)
            Label(text="THANK YOU FOR USING THE APPLICATION",
                  font="helvetica 16 bold").pack(pady=20)
            Label(text="Created by:", font="helvetica 10").pack(pady=10)
            Label(text="Shrish Shrinath Vaidya",
                  font="helvetica 10").pack(pady=10)

        else:
            Label(text="The hidden info is : ",
                  font="helvetica 16 bold").pack(pady=20)
            Label(text=f"{message}", font="helvetica 14").pack(pady=20)
            Label(text="THANK YOU FOR USING THE APPLICATION",
                  font="helvetica 14 bold").pack(pady=20)
            Label(text="Created by:", font="helvetica 14").pack(pady=10)
            Label(text="Shrish Shrinath Vaidya",
                  font="helvetica 14").pack(pady=10)

    except Exception as e:
        print(e)
        Label(text="Invalid image format").pack()


root = Tk()
root.geometry("1536x864")
root.title("Hinding info in images")
root.wm_iconbitmap("image.ico")
# root.configure(background="grey")

Label(text="Welcome to the world of hidden info in images",
      font="helvetica 30 bold", pady=20).pack()


Button(text="Import image", pady=10,
       font="helvetica 14", command=imp).pack(pady=14)
Label(text="Now select either of these options:",
      font="helvetica 16").pack(pady=10)
bh1 = Button(text="Hide", pady=10, padx=10, font="helvetica 12", relief=RAISED,
             command=lambda: hide_pressed(bh1))
bh1.pack(pady=10)
b2 = Button(text="Reveal", pady=10, padx=10,
            font="helvetica 12", relief=RAISED, command=reveal_pressed)
b2.pack(pady=10)

root.mainloop()
