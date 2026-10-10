
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path


def decimal_to_bcd():
    value = entry_decimal.get().strip()

    if not value:
        messagebox.showwarning("Uyarı", "Lütfen bir decimal sayı girin.")
        return

    if not value.isdigit():
        messagebox.showerror(
            "Geçersiz Girdi",
            "Lütfen yalnızca 0 veya pozitif bir tam sayı girin."
        )
        return

    decimal_number = int(value)

    # Her decimal rakamını ayrı ayrı 4 bit ile göster.
    bcd_result = " ".join(f"{int(digit):04b}" for digit in value)

    result_decimal.config(text=str(decimal_number))
    result_bcd.config(text=bcd_result)


def clear_fields():
    entry_decimal.delete(0, tk.END)
    result_decimal.config(text="-")
    result_bcd.config(text="-")
    entry_decimal.focus()


# Ana pencere
root = tk.Tk()
root.title("DEC to BCD Converter")
root.geometry("850x650")
root.minsize(750, 550)
root.resizable(True, True)
root.configure(bg="#101827")

# Başlık
title = tk.Label(
    root,
    text="DEC  →  BCD",
    font=("Segoe UI", 25, "bold"),
    bg="#101827",
    fg="#60A5FA"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Decimal to Binary-Coded Decimal Converter",
    font=("Segoe UI", 10),
    bg="#101827",
    fg="#CBD5E1"
)
subtitle.pack(pady=(0, 20))

# Giriş alanı
input_label = tk.Label(
    root,
    text="Decimal sayıyı girin",
    font=("Segoe UI", 11, "bold"),
    bg="#101827",
    fg="white"
)
input_label.pack()

entry_decimal = tk.Entry(
    root,
    font=("Consolas", 16),
    justify="center",
    width=25,
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_decimal.pack(pady=10, ipady=8)
entry_decimal.bind("<Return>", lambda event: decimal_to_bcd())

# Butonlar
button_frame = tk.Frame(root, bg="#101827")
button_frame.pack(pady=10)

convert_button = tk.Button(
    button_frame,
    text="DÖNÜŞTÜR",
    command=decimal_to_bcd,
    font=("Segoe UI", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=9
)
convert_button.pack(side="left", padx=6)

clear_button = tk.Button(
    button_frame,
    text="TEMİZLE",
    command=clear_fields,
    font=("Segoe UI", 10, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=9
)
clear_button.pack(side="left", padx=6)

# Sonuç alanı
result_frame = tk.Frame(
    root,
    bg="#1E293B",
    padx=20,
    pady=15
)
result_frame.pack(fill="x", padx=35, pady=15)

tk.Label(
    result_frame,
    text="DECIMAL",
    font=("Segoe UI", 9, "bold"),
    bg="#1E293B",
    fg="#94A3B8"
).pack()

result_decimal = tk.Label(
    result_frame,
    text="-",
    font=("Consolas", 16, "bold"),
    bg="#1E293B",
    fg="white"
)
result_decimal.pack(pady=(2, 10))

tk.Label(
    result_frame,
    text="BCD SONUCU",
    font=("Segoe UI", 9, "bold"),
    bg="#1E293B",
    fg="#94F7C5"
).pack()

result_bcd = tk.Label(
    result_frame,
    text="-",
    font=("Consolas", 17, "bold"),
    bg="#1E293B",
    fg="#94F7C5",
    wraplength=480
)
result_bcd.pack(pady=(5, 0))

footer = tk.Label(
    root,
    text="Each decimal digit is encoded separately using 4 bits.",
    font=("Segoe UI", 8),
    bg="#101827",
    fg="#64748B"
)
footer.pack(pady=5)

entry_decimal.focus()


# VISION Üniversitesi logosu
logo_path = Path(__file__).parent / "assets" / "vizyon_logo.png"

if logo_path.exists():
    logo_image = Image.open(logo_path).convert("RGBA")

    # Logo boyutu: en fazla 180 x 180 piksel
    logo_image.thumbnail((180, 180))

    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(
        root,
        image=logo_photo,
        bg="#101827"
    )

    # Sol üst köşe
    logo_label.place(x=25, y=20, anchor="nw")

root.mainloop()