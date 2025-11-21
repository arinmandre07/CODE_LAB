from tkinter import *
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk
from stegano import lsb
from openai import OpenAI
import base64  


client = OpenAI(api_key="Your API")

root = Tk()
root.title("CipherVision: Advanced Image Steganography Tool")
root.geometry("1240x720+150+80")
root.resizable(False, False)
root.configure(background="#0f0f0f")

filename = None
saved_file = None


def encrypt_base64(text):
    return base64.b64encode(text.encode()).decode()

def decrypt_base64(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return text  


def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select an image File",
        filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All files", "*.*"))
    )
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=400, height=350)
        lbl.image = img

def Hide():
    global secret, saved_file, lbl, filename
    message = text1.get(1.0, END).strip()
    if not filename:
        messagebox.showerror("Error", "Please open an image first!")
        return
    if message:
        encrypted_message = encrypt_base64(message)
        secret = lsb.hide(filename, encrypted_message)
        saved_file = "hidden.png"
        secret.save(saved_file)
        
        
        text1.delete(1.0, END)
        
        
        lbl.configure(image=None)
        lbl.image = None
        filename = None
        
        messagebox.showinfo("Success", f"Message hidden and saved in {saved_file}")

def Show():
    global saved_file, lbl, filename
    target_file = saved_file if saved_file else filename
    if not target_file:
        messagebox.showerror("Error", "No image selected!")
        return

    hidden_message = lsb.reveal(target_file)
    if hidden_message:
        decrypted = decrypt_base64(hidden_message)
        
        
        lbl.configure(image=None)
        lbl.image = None
        filename = None
        
        
        open_chatbot(initial_text=f"Decrypt text: {decrypted}")
    else:
        messagebox.showwarning("Warning", "No hidden message found!")


def save():
    global saved_file
    if 'secret' in globals():
        secret.save("hidden.png")
        saved_file = "hidden.png"
        messagebox.showinfo("Saved", "Image saved as hidden.png")
    else:
        messagebox.showerror("Error", "No secret image to save.")


def open_chatbot(initial_text=None):
    chat_win = Toplevel(root)
    chat_win.title("Cipher Terminal")
    chat_win.geometry("600x500")
    chat_win.configure(bg="black")

    chat_history = Text(chat_win, font=("Consolas", 12), bg="black", fg="lime", wrap=WORD, state=DISABLED)
    chat_history.place(x=10, y=10, width=580, height=380)

    chat_input = Text(chat_win, font=("Consolas", 12), bg="#111111", fg="lime", insertbackground="lime", height=3)
    chat_input.place(x=10, y=400, width=480, height=80)

    if initial_text:
        chat_input.insert("1.0", initial_text)

    def send_message():
        user_input = chat_input.get("1.0", END).strip()
        chat_input.delete("1.0", END)
        if not user_input:
            return

        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"user@cipher:~$ {user_input}\n")
        chat_history.config(state=DISABLED)
        chat_history.see(END)

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are the Cipher System, a helpful assistant for Base64 encryption and decryption do it perfectly without making a mistake in the message."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content.strip()
            chat_history.config(state=NORMAL)
            chat_history.insert(END, f"cipher@system:~$ {reply}\n\n")
            chat_history.config(state=DISABLED)
            chat_history.see(END)
        except Exception as e:
            chat_history.config(state=NORMAL)
            chat_history.insert(END, f"Error: {e}\n\n")
            chat_history.config(state=DISABLED)
            chat_history.see(END)

    Button(chat_win, text="Execute", font="arial 12 bold", bg="white", fg="black", command=send_message).place(x=500, y=420, width=80, height=40)


try:
    image_icon = ImageTk.PhotoImage(Image.open("anony.png"))
    root.iconphoto(False, image_icon)
except:
    pass

try:
    logo = ImageTk.PhotoImage(Image.open("egg.png"))
    Label(root, image=logo, bg='#2f4155').place(x=20, y=20)
except:
    pass

Label(root, text="Cipher Vision", background="#0f0f0f", fg="white", font=('ariel 25 bold')).place(x=120, y=45)


f = Frame(root, bd=3, bg="black", width=580, height=400, relief=GROOVE)
f.place(x=20, y=150)
lbl = Label(f, bg="black")
lbl.place(x=80, y=30)


frame2 = Frame(root, bd=3, width=580, height=400, bg="black", relief=GROOVE)
frame2.place(x=640, y=150)
text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=580, height=400)
Scrollbar1 = Scrollbar(frame2)
Scrollbar1.place(x=560, y=0, height=400)
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)


frame3 = Frame(root, bd=3, bg="black", width=580, height=100, relief=GROOVE)
frame3.place(x=20, y=585)
Button(frame3, text="Open Image", width=16, height=2, font="arial 15 bold", command=showimage).place(x=30, y=15)
Button(frame3, text="Save Image", width=16, height=2, font="arial 15 bold", command=save).place(x=340, y=15)


frame4 = Frame(root, bd=3, bg="black", width=580, height=100, relief=GROOVE)
frame4.place(x=640, y=585)
Button(frame4, text="Encrypt", width=16, height=2, font="arial 15 bold", command=Hide).place(x=30, y=15)
Button(frame4, text="Decrypt", width=16, height=2, font="arial 15 bold", command=Show).place(x=340, y=15)


def on_enter(e):
    cipher_btn['bg'] = '#4CAF50'  
    cipher_btn['fg'] = 'white'

def on_leave(e):
    cipher_btn['bg'] = '#3A3A3A'
    cipher_btn['fg'] = '#00FF41'

cipher_btn = Button(
    root,
    text="💬 Open Cipher",
    font=("Arial", 14, "bold"),
    bg="#3A3A3A",
    fg="#00FF41",
    activebackground="#4CAF50",
    activeforeground="white",
    bd=0,               
    relief=RIDGE,
    cursor="hand2",
    padx=20,            
    pady=10,            
    command=open_chatbot
)
cipher_btn.place(x=980, y=30)


cipher_btn.bind("<Enter>", on_enter)
cipher_btn.bind("<Leave>", on_leave)

root.mainloop()
