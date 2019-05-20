from pysine import sine
import sys

duration = .5
frequency_offset = 400
multiplexor = 1.5

def to_utf_code(string):
	ints = []
	for char in string:
		ints.append(ord(char))
	return(ints)

def sound(string):
	ints = to_utf_code(string)
	char_duration = duration / len(ints)
	for char in ints:
		sine(frequency = (char + frequency_offset)*multiplexor, duration = char_duration)

for line in sys.stdin:
	sys.stdout.write(line)
	sound(line)

def play():
	while True:
     		sound(input())	
