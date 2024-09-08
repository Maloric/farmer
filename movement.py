def move_to(x, y):
	# quick_print('Moving to', x, y)
	while get_pos_x() != x or get_pos_y() != y:
		move_towards(x, y)
	
def get_move_dir_x(x):
	diff = x - get_pos_x() # -6
	alt = get_pos_x() - x - get_world_size() # 6
	if (diff < 0):
		if abs(alt) < abs(diff):
			return East
		else:
			return West
	if (diff > 0):
		if abs(alt) < abs(diff):
			return West
		else:
			return East
	return None

	
def get_move_dir_y(y):
	diff = y - get_pos_y() # -6
	alt = get_pos_y() - y - get_world_size() # 6
	if (diff < 0):
		if abs(alt) < abs(diff):
			return North
		else:
			return South
	if (diff > 0):
		if abs(alt) < abs(diff):
			return South
		else:
			return North
	return None
	

def distance_to_y(y):
	return abs(get_pos_y() - y)
	
def move_towards(x, y):
	h = get_move_dir_x(x)
	v = get_move_dir_y(y)
	if h != None:
		move(h)
	
	if v != None:
		move(v)