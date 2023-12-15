import subprocess
import os

def create_zip_in_memory(folder=None, files=None):
    if folder:
        files_names = os.listdir(folder)
        files = [f'{folder}/{file}' for file in files_names]

    zip_command = ['zip', '-r', '-', *files]

    zip_process = subprocess.Popen(zip_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    zip_output, zip_err = zip_process.communicate()

    return zip_output


photo_content = create_zip_in_memory(folder='for_archive')

with open("photos.zip", "wb") as zip_file:
    zip_file.write(photo_content)

