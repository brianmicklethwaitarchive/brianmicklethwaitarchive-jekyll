# Fixes some problems with markdown files
# generated from LA pamphlets by
# pdf2md.morethan.io

import sys

filename = sys.argv[1]
paragraph_break = False

print('---')
print('layout: page')
print('title: insert title')
print('permalink: /' + filename)
print('---')
print()

with open(filename) as f:
    line_to_append = None
    for line in f:
        line = line.strip()
        if line == '```':
            line_to_append = None
            paragraph_break = False
            continue
        if paragraph_break:
            paragraph_break = False
            if len(line):
                print()
        if line_to_append:
            line = line_to_append + line
        if len(line) and line[-1] == '-':
            line_to_append = line[:-1]
        else:
            print(line)
            # short lines ending in a full stop are usually paragraph breaks
            if len(line) and line[-1] == '.' and len(line) < 30:
                paragraph_break = True
            line_to_append = None
