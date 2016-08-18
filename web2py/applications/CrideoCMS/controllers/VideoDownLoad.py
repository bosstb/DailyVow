from __future__ import unicode_literals

from applications.CrideoCMS.modules import youtube_dl

ydl_opts = {}


def index():
    download('https://www.youtube.com/watch?v=rCRP-5om_3Y');
    return "dafas";


def download(url):

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
