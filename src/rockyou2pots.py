#!/usr/bin/env python3

import lzma

original_lines = []
with lzma.open('rockyou.txt.xz', 'rb') as f:
    original_lines = f.readlines()

def decode_lines(lines, encoding):
    output_lines = []
    for line in lines:
        try:
            tempstring = str(line, encoding=encoding, errors='strict').rstrip('\n')
            if str.isprintable(tempstring):
                output_lines.append(tempstring)
        except UnicodeDecodeError:
            pass
    return output_lines

def output_pot(lines, file):
    with open(file, 'w') as f:
        for line in lines:
            f.write(':' + line + '\n')

utf8_lines = decode_lines(original_lines, 'utf8')

latin1_lines = decode_lines(original_lines, 'latin1')

# ansi == cp1252; http://www.alanwood.net/demos/ansi.html
ansi_lines = decode_lines(original_lines, 'cp1252')

lanman_lines = []
for line in ansi_lines:
    if len(line) <= 14:
        lanman_lines.append(line)


output_pot(utf8_lines, "rockyou.utf8.24.pot")
output_pot(latin1_lines, "rockyou.ansi.16.pot")
output_pot(ansi_lines, "rockyou.ansi.pot")
output_pot(lanman_lines, "rockyou.lm850.pot")

