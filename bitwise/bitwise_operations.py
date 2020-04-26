def is_chosen_color(chosen_colors, color):
    # 'chosen_colors & color' is binary AND
	return color == chosen_colors & color


red = 1
blue = red << 1
yellow = blue << 1
green = yellow << 1
pink = green << 1
white = pink << 1
black = white << 1

# binary OR to include all chosen colors
chosen_colors = red | yellow | white | black
print(f"white : {is_chosen_color(chosen_colors, white)}")
print(f"yellow : {is_chosen_color(chosen_colors, yellow)}")
print(f"blue : {is_chosen_color(chosen_colors, blue)}")
