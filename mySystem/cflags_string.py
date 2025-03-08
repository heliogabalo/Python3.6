#!/usr/bin/env python3


header_paths = [
	"/lib/modules/$(uname -r)/build/include/linux",
	"/lib/modules/$(uname -r)/build/arch/x86/include/asm",
	"/usr/include/linux",
	"/usr/include/asm"
]

with open("header_paths.txt", "w") as a_file:
	for path in header_paths:
		a_file.write(f"{path}\n")
		
## load the list as CFLAGS parameter
# CFLAGS=$(cat header_paths.txt |xargs -I {} echo "-I{}" |tr '\n' ' ')
