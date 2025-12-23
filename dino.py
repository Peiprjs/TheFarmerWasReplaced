from functions import *

change_hat(Hats.Dinosaur_Hat)
next_apple = measure()
current_position = [get_pos_x(), get_pos_y()]

while True:
	if next_apple is None:
		print("HELP")
	while get_pos_x() <  next_apple[0]:
		previous_position = current_position
		if not move(East):
			break
		current_position = [get_pos_x(), get_pos_y()]

	while get_pos_x() > next_apple[0]:
		previous_position = current_position
		if not move(West):
			break
		current_position = [get_pos_x(), get_pos_y()]
		
	while get_pos_y() < next_apple[1]:
		previous_position = current_position
		if not move(North):
			break
		current_position = [get_pos_x(), get_pos_y()]

	while get_pos_y() > next_apple[1]:
		previous_position = current_position
		if not move(South):
			break
		current_position = [get_pos_x(), get_pos_y()]

	if get_pos_x() == next_apple[0] and get_pos_y() == next_apple[1]:
		next_apple = measure()
	
	if current_position == previous_position:
		goToBeginning()
		if current_position == [get_pos_x(), get_pos_y()]:
			change_hat(Hats.Dinosaur_Hat)