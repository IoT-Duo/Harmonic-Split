## Harmonic Split - Web Application Consisting of Guitar Tuner Made in JavaScript and AI Song Splitter - Spleeter Made in Python
### About This Web Application:
Made by: 

Frimu Aurel-Viorel:
- [GitHub](https://github.com/AurasV)

Nisipeanu Ionut:
- [Github](https://github.com/Nasapan23)

Made for the Scientific Communication Session 2023 Organized by:

`Politehnica University of Bucharest - Faculty of Engineering in Foreign Languages`
- English link - [here](http://fils.upb.ro/en/scientific-communication-session/)
- Romanian link - [here](http://fils.upb.ro/ro/sesiune-comunicari-stiintifice/)
- French link - [here](http://fils.upb.ro/fr/seance-de-communication-scientifique/)

Got 2nd place in category - `Computers and Information Technology in English`
### Main Page
![Main Page](https://github.com/AurasV/Guitar-Tuner-and-AI-Song-Splitter-Web-Application/assets/80701407/d376a008-55f3-455a-bed0-8fdcef5abecc)
### Guitar Tuner Page
![Guitar Tuner Page](https://github.com/AurasV/Guitar-Tuner-and-AI-Song-Splitter-Web-Application/assets/80701407/dfc60c7e-4991-4d7d-b89e-a80fccfa827d)
### Audio Splitter Page
![Audio Splitter Page](https://github.com/AurasV/Guitar-Tuner-and-AI-Song-Splitter-Web-Application/assets/80701407/ac041b48-eb03-448c-bd2c-63842e47eb6f)

# Usage:
#### *Python Version*:
Built and tested on Python 3.10.6
#### *Operating System*:
Built and tested on Windows 10 Pro version 21H1, should (in theory) work on most Windows 10 versions and Windows 11 
#### *Necessary Libraries / Modules*:
- werkzeug.utils
- flask
- spleeter
#### *How to Get Them?*
- `pip install werkzeug.utils`
- `pip install flask`
- `pip install spleeter`
#### *Necessary Changes to the Code:*
Change `UPLOAD_FOLDER = 'YOUR UPLOAD FOLDER GOES HERE'` from line 10 of `flask_main.py` to the folder you want it to save the archives of the split songs - use `os.path.join('app', 'subdir', 'dir', 'filename.foo')` for system agnostic paths!  (as of right now the app doesn't delete the archives or the songs after sending, will probably add in a future update)
#### *The AI Model:*
As of right now the file size limit GitHub has doesn't let me upload the model but it can be downloaded from [here](https://github.com/deezer/spleeter/releases/download/v1.4.0/5stems.tar.gz) then the content should be unarchived twice using [7-zip](https://www.7-zip.org/) and placed in the `pretrained_models/5stems` folder
#### *Running it:*
After running the `flask_main.py` file, the web application will be available at `http://127.0.0.1:5000` / `localhost:5000` so just navigate to that address in your browser of choice and start using the app, for the song splitter only you can use my audio splitter only found [here](https://github.com/AurasV/Audio-Splitter)
#### *Recommended Specs:*
It's better to use a machine with a beefier CPU and at least 8GB of RAM as the AI model runs on the CPU and uses around 4GB of RAM per song that's being split

Tested on a laptop with:
- Ryzen 7 5800H
- 16GB RAM / 32GB RAM

