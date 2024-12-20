#!/usr/bin/env python3

#/*
# * gitInit.py
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

import subprocess


def initialize_git_repo(directory):
	'''Run "git init" in the specified directory.
		 This function will initialize a git repository in the
		 current directory.
		 It also will ensures that an exception will be raised
		 if the command fails.
	'''
	try:
		subprocess.run(["git","init"], cwd=directory, check=True)
#		print(f"Initialized empty Git repository in {directory}")
	except subprocess.CalledProcessError as e:
		print(f"Error Initializing Git repository: {0}")


def git_add_all(directory):
	'''Run "git add ." in the specified directory.
		 This function will stage all files in working directory.
		 It also will ensures that an exception will be raised
		 if the command fails.
	'''
	try:
		# Run 'git init' in the specified directory
		subprocess.run(["git","add", "."], cwd=directory, check=True)
		print(f"Added all unstaged files in working directory {directory}")
	except subprocess.CalledProcessError as e:
		print(f"Error staging all files in: {e}")


def git_commit(message, directory):
	'''Automate the commit of all staged files.'''
	try:
		subprocess.run(["git","commit", "-m", message], cwd=directory, check=True)
		print(f"Commit all staged work with message: {message}")
	except subprocess.CalledProcessError as e:
		print(f"Error trying to commit: {e}")


def git_push(*repository, branch = "master"):
	'''Automated pushes of defined repositories.'''
	
	for repo in repository:
		print(f"Processing repository: {repo}")
		try:
			subprocess.run(["git", "push", "origin", branch], cwd=repo, check=True)
			print(f"Pushing to repo: {repo}")
		except subprocess.CalledProcessError as e:
			print(f"Error pushing to {repo}: {e}")









# Example usage
#initialize_git_repo("/path/to/project")



