#!/bin/python
import sys
from koans_suite.mountain import Mountain 

def main(args=None):
	if len(args) > 1:
		path = args[1]
	else:
		path = "koans"
	Mountain().walk_the_path(path)

if __name__ == '__main__':
	main(sys.argv)

