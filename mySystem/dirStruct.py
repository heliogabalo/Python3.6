import os
import sys

def print_tree(directory, prefix=""):
    """Recursively print the directory structure in a tree-like format."""
    try:
        # Check if the directory is accessible
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            return

        # Get the list of items in the directory
        items = os.listdir(directory)
        items.sort() # Sort alphabetically

        for i, item in enumerate(items):
            path = os.path.join(directory, item)
            is_last = (i == len(items) - 1)

            # Print the current item
            print(prefix + ("└── " if is_last else "├── ") + item)

            # If the item is a directory, recurse
            if os.path.isdir(path):
                print_tree(path, prefix + (" " if is_last else "│ "))
    except PermissionError:
        print(f"{prefix}└── [Permission Denied: Cannot access '{os.path.basename(directory)}']")

def main():
    # Check if a target path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <target_path>")
        sys.exit(1)

    target_path = sys.argv[1]
    print(f"Directory structure of: {target_path}")
    print_tree(target_path)

if __name__ == "__main__":
    main()
