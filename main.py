from tkinter import *
import speedtest

def animate_speed(label, target, unit="Mbps", delay=10):
    current = 0.0
    increment = target / 100

    def step():
        nonlocal current
        current += increment
        if current >= target:
            current = target
        label.config(text=f"{current:.2f} {unit}")
        if current < target:
            label.after(delay, step)

    step()

def speedcheck():
    button.config(text="CHECKING...", state=DISABLED)
    sp.update()

    st = speedtest.Speedtest()
    st.get_servers()
    down = round(st.download() / (10 ** 6), 3)  # Mbps
    up = round(st.upload() / (10 ** 6), 3)

    animate_speed(download_speed, down)
    animate_speed(upload_speed, up)

    button.config(text="CHECK SPEED", state=NORMAL)

sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("300x500")
sp.config(bg="black")

title_label = Label(sp, text="Internet Speed Tester", font=("Amazon Ember Display", 18, "bold"), bg="black", fg="white")
title_label.pack(pady=20)

download_label = Label(sp, text="Download Speed", font=("Amazon Ember Regular", 14), bg="black", fg="white")
download_label.pack(pady=10)

download_speed = Label(sp, text="00 Mbps", font=("Spotify Mix Extrabold", 16, "bold"), bg="black", fg="red")
download_speed.pack(pady=5)

upload_label = Label(sp, text="Upload Speed", font=("Amazon Ember Regular", 14), bg="black", fg="white")
upload_label.pack(pady=10)

upload_speed = Label(sp, text="00 Mbps", font=("Spotify Mix Extrabold", 16, "bold"), bg="black", fg="dodgerblue")
upload_speed.pack(pady=5)

button = Button(
    sp,
    text="CHECK SPEED",
    font=("Lemon Milk", 10, "bold"),
    relief=RAISED,
    bg="white",
    fg="black",
    disabledforeground="black",
    command=speedcheck
)

button.pack(pady=40)



sp.mainloop()