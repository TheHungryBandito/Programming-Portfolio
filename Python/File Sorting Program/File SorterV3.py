import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys

mustard = "#f3ca20"
black = "grey10"
sourcePath = " "
folderPath = " "
txt_Folder = "Data"
exe_Folder = "Applications"
compressed_Folder = "Compressed"
media_Folder = "Media"

extension_dict = {
    "Data": ['.txt', '.pdf', '.doc', '.docx', '.odt', '.rtf',
             '.tex', '.wpd', '.ods', '.xls', '.xlsm', '.xlsx',
             '.pl', '.class', '.cpp', 'cs', '.h', '.java',
             '.php', '.sh', '.swift', '.vb', '.key', '.xml',
             '.odp', '.pps', '.ppt', '.pptx', '.csv', '.dat',
             '.db', '.dbf', '.log', '.mdb', '.sav', '.sql'],

    "Applications": ['.exe', '.lnk', '.url', '.apk', '.bat', '.bin', '.cgi',
                     '.pl', '.com', '.gadget', '.jar', '.msi', '.py', '.wsf'],

    "Media": ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
              '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob',
              '.wmv', '.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg',
              '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.aif',
              '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav',
              '.wma', '.wpl'],

    "Compressed": ['.7z', '.arj', '.deb', '.pkg',
                   '.rar', '.rpm', '.tar.gz',
                   '.z', '.zip']
}

visuals = Tk()
visuals.title("File Sorter")
visuals.config(background=black)
visuals.wm_minsize(width=414, height=140)
visuals.maxsize(width=414, height=140)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: check_folder_input(sv))
# Logo
logo = PhotoImage(file='logo.png')
my_logo = Label(visuals, image=logo, width=40, height=40)
# Initiate Gui
find_source_path_button = Button(visuals,
                                 text="Select Folder to Clean", width=25,
                                 bg=mustard,
                                 command=lambda: find_source_path())

find_folder_path_button = Button(visuals,
                                 text="Select Location for New Folder", width=25,
                                 bg=mustard,
                                 command=lambda: find_folder_path(),
                                 state=tk.DISABLED)

continue_button = Button(visuals,
                         text="Continue", width=25,
                         bg=mustard,
                         command=lambda: main(),
                         state=tk.DISABLED)

exit_button = Button(visuals,
                     text="Close",
                     bg=mustard,
                     width=5,
                     command=lambda: sys.exit())
new_button = Button(visuals,
                    text="Reset",
                    bg=mustard,
                    width=5,
                    command=lambda: reset())

folder_name_label = tk.Label(visuals,
                             text="Folder Name:", width=25,
                             borderwidth=4,
                             bg=mustard,
                             relief="raised",
                             fg='#f00')
folder_name_input = tk.Entry(visuals, width=30,
                             state=tk.DISABLED,
                             textvariable=sv)
title_label = tk.Label(visuals,
                       text="File Sorter V3",
                       borderwidth=4,
                       relief="raised",
                       fg=mustard,
                       bg=black,
                       font='Helvetica 18 bold',
                       width=27)
info_label = tk.Label(visuals,
                      text=" ",
                      borderwidth=2,
                      relief="flat",
                      fg=mustard,
                      bg="grey",
                      width=25)
source_label = tk.Label(visuals,
                        text=" ",
                        borderwidth=2,
                        relief="flat",
                        fg=mustard,
                        bg="grey",
                        width=25)
folder_label = tk.Label(visuals,
                        text=" ",
                        borderwidth=2,
                        relief="flat",
                        fg=mustard,
                        bg="grey",
                        width=25)


# Find Path to messy Folder
def find_source_path():
    global sourcePath
    sourcePath = filedialog.askdirectory(initialdir='C:\\', title="Select a folder")
    if os.path.isdir(sourcePath):
        find_folder_path_button['state'] = tk.NORMAL
    else:
        find_folder_path_button['state'] = tk.DISABLED
    source_label.config(text=sourcePath)


# Find Path to new folder
def find_folder_path():
    global folderPath
    folderPath = filedialog.askdirectory(initialdir='C:/', title="Select a folder")
    if os.path.isdir(folderPath):
        folder_name_input['state'] = tk.NORMAL
        folder_name_label.config(fg='black')
    else:
        folder_name_input['state'] = tk.DISABLED
        folder_name_label.config(fg='#f00')
    folder_label.config(text=folderPath)


def check_folder_input(sv):
    print(sv.get())
    if folder_name_input.get() == "":
        continue_button['state'] = tk.DISABLED
    else:
        continue_button['state'] = tk.NORMAL


