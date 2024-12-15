#!/usr/bin/python3.6

import os
import myLibShell as sh
import gitInit as git


def setup_directories(source, bak, dest, bak_src, bak_test, pathtests, pathsrc):
	'''Sets up the necessary directories and copies initial files.'''
	# Ensures destination and backup directories are prepared
	sh.change_to_dir(dest)
	sh.remove_directory(bak)
	sh.remove_directory(dest)
	sh.copy_recursive(source, bak)
	
	# Create required directories
	sh.create_directory(pathtests)
	sh.create_directory(pathsrc)
	
def copy_and_prepare_files(bak, dest, bak_src, pathsrc, bak_test, pathtests):
	'''Copies and prepares files for the project structure.'''
	# Copy main configuration files
	config_files = ['Makefile.am', 'configure.ac']
	sh.cherry_pick_files(bak, dest, config_files)
	
	# Copy source files
	source_files = ['Makefile.am', 'main.c']
	sh.cherry_pick_files(bak_src, pathsrc, source_files)
	
	# Create empty and combined source files
	sh.create_empty_file(f"{pathsrc}/money.c")
	sh.cat_file(f"{bak_src}/money.1.h", f"{pathsrc}/money.h")
	
	# Prepare test files
	sh.cat_file(f"{bak_test}/check_money.1.c", f"{pathtests}/check_money.c")
	sh.cherry_pick_files(bak_test, pathtests, ['Makefile.am'])
	sh.copy_file(f"{bak_test}/Makefile.am", pathtests)
	
	
def initialize_git_repo(dest):
	'''Initializes a Git repository and makes the first commit.'''
	git.initialize_git_repo(dest)
	git.git_add_all(dest)
	commit_message = "Initial commit."
	git.git_commit(commit_message, dest)
	
	
def displays_final_message():
	'''Prints a warning about no automating the final steps.'''
	text = (
        "You shouldn't automate this script\n"
        "since it is not possible to predict the result:\n"
        "#autoreconf --install 2> /tmp/error.log | tee /tmp/out.log\n"
        "#./configure\n"
        "#make\n"
        "#make distcheck\n"
        "#tar ztf my-example.tar.gz\n"
	)
	print(f"{text:>}")
	
	
def main():
	# Define paths
	source = '/usr/share/doc/check-devel-0.9.9/example'
	bak = '/tmp/example'
	bak_src = '/tmp/example/src'
	bak_test = '/tmp/example/tests'
	dest = '/tmp/myExample'
	pathtests = '/tmp/myExample/tests'
	pathsrc = '/tmp/myExample/src'
	
	# Setup directories and prepare files
	setup_directories(source, bak, dest, bak_src, bak_test, pathtests, pathsrc)
	copy_and_prepare_files(bak, dest, bak_src, pathsrc, bak_test, pathtests)
	
	# Initialize Git and commit
	initialize_git_repo(dest)
	
	# Display final message
	displays_final_message()
	
	
if __name__ == "__main__":
		main()
	
	