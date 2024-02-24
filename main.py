"""Absolute laziness.

   1. Extracts the .mp3 of YouTube video.
   2. Saves it on current directory.
   3. Starts a HTTP server.
   4. Generates a QR code for connecting to HTTP server on cellphone.
   5. Now you can download the file to your phone, no need for cables.
    
   Very useful when I need to download a live set (or music compilations)
   and don't want to go through the hassle of acessing those dark websites full of ads,
   or grabbing my USB cable to transfer it.
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

    # download the file
    out_file = video.download(output_path=".")

    # save the file
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")


def generate_qr_code():
    """Creates QR code with IP address to be opened in cellphone."""

    # getting ip address
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)

    # creates qr code and saves it
    img = qrcode.make(f"http://{ip}:8080")
    type(img)
    img.save("qrcode.png")

    # open it on screen
    file = Image.open("qrcode.png")
    file.show()


def run_server():
    """Initiates a server that can be acessed via smartphone.
    Just add http://ip_address:8080 and voila.

    Credits to this: https://github.com/brandon-wallace/serve_files"""

    parser = argparse.ArgumentParser(
        description="Serve files from the current \
                                    directory."
    )

    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)

    parser.add_argument(
        "--host",
        default=ip,
        type=str,
        required=False,
        help="Specify the ip address to listen on.",
    )

    parser.add_argument(
        "--port",
        default=8080,
        type=int,
        required=False,
        help="Specify the port to listen on.",
    )

    args = parser.parse_args()

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((args.host, args.port), handler) as httpd:
        print(f"Server is listening on {args.host} on port {args.port}.")
        httpd.serve_forever()


def main():
    """Main."""

    download()
    generate_qr_code()
    run_server()


if __name__ == "__main__":
    main()
