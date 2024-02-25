# lazy-transfer

1. Extracts the .mp3 of a YouTube video.
2. Saves it on current directory.
3. Starts a HTTP server.
4. Generates a QR code for connecting to HTTP server on cellphone.
5. Now you can download the file to your phone, no need for cables.
    

Very useful when I need to download a live set (or music compilations) and don't want to go through the hassle of acessing those dark websites full of ads, or grabbing my USB cable to transfer it.

## How to use:

* clone the repo
* create/activate virtual environment
* `pip install -r requirements.txt`
* `python main.py`

Script will ask for a YouTube URL and display a QR code afterwards. 

Just point your camera to it and download your file to your phone.

## EVEN MORE LAZY (if you have Termux in your Android)

* open Termux
* git clone
* `python very_lazy.py`

Script will ask for a YouTube URL and save it directly to your Downloads folder in your phone.