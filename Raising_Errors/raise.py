def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if type(color) is not str:
		raise TypeError("color must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

# colorize([], 'cyan')
# colorize(34, "red")
colorize('hello', 10)