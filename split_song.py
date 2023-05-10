import subprocess
import shutil


def execute(filesave, fileopen):
    """
    @article{spleeter2020,
    doi = {10.21105/joss.02154},
    url = {https://doi.org/10.21105/joss.02154},
    year = {2020},
    publisher = {The Open Journal},
    volume = {5},
    number = {50},
    pages = {2154},
    author = {Romain Hennequin and Anis Khlif and Felix Voituret and Manuel Moussallam},
    title = {Spleeter: a fast and efficient music source separation tool with pre-trained models},
    journal = {Journal of Open Source Software},
    note = {Deezer Research}
    }
    https://github.com/deezer/spleeter
    """
    amount = 5
    command = "python3 -m spleeter separate -p spleeter:" + str(
        amount) + "stems -o " + filesave + " " + '"' + fileopen + '"'
    subprocess.run(command)


def archive_make(filesave, file_name, file_name_no_extension):
    archive = shutil.make_archive(filesave + "/" + file_name, 'zip', filesave + "/" + file_name_no_extension)
    shutil.rmtree(filesave + "/" + file_name_no_extension)
