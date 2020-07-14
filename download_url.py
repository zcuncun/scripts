import os
from urllib.request import urlretrieve
from urllib.error import URLError
from multiprocessing import Pool

with open('URL_0609.txt') as f:
    infos = f.readlines()

print(len(infos))

infos = [info for info in infos if info[:4] == 'http']

print(len(infos))

infos = [info.split() for info in infos]

ext_map = {'jpg': 'jpg', 'jpeg': 'jpg', 'png': 'png', 'JPG': 'jpg', 'PNG': 'png', 'jpG': 'jpg'}

def download(info):
    ext = info[0][info[0].rfind('.') + 1:]
    try:
        urlretrieve(info[0], f'ecd_images/{info[1]}.{ext_map[ext]}')
    except URLError:
        print(info)
    else:
        pass

with Pool(16) as p:
    p.map(download, infos)
