step=1000
targetCount = step
entityType = None
cellsToCheck = []

clear()

while True:	
	if entityType != None:
		itemType = get_item_from_entity_type(entityType)
		if num_items(itemType) > targetCount:
			entityType = None
	
	
	while entityType == None:
		entityType = get_target_crop(entityType, targetCount)
		quick_print("New entity type", entityType)	
		cellsToCheck = get_all_cells()	
		targetCount += step
		quick_print('Target count:', targetCount)
		
	petals = []
	
	while len(cellsToCheck) > 0:
		cell = cellsToCheck.pop(0)
		move_to(cell[0], cell[1])
		if entityType == Entities.Grass:
			plant_grass()
		elif entityType == Entities.Carrots:
			plant_carrots()
		elif entityType == Entities.Bush or entityType == Entities.Tree:
			plant_tree()
		elif entityType == Entities.Pumpkin:
			isHarvestable = plant_pumpkins()
			if isHarvestable != True:
				cellsToCheck.append(cell)
			if len(cellsToCheck) == 0:
				harvest()
		elif entityType == Entities.Sunflower:
			petalCount = plant_sunflowers()
			
			if len(petals) == 0:
				petals.append([petalCount, get_pos_x(), get_pos_y()])
			else:
				for i in range(len(petals)):
					if petalCount >= petals[i][0]:
						petals.insert(i, [petalCount, get_pos_x(), get_pos_y()])
						break
					elif i == len(petals) - 1:
						petals.append([petalCount, get_pos_x(), get_pos_y()])
						
			if len(petals) == get_world_size() ** 2:
				for petal in petals:
					move_to(petal[1], petal[2])
					while can_harvest() != True:
						# Waiting because this has to be done in order
						quick_print("Waiting...")
					harvest()
				
	cellsToCheck = get_all_cells()	
	


		