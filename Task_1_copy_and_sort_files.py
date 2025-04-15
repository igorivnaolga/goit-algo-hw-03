import os
import shutil
import sys

def copy_and_sort_files(src, dst):
    """Recursively copy files from src to dst, sorting them by file extension."""
    try:
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            if os.path.isdir(src_path):
                # Recursively process subdirectories
                copy_and_sort_files(src_path, dst)
            elif os.path.isfile(src_path):
                # Extract extension and prepare destination folder
                _, ext = os.path.splitext(item)
                ext = ext[1:] if ext else "no_extension"
                ext_folder = os.path.join(dst, ext)

                os.makedirs(ext_folder, exist_ok=True)

                dst_path = os.path.join(ext_folder, item)

                if os.path.exists(dst_path):
                    print(f"Already exists: {dst_path}")
                else:
                    try:
                        shutil.copy(src_path, dst_path)
                        print(f"Copied: {src_path} -> {dst_path}")
                    except Exception as e:
                        print(f"Failed to copy {src_path}: {e}")
    except Exception as e:
        print(f"Error accessing {src}: {e}")

def main():
    # Read command line arguments manually
    if len(sys.argv) < 2:
        print("Usage: Task_1_copy_and_sort_files.py <source_dir> [destination_dir]")
        return

    source = os.path.abspath(sys.argv[1])
    destination = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.abspath("dest")

    if not os.path.isdir(source):
        print(f"Error: Source path '{source}' is not a valid directory.")
        return

    os.makedirs(destination, exist_ok=True)
    copy_and_sort_files(source, destination)

if __name__ == "__main__":
    main()
