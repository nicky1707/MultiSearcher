import webbrowser
import urllib.parse
import tkinter as tk
from tkinter import ttk

def create_url():
    # while True:
    query = search_entry.get().strip()
    if query != "":
        query = query.replace(" ", "+") # Replace spaces with plus signs
        urls = [
            f"https://search.brave.com/search?q={query}",
            f"https://www.bing.com/search?q={query}",
            f"https://www.google.com/search?q={query}",
            f"https://https://duckduckgo.com/?hps=1&q={query}ia=web",
        ]
        return urls
    else:
        print("Please enter a search term.")
        return None


def open_new_tabs(urls):
    # open multiple tabs with 3 search engines in default browser
    for url in urls:
        webbrowser.open_new_tab(url)


def search(event=None):
    urls = create_url()
    open_new_tabs(urls)


# create a window
window = tk.Tk()
window.title("Search")
window.geometry("400x150")
window.configure(bg="#282a36")  
window.iconbitmap(default="")

# window.iconbitmap('logo.ico')
# window.iconbitmap("")
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', foreground='#f8f8f2', background='#282a36')
style.configure('TEntry', foreground='#f8f8f2', fieldbackground='#44475a')
style.configure('TButton', foreground='#f8f8f2', background='#44475a', relief='flat', padding=5, font=('Segoe UI', 10))


# create a label
label = ttk.Label(window, text=" ")
label.pack(pady=10)

# create an entry widget
search_entry = ttk.Entry(window, width=30,font=('Helvetica', 16))
search_entry.pack(pady=8, ipady=8)

# Bind the Return key to the search function
search_entry.bind("<Return>", search)

# center the window on the screen
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

search_entry.focus_set()  # set focus to the entry widget

# run the main event loop
window.mainloop()
