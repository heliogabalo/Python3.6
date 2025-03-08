#!/usr/bin/env python3
#
# Copyright (c) 2025 Raul Vilchez Ruiz
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import re
import sys

def rst_to_adoc(rst_content):
    """
    Convert reStructuredText content to AsciiDoc content.
    """
    # Convert headings
    rst_content = re.sub(r'^=+\n(.+)\n=+\n', r'= \1\n', rst_content, flags=re.MULTILINE) # Level 1
    rst_content = re.sub(r'^-+\n(.+)\n-+\n', r'== \1\n', rst_content, flags=re.MULTILINE) # Level 2
    rst_content = re.sub(r'^~+\n(.+)\n~+\n', r'=== \1\n', rst_content, flags=re.MULTILINE) # Level 3

    # Convert bold and italic
    rst_content = re.sub(r'\*\*(.+?)\*\*', r'*\1*', rst_content) # Bold
    rst_content = re.sub(r'\*(.+?)\*', r'_\1_', rst_content) # Italic

    # Convert bullet lists
    rst_content = re.sub(r'^\* ', r'* ', rst_content, flags=re.MULTILINE)

    # Convert numbered lists
    rst_content = re.sub(r'^#. ', r'. ', rst_content, flags=re.MULTILINE)

    # Convert literal blocks
    rst_content = re.sub(r'::\n\s+', r'[source]\n----\n', rst_content)
    rst_content = re.sub(r'^\s{4}', r'', rst_content, flags=re.MULTILINE)

    return rst_content

def convert_rst_file_to_adoc(input_file, output_file):
    """
    Convert a .rst file to an .adoc file.
    """
    try:
        # Read the .rst file
        with open(input_file, 'r', encoding='utf-8') as file:
            rst_content = file.read()

        # Convert RST to AsciiDoc
        adoc_content = rst_to_adoc(rst_content)

        # Write the AsciiDoc content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(adoc_content)

        print(f"Conversion complete! AsciiDoc saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """
    Main function to handle command-line arguments.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python rst_to_adoc.py <input_file.rst>")
        sys.exit(1)

    # Get the input file from command-line arguments
    input_rst_file = sys.argv[1]

    # Generate the output file name
    if input_rst_file.endswith('.rst'):
        output_adoc_file = input_rst_file[:-4] + '.adoc'
    else:
        output_adoc_file = input_rst_file + '.adoc'

    # Perform the conversion
    convert_rst_file_to_adoc(input_rst_file, output_adoc_file)

if __name__ == "__main__":
    main()
