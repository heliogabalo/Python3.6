#!/usr/bin/env python3

#/*
# * myLibShell.py
# * This file is part of libtool-izator-starter?
# *
# * Copyright (C) 2024 - Raul Vilchez Ruiz
# *
# * libtool-izator-starter is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * libtool-izator-starter is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with <program name>. If not, see <http://www.gnu.org/licenses/>.
# */


import os
import glob
import pydoc
import shutil
import subprocess



#####################################
#							INFO									#
#####################################
def list_files():
	'''List all files on current working directory.'''
	try:
		ls = glob.glob('*')	

		for a_file in ls:
			#print(a_file)
			print(" {0:>2} ".format(a_file))		
	except OSError as e:
		print(f"Error listing directory: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")


def print_pwd():
	try:
		current = os.getcwd()
		print(current)
	except OSError as e:
		print(f"Error printing directory: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")


def my_pydoc_pager(text):
	pydoc.pager(text)
	

def change_to_dir(directory):
	'''Change directory to /tmp'''
	try:
		os.chdir(directory)
		print(f"Working directory: {directory}")
	except OSError as e:
		print(f"Error changing directory: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")


#####################################
#							COPY									#
#####################################
def create_empty_file(fileName):
	'''Create a file only if it does not exist.'''
	try:
		with open(fileName, 'x') as f:
			pass
	except FileExistsError:
		print("File already exist.")


def cat_file(source, destination):
	'''Copy the contents of a source file to a 
		 destination file. 
	'''
	try:
		with open(source, 'r') as src, open(destination, 'w') as dest:
			dest.write(src.read())
	except OSError as e:
		print(f"Error copying file contents: {e}")


def copy_recursive(source, dest):
	'''Copy a directory recursively.'''
	try:
		shutil.copytree(source, dest)
		print(f"Directory: {source} had been copied.")
	except FileExistsError:
		print(f"Destination directory: {dest} already exist.")
	except IsADirectoryError:
		print(f"Destination directory: {dest} should be copied with 'shutil.copytree'.")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}.")

		
def copy_file(source, dest):
	'''Copy /tmp/exampleA to /tmp/exampleB'''
	try:
		shutil.copy(source, dest)
		print(f"File: {source} had been copied.")
	except subprocess.CalledProcessError as e:
		print(f"Error copying directory: {e}")


def create_directory(directory):
	'''Create directories.
		 TODO:
		 	implement a extended prototype(sobrecarga)
		 	with 2, 3 or more args.
	'''
	try:
		os.makedirs(directory, exist_ok=True)
		print(f"Directory: {directory} had been created.")
	except OSError as e:
		print(f"Error creating directory: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")


def cherry_pick_files(source, destination, fileList):
	'''@source; source path.
		 @destination; destination path.
		 @fileList; it expects an array of files, single files
		 					  should be declared as a single file list.
		 					  i.e: ['myFile'].
	'''
	try:
		os.makedirs(destination, exist_ok=True)
		
		for fileName in fileList:
			source_path = os.path.join(source, fileName)
			destination_path = os.path.join(destination, fileName)
			copy_file(source_path, destination_path)
			
	except OSError as e:
		print(f"Error directory {source} doesn't exist. Error: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")	


#####################################
#							DELETE								#
#####################################
def remove_directory(directory):
	'''Remove /tmp/example if it exist'''
	try:
		shutil.rmtree(directory)
		print(f"Directory: {directory} had been removed.")
	except OSError as e:
		print(f"Error removing directory: {e}")
	except Exception as e:
		print(f"An unexpected Error occurred: {e}")

#####################################
#							MISCELANEA						#
#####################################
def colored_output():
	## TODO:
	## Place this lines where you want
	## to call for colored output.
	my_colors = myLibShell.Bcolors
	print(my_colors.FAIL + "Peligro: 3m..2m.1m:" + my_colors.ENDC)





#####################################
#						EXAMPLE CALL						#
#####################################
#os.system(cmd)
#list_files()
#print_pwd()
#change_dir('linux/')
#my_pydoc_pager('text texttexttext texttext\ntext texttexttext texttext ')
