#!/bin/python3
filenames = ['create.md', 'retrieve.md', 'update.md', 'delete.md']
with open('CRUD_operations.md', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
            outfile.write("\n\n")
