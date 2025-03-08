import os
import shutil

def get_user_input():
    input_dir = input("Enter the input directory: ")
    dir_to_compare = input("Enter the directory to compare: ")
    output_dir = input("Enter the destination directory: ")
    example_etc_dir = os.path.join(output_dir, "example_etc")
    return input_dir, dir_to_compare, output_dir, example_etc_dir

def compare_and_copy(input_dir, dir_to_compare, output_dir, example_etc_dir):

    # Ensure the output and example_etc directories exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(example_etc_dir):
        os.makedirs(example_etc_dir)

    # Walk through the directory to compare
    for root, dirs, files in os.walk(dir_to_compare):
        # Get the relative path from the dir_to_compare
        relative_path = os.path.relpath(root, dir_to_compare)
        
        # Construct corresponding paths in the input, output, and example_etc directories
        input_path = os.path.join(input_dir, relative_path)
        output_path = os.path.join(output_dir, relative_path)
        example_etc_path = os.path.join(example_etc_dir, relative_path)

        # Check if the corresponding directory exists in the input directory
        if os.path.exists(input_path):
            # Create the directory in the output and example_etc directories if they don't exist
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            if not os.path.exists(example_etc_path):
                os.makedirs(example_etc_path)

            # Copy matching files to both output and example_etc directories
            for file in files:
                input_file_path = os.path.join(input_path, file)
                compare_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_path, file)
                example_etc_file_path = os.path.join(example_etc_path, file)

                # Check if the file exists in the input directory
                if os.path.exists(input_file_path):
                    shutil.copy2(input_file_path, output_file_path)
                    shutil.copy2(input_file_path, example_etc_file_path)
                    print(f"Copied: {input_file_path} -> {output_file_path}")
                    print(f"Copied to example_etc: {input_file_path} -> {example_etc_file_path}")
                else:
                    print(f"File does not exist in input directory: {compare_file_path}")

            # Copy matching directories to the output directory
            for dir in dirs:
                input_dir_path = os.path.join(input_path, dir)
                compare_dir_path = os.path.join(root, dir)
                output_dir_path = os.path.join(output_path, dir)

                # Check if the directory exists in the input directory
                if os.path.exists(input_dir_path):
                    shutil.copytree(input_dir_path, output_dir_path)
                    print(f"Copied directory: {input_dir_path} -> {output_dir_path}")

                    # Create a soft link in example_etc pointing to the directory in the output directory (using absolute path)
                    example_etc_dir_path = os.path.join(example_etc_path, dir)
                    if not os.path.exists(example_etc_dir_path):
                        # Use absolute path for the target of the soft link
                        absolute_output_dir_path = os.path.abspath(output_dir_path)
                        os.symlink(absolute_output_dir_path, example_etc_dir_path)
                        print(f"Created soft link in example_etc: {example_etc_dir_path} -> {absolute_output_dir_path}")
                else:
                    print(f"Directory does not exist in input directory: {compare_dir_path}")
        else:
            print(f"Directory does not exist in input directory: {input_path}")


def main():
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

    try:
    	os.mkdir('existing_directory')
    except OSEerror as e:
    	if e.errno == 17: # [Errno 17] File exists
    		print('Directory already exist.')
    	else:
    		raise # Re-raise the exception if it's not a Errno 17



if __name__ == "__main__":
    main()
