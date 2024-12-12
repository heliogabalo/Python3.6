#!/usr/bin/python3.6 

import os
import myLibShell as sh
import gitInit as git



source = '/usr/share/doc/check-devel-0.9.9/example'
bak = '/tmp/example'
bak_src = '/tmp/example/src'
bak_test = '/tmp/example/tests'
dest = '/tmp/myExample'
pathtests = '/tmp/myExample/tests'
pathsrc = '/tmp/myExample/src'


sh.change_to_dir(dest)
sh.remove_directory(bak)
sh.remove_directory(dest)
sh.copy_recursive(source, bak)
sh.create_directory(pathtests)
sh.create_directory(pathsrc)
sh.change_to_dir(dest)

git.initialize_git_repo('.')
file_list = ['Makefile.am', 'configure.ac']
sh.cherry_pick_files(bak, dest, file_list)

file_list = ['Makefile.am', 'main.c']
sh.cherry_pick_files(bak_src, pathsrc, file_list)
#sh.create_empty_file("money.c")
sh.cat_file("/tmp/example/src/money.1.h", "/tmp/myExample/src/money.h")
sh.cat_file("/tmp/example/tests/check_money.1.c", "/tmp/myExample/tests/check_money.c")
sh.cherry_pick_files(bak_test, pathtests, ['Makefile.am'])
sh.copy_file("/tmp/example/tests/Makefile.am", pathtests)
sh.change_to_dir(dest)

git.git_add_all(dest)
message = "Initial commit."
git.git_commit(message, dest)

text = " You shouldn't automate this script\n \
since is not possible to predict the result:\n \
#autoreconf --install 2> /tmp/error.log |tee /tmp/out.log\n \
#./conffigure\n \
#make\n \
#make distcheck\n \
#tar ztf my-example.tar.gz\n" 
print(f'{text:>}')




