import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import sys

def process_file(src_file, dest_dir):
    _, extension = os.path.splitext(src_file)
    extension = extension[1:] if extension else "no extension"

    dest_path = os.path.join(dest_dir, extension)
    os.makedirs(dest_path, exist_ok = True)

    shutil.copy(src_file, os.path.join(dest_path, os.path.basename(src_file)))

def process_directory(src_dir, dest_dir):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                src_file = os.path.join(root, file)
                executor.submit(process_file, src_file, dest_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage : python script.py <source_directory> [<destination_directory]")
        return
    
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    process_directory(src_dir, dest_dir)

if __name__ == "__main__":
    main()

# Example of usage
# Enter in cmd: python this_file.py /path/to/non-sorted_directory path/to/directory/for/sorting