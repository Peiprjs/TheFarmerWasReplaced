from functions import *

change_hat(Hats.Wizard_Hat)
goToBeginning()
	
while True:
	get_pumpkin_requirements(1000000)
	
	if get_entity_type() != Entities.Pumpkin:
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				plantGrassland(Entities.Pumpkin)
				move(North)
			move(East)
	for i in range(get_world_size()):
		for e in range(get_world_size()):
			harvest()
			plantGrassland(Entities.Pumpkin)
			move(North)
		move(East)