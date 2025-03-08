import os
import shutil

def get_user_input():
    """Prompt the user for input and return the directory paths."""
    input_dir = input("Enter the input directory: ")
    dir_to_compare = input("Enter the directory to compare: ")
    output_dir = input("Enter the destination directory: ")
    example_etc_dir = os.path.join(output_dir, "example_etc")
    return input_dir, dir_to_compare, output_dir, example_etc_dir

def ensure_directory_exists(directory):
    """Ensure a directory exists. If not, create it."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}")
        raise

def copy_file(src, dst, description=""):
    """Copy a file from src to dst and print a message."""
    try:
        shutil.copy2(src, dst)
        print(f"Copied {description}: {src} -> {dst}")
    except OSError as e:
        print(f"Error copying file {src} to {dst}: {e}")

def copy_directory(src, dst):
    """Copy a directory from src to dst and print a message."""
    try:
        shutil.copytree(src, dst)
        print(f"Copied directory: {src} -> {dst}")
    except OSError as e:
        print(f"Error copying directory {src} to {dst}: {e}")

def create_symlink(target, link_path):
    """Create a symbolic link pointing to the target."""
    try:
        os.symlink(target, link_path)
        print(f"Created soft link: {link_path} -> {target}")
    except OSError as e:
        print(f"Error creating symlink {link_path}: {e}")

def compare_and_copy(input_dir, dir_to_compare, output_dir, example_etc_dir):
    """Compare directories and copy matching files and directories."""
    # Ensure output and example_etc directories exist
    ensure_directory_exists(output_dir)
    ensure_directory_exists(example_etc_dir)

    # Walk through the directory to compare
    for root, dirs, files in os.walk(dir_to_compare):
        relative_path = os.path.relpath(root, dir_to_compare)
        input_path = os.path.join(input_dir, relative_path)
        output_path = os.path.join(output_dir, relative_path)
        example_etc_path = os.path.join(example_etc_dir, relative_path)

        # Check if the corresponding directory exists in the input directory
        if not os.path.exists(input_path):
            print(f"Directory does not exist in input directory: {input_path}")
            continue

        # Ensure output and example_etc subdirectories exist
        ensure_directory_exists(output_path)
        ensure_directory_exists(example_etc_path)

        # Copy matching files
        for file in files:
            input_file_path = os.path.join(input_path, file)
            output_file_path = os.path.join(output_path, file)
            example_etc_file_path = os.path.join(example_etc_path, file)

            if os.path.exists(input_file_path):
                copy_file(input_file_path, output_file_path, "to output")
                copy_file(input_file_path, example_etc_file_path, "to example_etc")
            else:
                print(f"File does not exist in input directory: {os.path.join(root, file)}")

        # Copy matching directories
        for dir in dirs:
            input_dir_path = os.path.join(input_path, dir)
            output_dir_path = os.path.join(output_path, dir)
            example_etc_dir_path = os.path.join(example_etc_path, dir)

            if os.path.exists(input_dir_path):
                copy_directory(input_dir_path, output_dir_path)
                # Create a symlink in example_etc pointing to the output directory
                create_symlink(os.path.abspath(output_dir_path), example_etc_dir_path)
            else:
                print(f"Directory does not exist in input directory: {os.path.join(root, dir)}")

def main():
    """Main function to execute the script."""
    try:
        input_dir, dir_to_compare, output_dir, example_etc_dir = get_user_input()

        # Validate input directories
        if not os.path.exists(input_dir):
            print(f"Input directory does not exist: {input_dir}")
            return
        if not os.path.exists(dir_to_compare):
            print(f"Directory to compare does not exist: {dir_to_compare}")
            return

        compare_and_copy(input_dir, dir_to_compare, output_dir, example_etc_dir)
        print("Copy operation completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
