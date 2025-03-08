import os
import shutil

def get_user_input():
    input_dir = input("Enter the input directory: ")
    dir_to_compare = input("Enter the directory to compare: ")
    output_dir = input("Enter the destination directory: ")
    return input_dir, dir_to_compare, output_dir

def compare_and_copy(input_dir, dir_to_compare, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Walk through the directory to compare
    for root, dirs, files in os.walk(dir_to_compare):
        # Get the relative path from the dir_to_compare
        relative_path = os.path.relpath(root, dir_to_compare)
        
        # Construct corresponding paths in the input and output directories
        input_path = os.path.join(input_dir, relative_path)
        output_path = os.path.join(output_dir, relative_path)

        # Check if the corresponding directory exists in the input directory
        if os.path.exists(input_path):
            # Create the directory in the output directory if it doesn't exist
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # Copy matching files
            for file in files:
                input_file_path = os.path.join(input_path, file)
                compare_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_path, file)

                # Check if the file exists in the input directory
                if os.path.exists(input_file_path):
                    shutil.copy2(input_file_path, output_file_path)
                    print(f"Copied: {input_file_path} -> {output_file_path}")
                else:
                    print(f"File does not exist in input directory: {compare_file_path}")

            # Copy matching directories
            for dir in dirs:
                input_dir_path = os.path.join(input_path, dir)
                compare_dir_path = os.path.join(root, dir)
                output_dir_path = os.path.join(output_path, dir)

                # Check if the directory exists in the input directory
                if os.path.exists(input_dir_path):
                    shutil.copytree(input_dir_path, output_dir_path)
                    print(f"Copied directory: {input_dir_path} -> {output_dir_path}")
                else:
                    print(f"Directory does not exist in input directory: {compare_dir_path}")
        else:
            print(f"Directory does not exist in input directory: {input_path}")

def main():
    input_dir, dir_to_compare, output_dir = get_user_input()
    
    # Validate input directories
    if not os.path.exists(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return
    if not os.path.exists(dir_to_compare):
        print(f"Directory to compare does not exist: {dir_to_compare}")
        return
    
    compare_and_copy(input_dir, dir_to_compare, output_dir)
    print("Copy operation completed.")

if __name__ == "__main__":
    main()
