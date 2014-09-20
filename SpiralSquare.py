'''
Created on Sep 16, 2014

@author: hoangnm
'''

__author__  = "Minh-Hoang, Nguyen <hoangnm.53@gmail.com>"
__date__    = "$September 16, 2014$"
__version__ = "1.0"

import argparse

def generateSpiralSquare(size):
	spiralMatrix = [[0 for i in xrange(size)] for i in xrange(size)]

	x = y = 0
	dx = 0; dy = -1

	for i in range(size**2):
		# Use center point as origin of new coordinate to make spiral square
		if (-size/2 <= x <= size/2) and (-size/2 <= y <= size/2):
			spiralMatrix[x+size/2][-(y-size/2)] = i+1

		# Change direction
		if x == y or (x > 0 and x == 1-y) or (x < 0 and x == -y):
			tmp = dx
			dx = -dy
			dy = tmp

		x = x + dx
		y = y + dy

	return spiralMatrix
	
def writeMatrix(outfile, matrix):
	try:
		outfile = open(args.outfile, 'w')
		for j in range(0, len(matrix[0])):
			for i in range(0, len(matrix[0])):
				outfile.write(str(matrix[i][j]).rjust(3))
				outfile.write(" ")
			outfile.write("\n\n")
		outfile.close()
	except IOError:
		print "Error when write down out file"
	
if __name__ == '__main__':
	usage = "usage: %(prog)s [options] \npython SpiralSquare -h for help"

	parser = argparse.ArgumentParser(prog="SpiralSquare", usage=usage, 
    	version="SpiralSquare "+__version__,
    	description='Generate Spiral Square',
    	epilog="(C) 2014 by Minh-Hoang, Nguyen")

	parser.add_argument("-s", "--size", dest="size",required=True,
                        help="Size of spiral square")
	parser.add_argument("-o","--outfile", dest="outfile", required=True, 
                        help="Outfile path")
	args = parser.parse_args()

	if args:
		size = int(args.size)
		if(size % 2 == 1):
			writeMatrix(args.outfile, generateSpiralSquare(size))
		else:
			print "Warning:\nThe size is not an odd number, then I cannot generate spiral square!"\
				  "\nPlease try again with an odd number!"

