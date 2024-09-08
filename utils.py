
def get_target_crop(current_type, targetNumber):
	if current_type != None and num_items(current_type) < targetNumber:
		return current_type
		
	if num_items(Items.Hay) < targetCount:
		return Entities.Grass
		
	if num_items(Items.Wood) < targetCount:
		return Entities.Tree
		
	if num_items(Items.Carrot) < targetCount:
		return Entities.Carrots
		
	if num_items(Items.Pumpkin) < targetCount:
		return Entities.Pumpkin
	
	# This isn't like the others...
	if num_items(Items.Power) < targetCount:
		return Entities.Sunflower
				
	return None
	
def get_item_from_entity_type(entity_type):
	if entity_type == Entities.Grass:
		return Items.Hay
		
	if entity_type == Entities.Bush:
		return Items.Wood
		
	if entity_type == Entities.Tree:
		return Items.Wood
		
	if entity_type == Entities.Carrots:
		return Items.Carrot
		
	if entity_type == Entities.Pumpkin:
		return Items.Pumpkin
		
	if entity_type == Entities.Sunflower:
		return Items.Power
		
	return None	
	
	
def get_entity_from_item_type(item_type):
	if item_type == Items.Hay:
		return Entities.Grass
		
	if item_type == Items.Wood:
		return Entities.Tree
		
	if item_type == Items.Bush:
		return Entities.Tree
		
	if item_type == Items.Carrot:
		return Entities.Carrots
		
	if item_type == Items.Pumpkin:
		return Entities.Pumpkin
		
	if entity_type == Items.Power:
		return Entities.Sunflower
		
	return None
		
def is_even(num):
	if num % 2 == 0:
		return True
	return False
	
def get_all_cells():
	cells = []
	for x in range(get_world_size()):
		
		if is_even(x):
			for y in range(get_world_size()):
				cells.append([x,y])
		else:
			for y in range(get_world_size()):
				cells.append([x,(get_world_size() - 1) - y])
			
	return cells