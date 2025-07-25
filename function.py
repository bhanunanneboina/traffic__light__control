import tkinter as tk
from tkinter import messagebox

def create_card():
    groom = groom_entry.get().strip()
    bride = bride_entry.get().strip()
    date = date_entry.get().strip()
    venue = venue_entry.get().strip()

    if not (groom and bride and date and venue):
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    card_text = (
        f"💍 Wedding Invitation 💍\n\n"
        f"You are cordially invited to the wedding of\n\n"
        f"{groom} & {bride}\n\n"
        f"Date: {date}\n"
        f"Venue: {venue}\n\n"
        f"Please join us to celebrate this joyous occasion!"
    )

    card_label.config(text=card_text)

def change_bg_color(event=None):
    selected_color = bg_color_var.get()
    root.config(bg=selected_color)
    # Also update background of widgets where needed
    for widget in [groom_label, bride_label, date_label, venue_label, create_btn, card_label, bg_label, bg_color_menu]:
        widget.config(bg=selected_color)

# Create main window
root = tk.Tk()
root.title("Wedding Card Creator")
root.geometry("400x550")
root.resizable(False, False)

# Default background color
default_bg = "white"
root.config(bg=default_bg)

# Labels and Entries for input
groom_label = tk.Label(root, text="Groom's Name:", bg=default_bg)
groom_label.pack(pady=(20,0))
groom_entry = tk.Entry(root, width=40)
groom_entry.pack()

bride_label = tk.Label(root, text="Bride's Name:", bg=default_bg)
bride_label.pack(pady=(10,0))
bride_entry = tk.Entry(root, width=40)
bride_entry.pack()

date_label = tk.Label(root, text="Wedding Date:", bg=default_bg)
date_label.pack(pady=(10,0))
date_entry = tk.Entry(root, width=40)
date_entry.pack()

venue_label = tk.Label(root, text="Venue:", bg=default_bg)
venue_label.pack(pady=(10,0))
venue_entry = tk.Entry(root, width=40)
venue_entry.pack()

# Background color selection
bg_label = tk.Label(root, text="Select Background Color:", bg=default_bg)
bg_label.pack(pady=(15,0))

bg_color_var = tk.StringVar(value=default_bg)
colors = ["white", "light pink", "light blue", "light yellow", "lavender", "peach puff", "mint cream"]
bg_color_menu = tk.OptionMenu(root, bg_color_var, *colors, command=change_bg_color)
bg_color_menu.config(width=15)
bg_color_menu.pack()

# Create Card button
create_btn = tk.Button(root, text="Create Wedding Card", command=create_card, bg="#f4a261", fg="white")
create_btn.pack(pady=20)

# Label to display the wedding card
card_label = tk.Label(root, text="", justify="center", font=("Helvetica", 12), fg="#264653", bg=default_bg, wraplength=350)
card_label.pack(pady=10, padx=10)

root.mainloop()
