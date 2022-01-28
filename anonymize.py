import sys
import re

def replace(pattern, repl, string):
	r_str = string
	for match in re.findall(pattern, r_str):
		r_str = re.sub(pattern, repl, string)
	return r_str

def readPGN(file_name):
	with open(file_name, "r") as file:
		return file.read()

def writePGN(file_name, output_name):
	with open(output_name, "w") as file:
		pgn = readPGN(file_name)

		newPGN = ''
		for i in pgn.split("\n\n\n"):
			newPGN += (editPGN(i) + '\n\n')

		file.write(newPGN)

def removeComments(pgn):
	pattern = r'({[^}]*})+'
	return replace(pattern, "", pgn)

def removeResult(pgn):
	pattern = r'(1-0|1\/2-1\/2|0-1)'
	return replace(pattern, "", pgn)

def removeTags(pgn):
	pattern = r'(\[[^\]]*])'
	return replace(pattern, "", pgn)

def removeNewLines(pgn):
	pattern = r'(\n)'
	return replace(pattern, "", pgn)

def trimSpaces(pgn):
	pattern = r'( +)+'
	return replace(pattern, " ", pgn)

def editPGN(pgn):
	return trimSpaces(removeNewLines(removeTags(removeResult(removeComments(pgn))))) + "*"

def manglePGN(pgn):
	return replace(r'( +)+', " ", replace(r'\n', "", replace(r'(\[[^\]]*])|({[^}]*})|(1-0|1\/2-1\/2|0-1)', "", pgn)))

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	pgn_file_pattern = r'(.+\.pgn)'
	assert(re.match(pgn_file_pattern, input_file) and re.match(pgn_file_pattern, output_file))
	writePGN(input_file, output_file)

if __name__ == "__main__":
	main()