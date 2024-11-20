## FILE HANDLING ##
- Handling a file.
- Phenomenon of reading the data from the file or writing the data into the file.
- 4 modes to read:-
    1.r (read)- used to take the content from file.
    2.w (write)- used to write in a file.
    3.x (xmode)- used to write in a file but wont overwrite over another file.Exclusive Creation Mode 'x': This mode is used to create a new file, but it raises a FileExistsError if the file already exists
    4.a (append)-used to write in the same file itself rather than overwriting.
- open(file,mode) :-
    -inbuilt or generic fucntion.
    -it takes 2 arguments:-
        *file -path of file
        *mode-not manadatory.here we write the mode to be performed in " ".
- read(), readline(), readlines() to get content from the file.
## standard way   
- context manager is used to open the file in a standard way.
- 'with' keyword is used.
\\\\\\\\syntax\\\\\\\\
-with open(file,mode) as f:
-it gets automatically closed.
##

## NOTE
- r" "
- wherever you have '\' instead give '/' or '\\'
- .close() to close
- .closed() to check if its closed
- os.remove() and os.unlink() to remove a file
