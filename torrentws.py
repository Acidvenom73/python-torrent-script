#! python3
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from webbrowser import open

def main():

    ans = ""
    print("Options: Press 1 for Single Download")
    while(not ans == "1"):
        ans = input()
        if ans == "1":
            single()
        elif ans == "X" or ans == "C":
            break
    return


def single():
    print("Input your search: ")
    search = input()
    url = "https://magnetdl.me/search/" + search + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        Data = list(soup.findAll(title="Direct Download"))
    except IndexError:
        print("No torrents found!")
        return True

    i = 0
    while(True):
        ans = ""
        try:
            link = str(Data[i])
        except IndexError:
            print("Out of torrents!")
            return True
        link = link.partition("<a href=\"")[2]
        link = link.partition("\" rel=\"")[0]
        title = link.split("dn=")[1]
        title = title.split("&amp;")[0]
        print(title)
        while(ans != "Y" and ans != "N" and ans != "C"):
            print("Y = Yes, N = No, C = Cancel")
            ans = input()
        if ans == "Y":
            break
        elif ans == "C":
            return False
        i+=1

    open(link)
    print(link)
    return True

# def batch():
#     print("BATCH DOWNLOAD")

#     episode_counter = 0
#     print("Torrent name:")
#     search = input()

#     print("Season: ", end="")
#     season = "S0" + input()

#     while(True):
#         episode_counter+=1
#         if episode_counter < 10:
#             episode = "E0" + str(episode_counter)
#         else:
#             episode = str(episode_counter)
#         url = "https://kickasstorrents.to/usearch/" + search + " " + season + episode
#         print(url)
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         try:
#             Data = list(soup.findAll(title="Download torrent file"))
#         except IndexError:
#             print("No more episodes found!")
#             return True
#         i = 0
#         while(True):
#             ans = ""
#             try:
#                 link = str(Data[i])
#             except IndexError:
#                 print("Out of torrents!")
#                 return True
#             link = link.partition(" target=")[0]
#             link = link.partition("/download/")[2]
#             link = link.replace("\"", "")
#             print(link)
#             while(ans != "Y" and ans != "N" and ans != "C"):
#                 print("Y = Yes, N = No, C = Cancel")
#                 ans = input()
#             if ans == "Y":
#                 break
#             elif ans == "C":
#                 return False
#             i+=1

#         url = "https://kickasstorrents.to/" + link
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         link = str(soup.findAll(title="Magnet link"))
#         link = link.partition("title=")[0]
#         link = link.partition("href=")[2]
#         link = link.replace("\"", "")

#         open(link)
#         print(link)


if __name__ == "__main__":
    main()
