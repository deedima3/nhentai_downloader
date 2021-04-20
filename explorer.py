import os
import requests
from bs4 import BeautifulSoup
import eel

SAVE_FOLDER = "heheboi"
PREVIEW_FOLDER = "web/preview"

eel.init('web')

@eel.expose
def download_hentai(nuclear_code):
    newpath = SAVE_FOLDER + "/" + str(nuclear_code)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    url = "https://nhentai.net/g/" + str(nuclear_code) + "/1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    info = soup.find('span', {'class': 'num-pages'})
    pages = int(info.get_text())
    for i in range(pages):
        download_url = "https://nhentai.net/g/" + str(nuclear_code) + "/" + str(i+1)
        print(download_url)
        pics = requests.get(download_url)
        soup = BeautifulSoup(pics.text, 'html.parser')
        info = soup.find_all('img')
        for src in info:
            if "i.nhentai.net" in src['src']:
                download = requests.get(src['src'])
                print(download)
                imagename = SAVE_FOLDER + "/" + str(nuclear_code) + "/" + str(nuclear_code) + "_" + str(i+1) + ".png"
                with open(imagename, 'wb') as file:
                    file.write(download.content)

@eel.expose
def preview(nuclear_code):
    download_url = "https://nhentai.net/g/" + str(nuclear_code) + "/" + str(1)
    print(download_url)
    pics = requests.get(download_url)
    soup = BeautifulSoup(pics.text, 'html.parser')
    info = soup.find('img')
    info = soup.find_all('img')
    for src in info:
        if "i.nhentai.net" in src['src']:
            download = requests.get(src['src'])
            imagename = PREVIEW_FOLDER + "/" + str(nuclear_code) + "_" + str(1) + ".png"
            with open(imagename, 'wb') as file:
                file.write(download.content)
    return "preview/" + str(nuclear_code) + "_" + str(1) + ".png"

eel.start('index.html', size=(1280,900))
