import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
from sys import platform

if platform == "win32":
    print("Windows Detected!")
    import os
    import os.path
    from os import path

else:
    print("Windows only!")
    sys.exit()

visuals = Tk()

bg = "grey69"
fg = "black"
fg1 = "#990000"
sourcePath = " "
folderPath = " "
extension_dict = {
    "Data": ['.txt', '.pdf', '.doc', '.docx', '.odt', '.rtf',
             '.tex', '.wpd', '.ods', '.xls', '.xlsm', '.xlsx',
             '.pl', '.class', '.cpp', 'cs', '.h', '.java',
             '.php', '.sh', '.swift', '.vb', '.key', '.xml',
             '.odp', '.pps', '.ppt', '.pptx', '.csv', '.dat',
             '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.json'],

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
    folderPath = filedialog.askdirectory(initialdir='C:\\', title="Select a folder")
    if os.path.isdir(folderPath):
        folder_name_input['state'] = tk.NORMAL
        folder_name_label.config(fg=fg)
    else:
        folder_name_input['state'] = tk.DISABLED
        folder_name_label.config(fg=fg1)
    folder_label.config(text=folderPath)


def check_folder_input(sv):
    print(sv.get())
    if folder_name_input.get() == "":
        continue_button['state'] = tk.DISABLED
    else:
        continue_button['state'] = tk.NORMAL


# Make Directories
def make_dir(old_path, new_folder):
    new_path = os.path.join(old_path, new_folder)
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
        print("Directory {0} created".format(new_folder))
    else:
        print("Directory {0} found".format(new_folder))
    return new_path


# Clean Folder
def clean_up(path_txt, path_exe, path_main, path_media, path_compressed, path_clean):
    if path.exists(path_main):
        sourceFiles = os.listdir(path_clean)
        info_label.config(text=path_main)

        for file in sourceFiles:
            if file.endswith(tuple(extension_dict.get(list(extension_dict)[0]))):
                shutil.move(os.path.join(path_clean, file), os.path.join(path_txt, file))
            if file.endswith(tuple(extension_dict.get(list(extension_dict)[1]))):
                shutil.move(os.path.join(path_clean, file), os.path.join(path_exe, file))
            if file.endswith(tuple(extension_dict.get(list(extension_dict)[2]))):
                shutil.move(os.path.join(path_clean, file), os.path.join(path_media, file))
            if file.endswith(tuple(extension_dict.get(list(extension_dict)[3]))):
                shutil.move(os.path.join(path_clean, file), os.path.join(path_compressed, file))
        print("Files sorted in '% s'." % path_clean)
        with open("Paths.txt", 'w') as f:
            f.write('Path Storage:'
                    '\n \n{0}: '.format(list(extension_dict)[0]) + str(path_txt) +
                    '\n \n{0}: '.format(list(extension_dict)[1]) + str(path_exe) +
                    '\n \n{0}: '.format(list(extension_dict)[2]) + str(path_media) +
                    '\n \n{0}: '.format(list(extension_dict)[3]) + str(path_compressed) +
                    '\n \nMain: ' + str(path_main) +
                    '\n \nCreated using File Sorter - Windows.'
                    )
        txtFiles = os.listdir(path_txt)
        exeFiles = os.listdir(path_exe)
        mediaFiles = os.listdir(path_media)
        compressedFiles = os.listdir(path_compressed)
        info_label.config(text="Files in {0} moved to {1}.".format(path_clean, path_main))
        create_info(path_main, txtFiles, exeFiles, mediaFiles, compressedFiles)
    else:
        path_main = filedialog.askdirectory(initialdir='C:\\', title="Select a new folder")
        path_txt = make_dir(path_main, list(extension_dict)[0])
        path_exe = make_dir(path_main, list(extension_dict)[1])
        path_media = make_dir(path_main, list(extension_dict)[2])
        path_compressed = make_dir(path_main, list(extension_dict)[3])
        with open("Paths.txt", 'w') as f:
            f.write('Path Storage:'
                    '\n \n{0}: '.format(list(extension_dict)[0]) + str(path_txt) +
                    '\n \n{0}: '.format(list(extension_dict)[1]) + str(path_exe) +
                    '\n \n{0}: '.format(list(extension_dict)[2]) + str(path_media) +
                    '\n \n{0}: '.format(list(extension_dict)[3]) + str(path_compressed) +
                    '\n \nMain: ' + str(path_main) +
                    '\n \nCreated using File Sorter - Windows.'
                    )
        clean_up(path_txt,
                 path_exe,
                 path_main,
                 path_media,
                 path_compressed,
                 path_main)


# Create Text Doc containing moved items
def create_info(path_main, txt_files, exe_files, media_files, compressed_files):
    txtFile = [t for t in txt_files if t.endswith(tuple(extension_dict.get(list(extension_dict)[0])))]
    exeFile = [e for e in exe_files if e.endswith(tuple(extension_dict.get(list(extension_dict)[1])))]
    mediaFile = [m for m in media_files if m.endswith(tuple(extension_dict.get(list(extension_dict)[2])))]
    compressedFile = [c for c in compressed_files if c.endswith(tuple(extension_dict.get(list(extension_dict)[3])))]

    path_info = make_dir(path_main, "Info")

    with open(path_info + "/Clean Up Info.txt", 'w') as f:
        f.write('The path specified has been organized throughout the folders. '
                '\n \n{0} Files: '.format(list(extension_dict)[0]) + str(txtFile) +
                '\n \n{0} Files: '.format(list(extension_dict)[1]) + str(exeFile) +
                '\n \n{0} Files: '.format(list(extension_dict)[2]) + str(mediaFile) +
                '\n \n{0} Files: '.format(list(extension_dict)[3]) + str(compressedFile) +
                '\n \nCreated using File Sorter - Windows.'
                )
    print("Process Completed.")


# Sort files in folder
def sort():
    print("Sorted")
    path_storage = open("Paths.txt")
    all_paths = path_storage.readlines()
    text = all_paths[2].split(' ', 1)
    exe = all_paths[4].split(' ', 1)
    media = all_paths[6].split(' ', 1)
    compressed = all_paths[8].split(' ', 1)
    paths = all_paths[10].split(' ', 1)

    path_text = text[1].strip()
    path_exe = exe[1].strip()
    path_media = media[1].strip()
    path_compressed = compressed[1].strip()
    path_main = paths[1].strip()

    clean_up(path_text, path_exe, path_main, path_media, path_compressed, path_main)


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
    folder_name_label.config(fg=fg1)
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
    path_Txt = make_dir(path_main, list(extension_dict)[0])
    path_Exe = make_dir(path_main, list(extension_dict)[1])
    path_Media = make_dir(path_main, list(extension_dict)[2])
    path_Compressed = make_dir(path_main, list(extension_dict)[3])
    os.startfile(path_main)
    clean_up(path_Txt,
             path_Exe,
             path_main,
             path_Media,
             path_Compressed,
             sourcePath)


if __name__ == '__main__':

    visuals.title("File Sorter")
    visuals.config(bg="grey80")
    visuals.wm_minsize(width=413, height=168)
    visuals.maxsize(width=413, height=168)

    keyboard_track = StringVar()
    keyboard_track.trace("w", lambda name, index, mode, sv=keyboard_track: check_folder_input(sv))

    # Initiate Gui

    find_source_path_button = Button(visuals,
                                     text="Select Folder to Clean", width=25,
                                     bg=bg,
                                     command=lambda: find_source_path())
    find_source_path_button.grid(column=0, row=1)

    find_folder_path_button = Button(visuals,
                                     text="Select Location for New Folder", width=25,
                                     bg=bg,
                                     command=lambda: find_folder_path(),
                                     state=tk.DISABLED)
    find_folder_path_button.grid(column=0, row=2)

    continue_button = Button(visuals,
                             text="Continue", width=25,
                             bg=bg,
                             command=lambda: main(),
                             state=tk.DISABLED)
    continue_button.grid(column=0, row=4)

    exit_button = Button(visuals,
                         text="Close",
                         bg=bg,
                         width=5,
                         command=lambda: sys.exit()
                         )
    exit_button.grid(column=2, row=1)

    new_button = Button(visuals,
                        text="Reset",
                        bg=bg,
                        width=5,
                        command=lambda: reset())
    new_button.grid(column=2, row=2)

    folder_name_input = tk.Entry(visuals, width=30,
                                 state=tk.DISABLED,
                                 textvariable=keyboard_track)
    folder_name_input.grid(column=1, row=3)

    folder_name_label = tk.Label(visuals,
                                 text="Folder Name:", width=25,
                                 borderwidth=4,
                                 bg=bg,
                                 relief="raised",
                                 fg=fg1)
    folder_name_label.grid(column=0, row=3)

    info_label = tk.Label(visuals,
                          text=" ",
                          borderwidth=2,
                          relief="flat",
                          fg=fg,
                          bg="grey",
                          width=25)
    info_label.grid(column=1, row=4)

    source_label = tk.Label(visuals,
                            text=" ",
                            borderwidth=2,
                            relief="flat",
                            fg=fg,
                            bg="grey",
                            width=25)
    source_label.grid(column=1, row=1)

    folder_label = tk.Label(visuals,
                            text=" ",
                            borderwidth=2,
                            relief="flat",
                            fg=fg,
                            bg="grey",
                            width=25)
    folder_label.grid(column=1, row=2)

    title_label = tk.Label(visuals,
                           text="File Sorter",
                           borderwidth=4,
                           relief="raised",
                           fg=fg,
                           bg=bg,
                           font='Helvetica 18 bold',
                           width=27)
    title_label.grid(column=0, row=0, columnspan=3)

    # Automatically sort folder when items are added to path_main

    run_in_background_button = Button(visuals, text="Run Automatic Sorting",
                                      bg=bg, width=58, command=lambda: sort()
                                      )
    run_in_background_button.grid(column=0, row=5, columnspan=3)
    run_in_background_button['state'] = tk.NORMAL

    try:
        logo = PhotoImage(file='Logo.png')
        my_logo = Label(visuals, image=logo, width=40, height=40)
        my_logo.grid(column=2, row=3, rowspan=2)
    except TclError:
        pass

visuals.mainloop()
