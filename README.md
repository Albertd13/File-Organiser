# File-Organiser
File Organiser is a really simple script to organise your files by their extensions (using pathlib module)

## Usage Notes
Run file_organiser.py with python 3.4 and above. Copy paste the path (or address) of the directory you want to organise when prompted. To customise directory names and extensions, 
simply open my_categorisation.json and edit the file directly. If you broke something when editing my_categorisation, just delete it to restore defaults upon next run.

## Limitations
1. Will skip over organisation of any child directories.
2. Script will only sort one directory at a time. (may add functionality for this later)
3. Limited number of extensions included by default and does not handle duplicate entries in json file.
   
## Future Updates
1. Code in a way to reorganise files according to a new categorisation if changes are made to the my_categorisation file, without manually extracting files from each created directory.
