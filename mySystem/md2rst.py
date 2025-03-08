import re
import sys
from pathlib import Path

def convert_md_to_rst(md_file_path, rst_file_path):
    """
    Convert a Markdown file to reStructuredText.

    :param md_file_path: Path to the input Markdown file.
    :param rst_file_path: Path to the output reStructuredText file.
    """
    # Read the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    # Convert Markdown to reStructuredText
    rst_content = md_to_rst(md_content)

    # Write the reStructuredText content to the output file
    with open(rst_file_path, "w", encoding="utf-8") as rst_file:
        rst_file.write(rst_content)

    print(f"Converted {md_file_path} to {rst_file_path}")

def md_to_rst(md_text):
    """
    Convert Markdown text to reStructuredText.

    :param md_text: Markdown text as a string.
    :return: Converted reStructuredText as a string.
    """
    # Convert headings
    md_text = re.sub(r'^# (.+)$', r'\n\1\n=====', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)$', r'\n\1\n-----', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^### (.+)$', r'\n**\1**', md_text, flags=re.MULTILINE)

    # Convert bold and italic
    md_text = re.sub(r'\*\*(.+?)\*\*', r'**\1**', md_text)
    md_text = re.sub(r'\*(.+?)\*', r'*\1*', md_text)

    # Convert links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'`\1 <\2>`_', md_text)

    # Convert unordered lists
    md_text = re.sub(r'^- (.+)$', r'* \1', md_text, flags=re.MULTILINE)

    # Convert ordered lists
    md_text = re.sub(r'^\d+\. (.+)$', r'#. \1', md_text, flags=re.MULTILINE)

    # Convert inline code
    md_text = re.sub(r'`(.+?)`', r'``\1``', md_text)

    # Convert code blocks
    md_text = convert_code_blocks(md_text)

    return md_text

def convert_code_blocks(md_text):
    """
    Convert Markdown code blocks to reStructuredText code blocks.

    :param md_text: Markdown text as a string.
    :return: Text with code blocks converted to reStructuredText format.
    """
    # Handle multi-line code blocks with language specification
    md_text = re.sub(
        r'^```(\w*)\n(.+?)\n```',
        lambda match: f".. code-block:: {match.group(1)}\n\n " + match.group(2).replace("\n", "\n "),
        md_text,
        flags=re.DOTALL
    )

    # Handle single-line code blocks
    md_text = re.sub(
        r'^```(.+?)```',
        lambda match: f"::\n\n {match.group(1)}",
        md_text,
        flags=re.MULTILINE
    )

    return md_text

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python md_to_rst.py <input_md_file> <output_rst_file>")
        sys.exit(1)

    input_md_file = sys.argv[1]
    output_rst_file = sys.argv[2]

    # Perform the conversion
    convert_md_to_rst(input_md_file, output_rst_file)
