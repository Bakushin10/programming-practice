def is_chosen_color(chosen_colors, color):
	return color == chosen_colors & color


red = 1
blue = red << 1
yellow = blue << 1
green = yellow << 1
pink = green << 1
white = pink << 1
black = white << 1


chosen_colors = red | yellow | white | black
print(f"white : {is_chosen_color(chosen_colors, white)}")
print(f"yellow : {is_chosen_color(chosen_colors, yellow)}")
print(f"blue : {is_chosen_color(chosen_colors, blue)}")
