import argparse
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument('filename') # Positional 
parser.add_argument('-t', '--title') 

args = parser.parse_args()

print(f'{args.filename=}')
print(f'{args.title=}')

if input('proceed? y/n\n') != 'y':
 exit()

lines = list(open(args.filename, 'r'))

lines = [
'---\n',
'layout: post\n',
f'title: {args.title}\n',
'---\n'
] + lines

with open(args.filename, 'w') as f:
 f.writelines(lines)
