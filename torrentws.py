#! python3
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from webbrowser import open
import tkinter as tk

def gui():
    window = tk.Tk()
    window.title("Torrent helper")
    window.geometry('700x350')

    searchinput = tk.Entry(window, width=40)
    searchinput.grid(column=2, row=0)
    listbox  = tk.Listbox(window, selectmode="SINGLE", width="50")
    listbox.grid(column=3, row=3)
    Link, Titles = list(), list()

    def search():
        global Titles
        global Link
        Link, Titles = single(searchinput.get())
        for x, val in enumerate(Titles):
            listbox.insert(x, val)

    def download(): 
        global Link
        selection = listbox.curselection()[0]
        open(Link[selection])

    downloadbtn = tk.Button(window, text="Download", command=download)
    downloadbtn.grid(column=3, row=4)
    searchbtn = tk.Button(window, text="Search:", command=search)
    searchbtn.grid(column=0, row=0)
    window.mainloop()
    return


def main():
    gui()


def single(search):
    url = "https://magnetdl.me/search/" + search + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        Data = list(soup.findAll(title="Direct Download"))
    except IndexError:
        print("No torrents found!")
        return False

    def linkpartition(link):
        link = str(link)
        ret = link.partition("<a href=\"")[2]
        ret = ret.partition("\" rel=\"")[0]
        return ret

    def titlepartition(link):
        ret = linkpartition(link)
        ret = ret.split("dn=")[1]
        ret = ret.split("&amp;")[0]
        return ret

    Link = list(map(linkpartition, Data))
    Titles = list(map(titlepartition, Data))

    return [Link, Titles]

if __name__ == "__main__":
    main()
