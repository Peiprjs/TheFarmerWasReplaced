from functions import *

desiredWaterLevel = 0.4
goToBeginning()

while get_pos_x() <= 4:
    while get_pos_y() <= 4:
        if get_entity_type() == Entities.Dead_Pumpkin:
            plantGrassland(Entities.Pumpkin)
        elif can_harvest():
            harvest()
            plantGrassland(Entities.Pumpkin)
        else:
            plantGrassland(Entities.Pumpkin)
        
        if get_water() < desiredWaterLevel:
            use_item(Items.Water)
            
        move(North)
        
    move(East)
	