# def pecah_uang(coin, n):
#     total = 0
#     i = len(coin) - 1  # Mulai dari koin terbesar
#     while n != 0 and i >= 0:
#         if coin[i] <= n:
#             n -= coin[i]
#             print("Pilih koin", coin[i], "tersisa", n)
#             total += 1
#         else:
#             i -= 1
#     return total

# koin_input = input("Masukkan koin (pisahkan dengan spasi): ")
# uang_input = input("Masukkan uang: ")

# split_koin = koin_input.split(" ")
# coin = list(map(int, split_koin))
# coin.sort()

# print("\nKoin: ", coin)
# print("Uang: ", uang_input, "\n")

# total_koin = pecah_uang(coin, int(uang_input))
# print("Uang $", uang_input, "dapat ditukar menjadi", total_koin, "koin")
# --------------------------------------------------------------------------------------------------


import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pecah Uang")
        self.window.geometry("1280x632")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.result_label = tk.Label(self.window, text="", wraplength=400)  # Label untuk hasil

        self.canvas.create_text(
            700.0,
            200.0,
            anchor="nw",
            text="MASUKKAN KOIN :",
            fill="#9E6F21",
            font=("Inter Black", 24 * -1, "bold")
        )
        
        self.canvas.create_text(
            700.0,
            270.0,
            anchor="nw",
            text="pisahkan dengan spasi !",
            fill="#9E6F21",
            font=("Inter Black", 15 * -1, "bold")
        )

        
        self.canvas.create_text(
            700.0,
            350.0,
            anchor="nw",
            text="MASUKKAN UANG :",
            fill="#9E6F21",
            font=("Inter Black", 24 * -1, "bold")
        )

    
        self.canvas.create_text(
            750.0,
            82.0,
            anchor="nw",
            text="PENUKARAN UANG\n",
            fill="#9E6F21",
            font=("Inter Black", 45 * -1, "bold")
        )

        self.button_1 = Button(
            # image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.proses_klik,                    
            relief="flat",text="TUKAR",fg="#9E6F21",
            font=("Inter Black", 24 * -1, "bold")
        )
        self.button_1.place(
            x=1051.0000610351562,
            y=275.0,
            width=189.0,
            height=69.0
        )

        self.coin_entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.coin_entry.place(
            x=700.0,
            y=230.0,
            width=330.0,
            height=33.0
        )

        self.uang_entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.uang_entry.place(
            x=700.0,
            y=380.5,
            width=330.0,
            height=33.0
        )

        image_image_1 = PhotoImage(
            file=("coin1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )
        self.canvas.create_text(700.0,470.0, text="HASIL PENUKARAN :",fill="#9E6F21",anchor="nw", 
            font=("Inter Black", 24 * -1, "bold"))

        self.window.resizable(True, True)
        self.window.mainloop()

    def pecah_uang(self, coin, n):
        total = 0
        i = len(coin) - 1
        result_text = ""
        koin_terpilih = {}

        while n != 0 and i >= 0:
            if coin[i] <= n:
                n -= coin[i]
                if coin[i] in koin_terpilih:
                    koin_terpilih[coin[i]] += 1
                else:
                    koin_terpilih[coin[i]] = 1

                result_text += f"Pilih koin {coin[i]}, tersisa {n}\n"
                total += 1
            else:
                i -= 1

        # Tampilkan hasil pada elemen GUI (result_label)
        self.result_label.config(text=result_text)
        self.result_label.place(x=980.0,y=450.0)  # Pastikan label ditampilkan di jendela GUI
        
        result_text += f"Uang ${self.uang_entry.get()} dapat ditukar menjadi {total} koin\n\n"
        result_text += "Rincian koin yang digunakan:\n"

        for koin, jumlah in koin_terpilih.items():
            result_text += f"${koin}: {jumlah} koin\n"
        self.result_label.config(text=result_text)

    def proses_klik(self):
        koin = self.coin_entry.get().split()
        koin = list(map(int, koin))
        koin.sort()

        n = int(self.uang_entry.get())

        self.pecah_uang(koin, n)

if __name__ == "__main__":
    app = App()

# ==================================================================

