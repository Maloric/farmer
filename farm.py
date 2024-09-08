def plant_grass():
	if can_harvest():
		harvest()
	if get_ground_type() == Grounds.Soil:
		till()
		
def plant_bush():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
		
def plant_tree():
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Tree:
		if is_even(get_pos_x()) != is_even(get_pos_y()):
			plant(Entities.Tree)
		else:
			plant_bush()
		
def plant_carrots():
	if can_harvest():
		harvest()
		
	if get_entity_type() != Entities.Carrots:
		if (num_items(Items.Carrot_Seed) == 0):
			trade(Items.Carrot_Seed, 100)
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Carrots)
		
def plant_pumpkins():
	if get_entity_type() == Entities.Pumpkin and can_harvest():
		return True
		
	if get_entity_type() != Entities.Pumpkin:
		if can_harvest():
			harvest()
		if (num_items(Items.Pumpkin_Seed) == 0):
			trade(Items.Pumpkin_Seed, 100)
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Pumpkin)
		
def plant_sunflowers():

	if get_entity_type() != Entities.Sunflower:
		if can_harvest():
			harvest()
		if (num_items(Items.Sunflower_Seed) == 0):
			trade(Items.Sunflower_Seed, 100)
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Sunflower)
		return measure()