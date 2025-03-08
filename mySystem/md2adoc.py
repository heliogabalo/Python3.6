# md2adoc.py
import sys
import re

def md_to_adoc(md_text):
    # Basic conversions
    adoc_text = md_text
    adoc_text = re.sub(r'^# (.*)$', r'= \1', adoc_text, flags=re.MULTILINE) # Heading 1
    adoc_text = re.sub(r'^## (.*)$', r'== \1', adoc_text, flags=re.MULTILINE) # Heading 2
    adoc_text = re.sub(r'^### (.*)$', r'=== \1', adoc_text, flags=re.MULTILINE) # Heading 3
    adoc_text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', adoc_text) # Bold
    adoc_text = re.sub(r'_(.*?)_', r'_\1_', adoc_text) # Italics
    adoc_text = re.sub(r'`(.*?)`', r'`\1`', adoc_text) # Inline code
    adoc_text = re.sub(r'^- (.*)$', r'* \1', adoc_text, flags=re.MULTILINE) # Unordered lists
    adoc_text = re.sub(r'^(\d+)\. (.*)$', r'\1. \2', adoc_text, flags=re.MULTILINE) # Ordered lists
    return adoc_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python md2adoc.py input.md")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        md_text = f.read()

    adoc_text = md_to_adoc(md_text)
    print(adoc_text)
