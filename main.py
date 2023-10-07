import fnmatch
import os
import shutil
import datetime


def search_files_and_directories(search_dir, search_term):
    matches = []

    for root, dirnames, filenames in os.walk(search_dir):
        # Search files
        for filename in filenames:
            if fnmatch.fnmatch(filename, search_term):
                matches.append(os.path.join(root, filename))

        # Search directories
        for dirname in dirnames:
            if fnmatch.fnmatch(dirname, search_term):
                matches.append(os.path.join(root, dirname))

    return matches




def sort_files():
    # Add your sorting logic here
    files = []
    directories = []

    for item in os.listdir():
        if os.path.isfile(item):
            files.append(item)
        elif os.path.isdir(item):
            directories.append(item)

    files.sort()
    directories.sort()

    print("\nSorted Files:")
    for file in files:
        print(file)

    print("\nSorted Directories:")
    for directory in directories:
        print(directory)


def view_file_properties():
    file_name = input("\nEnter the name of the file: ")

    if os.path.isfile(file_name):
        file_stat = os.stat(file_name)
        file_size = file_stat.st_size

        # Convert last modified time to a readable format
        last_modified = datetime.datetime.fromtimestamp(file_stat.st_mtime)
        last_modified_str = last_modified.strftime("%Y-%m-%d %H:%M:%S")

        print("File Properties:")
        print("Name:", file_name)
        print("Size:", file_size, "bytes")
        print("Last Modified:", last_modified_str)

    else:
        print("File not found.")


def menu():
    print("Welcome to the File Explorer!")
    while True:
        print("\nPlease choose an option:")
        print("1. List files in current directory")
        print("2. Create a new directory")
        print("3. Delete a directory or file")
        print("4. Rename a directory or file")
        print("5. Copy a file")
        print("6. Move a file or directory")
        print("7. Sort files")
        print("8. View file properties")
        print("9. Change directory")  # Added option to change directory
        print("10. Create a file")  # Added option to create a file
        print("11. Search File or Directory")
        print("0. Exit\n")
        choice = input("> ")

        if choice == "1":
            list_files()
        elif choice == "2":
            create_directory()
        elif choice == "3":
            delete_file_or_directory()
        elif choice == "4":
            rename_file_or_directory()
        elif choice == "5":
            source = input("Enter the path of the file or directory to copy: ")
            destination = input("Enter the destination path: ")

            copy_file_or_directory(source, destination)
        elif choice == "6":
            move_file_or_directory()
        elif choice == "7":
            sort_files()
        elif choice == "8":
            file_path = input("Enter the path of the file: ")
            view_file_properties()
        elif choice == "9":  # Handle the option to change directory
            change_directory()
        elif choice == "10":  # Handle the option to create a file
            create_file()
        elif choice == "11":
            search_dir = input("Enter the directory to search: ")
            search_term = input("Enter the search term: ")
            results = search_files_and_directories(search_dir, search_term)

            if results:
                print("Matching files and directories:")
                for path in results:
                    print(path)
            else:
                print("No matching files or directories found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def list_files():
    print("\nCurrent directory: ", os.getcwd())
    print("Files and directories:")
    for item in os.listdir():
        print(item)


def create_directory():
    dir_name = input("\nEnter name of new directory: ")
    if os.path.exists(dir_name):
        print("Directory already exists.")
    else:
        os.mkdir(dir_name)
        print("Directory created.")

    # dir_name = input("\nEnter name of new directory: ")
    # for item in os.listdir():
    #     if(item == dir_name):
    #         print("Directory is already Exist!")
    #
    #     else:
    #         os.mkdir(dir_name)
    #         print("Directory created.")


def delete_file_or_directory():
    file_or_dir_name = input("\nEnter name of file or directory to delete: ")
    if os.path.isfile(file_or_dir_name):
        os.remove(file_or_dir_name)
        print("File deleted.")
    elif os.path.isdir(file_or_dir_name):
        shutil.rmtree(file_or_dir_name)
        print("Directory deleted.")
    else:
        print("File or directory not found.")


def rename_file_or_directory():
    old_name = input("\nEnter the name of the file or directory to rename: ")
    new_name = input("Enter the new name: ")
    os.rename(old_name, new_name)
    print("File or directory renamed.")


def copy_file_or_directory(source, destination):
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print("File copied.")
    elif os.path.isdir(source):
        shutil.copytree(source, destination)
        print("Directory copied.")
    else:
        print("Source file or directory does not exist.")


def move_file_or_directory():
    source = input("\nEnter the name of the file or directory to move: ")
    destination = input("Enter the name of the destination directory: ")
    shutil.move(source, destination)
    print("File or directory moved.")


def change_directory():
    new_directory = input("Enter the path of the new directory: ")
    if os.path.isdir(new_directory):
        os.chdir(new_directory)
        print("Directory changed.")
    else:
        print("Invalid directory path.")


def create_file():
    file_name = input("Enter name of new file: ")
    if os.path.exists(file_name):
        print("File already exists.")
    else:
        with open(file_name, 'w') as f:
            print("File created.")


menu()
