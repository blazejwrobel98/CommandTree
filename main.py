import tkinter as tk

window = tk.Tk()
window.title("DCN CommandTree")
window.geometry("500x350")
window.resizable(0, 0)
# noinspection SpellCheckingInspection
label = tk.Label(window, text="Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\n"
                              "Z binarnych liczb złożoności")
label.pack(side=tk.TOP)

tk.mainloop()
