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
    os.makedirs(edited_folder)


def create_ext_regex(ext_string):
    ext_regex = re.compile(r"%s" % ext_string)


input_values = gather_input()
input_values = ['.txt', r'C:\Users\Garrett\Documents\Technical Communication', r"C:\Users\Garrett\Documents"]
for i in range(len(input_values)):
    print(input_values[i])
create_destination_folder(input_values[2], input_values[0])
