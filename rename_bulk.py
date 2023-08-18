import os

def rename_files(directory_path):
    files = os.listdir(directory_path)

    for i, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = 'Test-' + str(i) + file_extension
        old_file_path = os.path.join(directory_path, file_name)
        new_file_path = os.path.join(directory_path, new_file_name)
        os.rename(old_file_path, new_file_path)

# Specify the directory path where the files are located
directory_path = "test dataset"

# Call the rename_files function with the directory path
rename_files(directory_path)
