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

import sys
import re

def md_to_adoc(md_text):
    # Convert headings
    md_text = re.sub(r'^# (.*)$', r'= \1', md_text, flags=re.MULTILINE) # Heading 1
    md_text = re.sub(r'^## (.*)$', r'== \1', md_text, flags=re.MULTILINE) # Heading 2
    md_text = re.sub(r'^### (.*)$', r'=== \1', md_text, flags=re.MULTILINE) # Heading 3
    md_text = re.sub(r'^#### (.*)$', r'==== \1', md_text, flags=re.MULTILINE) # Heading 4
    md_text = re.sub(r'^##### (.*)$', r'===== \1', md_text, flags=re.MULTILINE) # Heading 5
    md_text = re.sub(r'^###### (.*)$', r'====== \1', md_text, flags=re.MULTILINE) # Heading 6

    # Convert bold and italic
    md_text = re.sub(r'\*\*(.*?)\*\*', r'*\1*', md_text) # Bold
    md_text = re.sub(r'__(.*?)__', r'*\1*', md_text) # Bold (alternative syntax)
    md_text = re.sub(r'\*(.*?)\*', r'_\1_', md_text) # Italic
    md_text = re.sub(r'_(.*?)_', r'_\1_', md_text) # Italic (alternative syntax)

    # Convert inline code
    md_text = re.sub(r'`(.*?)`', r'`\1`', md_text)

    # Convert block code
    md_text = re.sub(r'^```(.*?)\n(.*?)\n```', r'[source,\1]\n----\n\2\n----', md_text, flags=re.DOTALL)

    # Convert unordered lists
    md_text = re.sub(r'^[-*+] (.*)$', r'* \1', md_text, flags=re.MULTILINE)

    # Convert ordered lists
    md_text = re.sub(r'^(\d+)\. (.*)$', r'\1. \2', md_text, flags=re.MULTILINE)

    # Convert links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'link:\2[\1]', md_text)

    # Convert images
    md_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'image::\2[\1]', md_text)

    # Convert blockquotes
    md_text = re.sub(r'^> (.*)$', r'____\n\1\n____', md_text, flags=re.MULTILINE)

    # Convert horizontal rules
    md_text = re.sub(r'^---$', r'''\n''' + '=' * 80 + r'''\n''', md_text, flags=re.MULTILINE)

    # Convert tables (basic support)
    def replace_table(match):
        rows = match.group(1).strip().split('\n')
        table = '[cols="1,1,1", options="header"]\n|===\n' # Adjust cols as needed
        for row in rows:
            table += '| ' + ' | '.join(row.strip().split('|')[1:-1]) + '\n'
        table += '|===\n'
        return table

    md_text = re.sub(r'^\|(.+)\|\n\|[-:|]+\|\n((?:\|.*\|\n)+)', replace_table, md_text, flags=re.MULTILINE)

    return md_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python md2adoc.py input.md")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        md_text = f.read()

    adoc_text = md_to_adoc(md_text)
    print(adoc_text)
