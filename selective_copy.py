import os
import re
import shutil


def gather_input():
    return_list = [input("Enter the extension that you want to copy, in .abc form.\n"),
                   input("Enter the directory that you want to copy from.\n"),
                   input("Enter the directory that you want to copy to.\n")]
    if not os.path.exists(return_list[1]):
        exit("The directory you're copying from doesn't exist, aborting program.")
    return return_list


def create_destination_folder(new_folder_path, folder_ext_contents):
    edited_folder = new_folder_path + r"\%s" % folder_ext_contents
    if not os.path.isdir(edited_folder):
        os.makedirs(edited_folder)
    return edited_folder


def create_ext_regex(ext_string):
    ext_regex = re.compile(ext_string)
    return ext_regex


# Execution portion
# input_values = gather_input()
input_values = ['.docx', r'C:\Users\Garrett\Documents\Old Semester Resources', r"C:\Users\Garrett\Documents"]

new_folder_name = create_destination_folder(input_values[2], input_values[0])

extension_regex = create_ext_regex(input_values[0])
for folderName, subfolders, filenames in os.walk(input_values[1]):

    for filename in filenames:
        no_temp_regex = re.compile(r"~")
        mo_temp = no_temp_regex.search(filename)
        mo = extension_regex.search(filename)
        if mo is not None and mo_temp is None:
            file_dir = os.path.join(folderName, filename)
            shutil.copy(file_dir, new_folder_name)
