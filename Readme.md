# Convert Youtube Videos to MP4 or MP3

I made this app to be able to convert youtube videos into mp4 or mp3 files easilly and efficiently. There is a webapp or a command line interface that you can use. The webapp is built using the Flask Framework for Python. The command line is built using plain python.

## How to use

### If you want to use in command Line:

    - Run Python main.py

### Run as Flask App:

    - Run Python app.py

## How it Works

### Endpoint: **/**

This endpoint is the landing page, On This landing page there is two links Depending on which format you want to convert to

- **MP3**
  - Clicking MP3 will redirect you to **/audio**
- **MP4**
  - Clicking MP4 will redirect you to **/video**
    <br/>

### Endpoint: **/audio**

This endpoint will render a form, In this Form the user will input Youtube link to any video or audio that they want converted to MP3

- **Input Box**

  - User will enter link inside

- **On Submit Click**
  - User will be redirected to **/audio_download**
    <br/>

### Endpoint: **/video**

This endpoint will render a form, In this Form the user will input Youtube link to any video that they want converted to MP4

- **Input Box**

  - User will enter link inside

- **On Submit Click**
  - User will be redirected to **/video_download**
    <br/>

### Endpoint **/audio_download**

- Method= POST
- This endpoint will download the Youtube video as MP3
- Downloaded to working directory
-

### Endpoint **/video_download**

- Method= POST
- This endpoint will download the Youtube video as MP4
- Downloaded to working directory
