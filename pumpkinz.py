from functions import *

desiredWaterLevel = 0.4
goToBeginning()

while True:
    for i in range(get_world_size()):
        if not can_harvest():
            plantGrassland(Entities.Pumpkin)
        
        if get_water() < desiredWaterLevel:
            use_item(Items.Water)
        move(North)
    move(East)
