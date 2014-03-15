#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gordonsong <gordon0640@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import os, sys
import getopt

def usage():
	print("Usage:%s [-a|-o|-c] [--help|--output] args...." %Dsys.argv[0])

def parseargs():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ao:c", ["help", "output="])

		print("============== opts ===============")
		print(opts)

		print("============== args ===============")
		print(args)

		for opt, arg in opts:
			if opt in ("-h", "--help"):
				usage()
				sys.exit(1)
			elif opt in ("-t", "--test"):
				print("for test option")
			else:
				print("%s ==> %s" %(opt, arg))
	except getopt.GetoptError:
		print("getopt error!")
		usage()
		sys.exit(1)

if __name__ == '__main__':
	parseargs()