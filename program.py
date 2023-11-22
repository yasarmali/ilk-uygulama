import tkinter as tk

arayüz = tk.Tk()
arayüz.title("Sifre")
arayüz.geometry("300x200")

kullanici = tk.Label(text="Kullanıcı Adı:")
kullanici.place(x=10,y=10)
a1 ="maliyasar"
a2 ="mali1234"



y = tk.StringVar()
kullanici_giris = tk.Entry(textvariable=y)
kullanici_giris.place(x=100,y=10)

kullanici = tk.Label(text="Şifre:")
kullanici.place(x=30,y=35)


x = tk.StringVar()
kullanici_giris = tk.Entry(textvariable=x)
kullanici_giris.place(x=100,y=30)

dogru_yanlis = tk.Label(font="Verdena 25 bold")
dogru_yanlis.place(x=100,y=95)

def giris_komut():
    kullan = y.get()
    sif = x.get()
    print(kullan,sif)
    if kullan == a1 and sif == a2:
        dogru_yanlis.config(text="Doğru",fg="green")
    else:
        dogru_yanlis.config(text="Yanlış",fg="red")
        

giris = tk.Button(text="GİRİŞ", command=giris_komut)
giris.place(x=187,y=60)

arayüz.mainloop()

