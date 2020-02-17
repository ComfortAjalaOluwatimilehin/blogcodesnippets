from urllib.parse import urlparse
import requests
from requests.exceptions import HTTPError
import xml.etree.ElementTree as ET
from typing import List
import tkinter
from functools import partial
import webbrowser


class Item:
    title: str
    description: str
    link: str

    def __init__(self, title, description, link):
        super().__init__()
        self.title = title
        self.description = description
        self.link = link

    def openbrowser(self) -> None:
        webbrowser.open_new_tab(self.link)


def geturlfromuser() -> str:
    userinput: str = input("Type in a valid url ")
    return userinput


def validateurl(url: str) -> bool:
    parsed = urlparse(url)
    allowedscheme = ["http", "https"]
    scheme: str = parsed.scheme
    return scheme in allowedscheme


def cleanurl(url: str) -> str:
    if url[len(url) - 1] == "/":
        return url[0: len(url) - 1]
    else:
        return url


def fetchxmlasstring(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except HTTPError as httperror:
        print("Errror:fetchxmlasstring {}".format(httperror))
    except Exception as e:
        print("General excepton: {}".format(e))
    else:
        print("done")


def getitems(content: str) -> List[Item]:
    root = ET.fromstring(content)
    items: List[Item] = list()
    print("finding items")
    for item in root.findall(".//item"):
        title = item.find("title").text
        description = item.find("description").text
        link = item.find("link").text
        item: Item = Item(title, description, link)
        items.append(item)
    return items


def clickpost(item: Item) -> None:
    webbrowser.open_new_tab(item.link)


def setupui(items: List[Item]) -> None:
    top = tkinter.Tk()
    for item in items:
        label = tkinter.Label(top, text=item.title)

        button = tkinter.Button(top, text="Open Post",
                                command=item.openbrowser)
        description = tkinter.Message(top, text=item.description)
        label.pack()
        description.pack()
        button.pack()
    tkinter.mainloop()


def start():
    url: str = geturlfromuser()
    isvalid: bool = validateurl(url)
    if isvalid == True:
        cleanedurl: str = cleanurl(url)
        content: str = fetchxmlasstring("{}/feed".format(cleanedurl))
        if content and len(content) > 0:
            items: List[Item] = getitems(content)
            setupui(items)
    else:
        print("invalid url {}".format(url))


start()
