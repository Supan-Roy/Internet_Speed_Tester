from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3))+" Mbps"
    up = str(round(sp.upload()/(10**6), 3))+" Mbps"
    download_speed.config(text=down)
    upload_speed.config(text=up)

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

button = Button(sp, text="CHECK SPEED", font=("Lemon Milk", 10, "bold"), relief=RAISED, bg="red", command=speedcheck)
button.pack(pady=40)



sp.mainloop()