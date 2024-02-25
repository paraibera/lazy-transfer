"""This one is even more lazy, since it's meant to be run in Termux.
   Termux = Linux for Android.

   1. Extracts the .mp3 of YouTube video.
   2. Saves it on Downloads directory (already in the phone)!
   """

# importing packages
import os
import qrcode
import socket
import argparse
import http.server
import socketserver

from PIL import Image
from pytube import YouTube


def download():
    """Download YouTube video given an URL."""

    # url input from user
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

    # extract only audio (best audio bitrate)
    video = yt.streams.filter(only_audio=True).order_by("abr").desc().first()

    # download the file to downloads folder
    out_file = video.download(output_path="../storage/downloads/")

    # save the file
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")


def main():
    """Main."""

    download()


if __name__ == "__main__":
    main()