# Make Directories
def make_dir(path, new_folder):
    new_path = os.path.join(path, new_folder)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
        print("Directory {0} created".format(new_folder))
    else:
        print("Directory {0} found".format(new_folder))
    return new_path


# Clean Folder
def clean_up(path_txt, path_exe, path_main, path_media, path_compressed):
    sourceFiles = os.listdir(sourcePath)
    info_label.config(text=path_main)

    for file in sourceFiles:
        if file.endswith(tuple(extension_dict.get("Data"))):
            shutil.move(os.path.join(sourcePath, file), os.path.join(path_txt, file))
        if file.endswith(tuple(extension_dict.get("Applications"))):
            shutil.move(os.path.join(sourcePath, file), os.path.join(path_exe, file))
        if file.endswith(tuple(extension_dict.get("Media"))):
            shutil.move(os.path.join(sourcePath, file), os.path.join(path_media, file))
        if file.endswith(tuple(extension_dict.get("Compressed"))):
            shutil.move(os.path.join(sourcePath, file), os.path.join(path_compressed, file))
    print("Files sorted in '% s'." % sourcePath)
    txtFiles = os.listdir(path_txt)
    exeFiles = os.listdir(path_exe)
    mediaFiles = os.listdir(path_media)
    compressedFiles = os.listdir(path_compressed)
    info_label.config(text="Files in {0} moved to {1}.".format(sourcePath, path_main))
    create_info(path_main, txtFiles, exeFiles, mediaFiles, compressedFiles)


# Create Text Doc containing moved items
def create_info(path_main, txtFiles, exeFiles, mediaFiles, compressedFiles):
    txtFile = [t for t in txtFiles if t.endswith(tuple(extension_dict.get("Data")))]
    exeFile = [e for e in exeFiles if e.endswith(tuple(extension_dict.get("Applications")))]
    mediaFile = [m for m in mediaFiles if m.endswith(tuple(extension_dict.get("Media")))]
    compressedFile = [c for c in compressedFiles if c.endswith(tuple(extension_dict.get("Compressed")))]

    with open(path_main + "/Clean Up Info.txt", 'w') as f:
        f.write('The path specified has been organized throughout the folders. '
                '\n \nData Files: ' + str(txtFile) +
                '\n \nApplications: ' + str(exeFile) +
                '\n \nMedia Files: ' + str(mediaFile) +
                '\n \nCompressed Files: ' + str(compressedFile) +
                '\n \nCreated using File Sorter.'
                )
    os.startfile(path_main)
    print("Process Completed.")


# Reset tkinter window
def reset():
    global sourcePath
    global folderPath
    sourcePath = " "
    folderPath = " "
    source_label.config(text="")
    folder_label.config(text="")
    info_label.config(text="")
    folder_name_input.delete(0, END)
    folder_name_label.config(fg="#f00")
    if find_source_path_button['state'] == tk.DISABLED:
        find_source_path_button['state'] = tk.NORMAL
    if find_folder_path_button['state'] == tk.NORMAL:
        find_folder_path_button['state'] = tk.DISABLED
    if continue_button['state'] == NORMAL:
        continue_button['state'] = tk.DISABLED
    if folder_name_input['state'] == tk.NORMAL:
        folder_name_input['state'] = tk.DISABLED


# Assign Dir/s
def main():
    find_source_path_button['state'] = tk.DISABLED
    find_folder_path_button['state'] = tk.DISABLED
    continue_button['state'] = tk.DISABLED
    directory = folder_name_input.get()
    path_main = make_dir(folderPath, directory)
    path_Txt = make_dir(path_main, txt_Folder)
    path_Exe = make_dir(path_main, exe_Folder)
    path_Media = make_dir(path_main, media_Folder)
    path_Compressed = make_dir(path_main, compressed_Folder)
    clean_up(path_Txt, path_Exe, path_main,
             path_Media,
             path_Compressed)


# Create Gui
def initiate_window():
    # GUI Loop
    find_source_path_button.grid(column=0, row=1)
    find_folder_path_button.grid(column=0, row=2)
    continue_button.grid(column=0, row=4)
    exit_button.grid(column=2, row=1)
    new_button.grid(column=2, row=2)
    folder_name_input.grid(column=1, row=3)
    folder_name_label.grid(column=0, row=3)
    info_label.grid(column=1, row=4)
    source_label.grid(column=1, row=1)
    folder_label.grid(column=1, row=2)
    title_label.grid(column=0, row=0, columnspan=3)
    my_logo.grid(column=2, row=3, rowspan=2)

    visuals.mainloop()


if __name__ == '__main__':
    initiate_window()
