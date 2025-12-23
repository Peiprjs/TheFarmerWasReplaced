def goToBeginning():
    for i in range(get_pos_x()):
	    move(West)
         
    for i in range(get_pos_y()):
        move(South)

def plantGrassland(entity):
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(entity)