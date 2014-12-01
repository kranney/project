inventory = []

def open_field():
	" The user will enter an open field and meet the end of the map."

	move = input('You are in an open field.\n')
	move.lower()
	if move == 'north':
		print('You do not want to go north!')
		open_field()
	elif move == 'west':
		day_forest_03()
	elif move == 'south':
		print('You cannot go there yet!')
		open_field()
	elif move == 'east':
		print('You are at the end of the open_field')
		open_field()
	else:
		print('Try using a cardinal direction!')
		open_field()

def day_forest_03():
	""" The user will wake up and see the village. They must head south or enter
	the village."""

	move = input('It is now morning. You exit the tent and can see your village'
		' south from where you are standing!\n')
	move.lower()
	if move == 'look':
		day_forest_03()
	elif move == 'north':
		print('You do not want to go backwards!')
		day_forest_03()
	elif move == 'east':
		open_field()
	elif move == 'south' or 'village':
		village_01()
	elif move == 'west':
		print('You do not want to go backwards!')
		day_forest_03()
	elif move == 'inventory':
		print(inventory)
		day_forest_03()
	else:
		print('Try using a cardinal direction!')
		day_forest_03()

def forest_02_03():
	""" The user will enter the north west side of the forest. Will be forced into 
	going south to face the wolf."""

	move = input('You are in the forest. You see a cave in the distance. \n')
	move.lower()
	if move == 'cave':
		print('The cave has collapsed! You may no longer enter!')
		forest_02_03()
	elif move == 'east':
		forest_01_03()
	elif move == 'west':
		print('You are at the end of the forest')
		# run this program again
		forest_02_02()
	elif move == 'north':
		battlefield()
	elif move == 'south':
		forest_04()
	elif move == 'inventory':
		print(inventory)
		forest_02_02()
	elif move == 'look':
		# start from top of program. it will give the same description as move will
		forest_02_02()
	else:
		print('You must choose from a cardinal direction, look, or inventory.')
		forest_02_02()

def village_01_01():
	""" The user now has the flowers and needs to go home to his/her family."""

	# i want to keep track of the number of moves. once the user goes over a specific
	# number of moves they lose the game.

	move = input('You now have the flowers and are excited to go home to your '
		'family\n')
	move.lower
	if move == 'east':
		village_02()
	elif move == 'inventory':
		print(inventory)
		village_01_01()
	else:
		print('Hint: Try using a cardinal direction!')
		village_01_01()

def salesman():
	""" The user will have a conversation with the salesman."""

	move = input('You have striked a conversation with the salesman. You now'
		' need to convince the salesman to help you out and get some flowers.'
		' You have two options: steal or ask\n')
	move.lower()
	if move == 'steal':
		print('You steal the flowers and get caught by the clerk. He throws'
			' a knife at you. You lose!!!')
		play()
	elif move == 'ask':
		print('You ask the salesman if he could give you some flowers. He then '
			"(noticing your clothes) says 'Anything for our military!'"
			'You then leave the store to go home.')
			# prompt the user to exit
		inventory.append('flowers')
		store_exit()
	elif move == 'inventory':
		print(inventory)
		salesman()
	else:
		salesman()

def store_exit():
	""" Allows the user to exit the store."""
	
	village_01_01()

def forest_01_03():
	""" The user enters the forest after taking items from the cave."""
	print('You are in the forest and you see a lighted cabin.')
	move = input('\n')
	move.lower()
	max_moves()
	if move == 'north':
		battlefield()
	elif move == 'east':
		print('You are at the end of the forest.')
		# start forest_01 over again
		forest_01_03()
	elif move == 'south':
		# forest_03()
		print('You can not go there yet!')
		forest_01_03()
	elif move == 'west':
		forest_02_02()
	elif move == 'look':
		print('You are in the forest. You see a cabin.')
		# need to run forest_01 all over again
		forest_01_03()
	elif move == 'cabin':
		itemless_cabin()
	elif move == 'exit':
		forest_01_03()
	elif move == 'inventory':
		print(inventory)
		forest_01_03()
	else:
		print('Choose from north, east, south, west, look, and cabin.')
		# run forest_01 again.
		forest_01_03()

def axe():
	""" The user will have to use the axe on the trees."""
	move = input('Use axe on what?\n')
	move.lower()
	if move == 'tree' or 'trees':
		print('You now have fire wood!!!')
		fire()
		inventory = inventory.append('wood')
	else:
		print('Hint: The forest is full of these!!!')
		axe()

def forest_02_02():
	""" The user will enter the north west side of the forest. Will be forced into 
	going south to face the wolf."""

	move = input('You are in the forest. You see a cave in the distance. \n')
	move.lower()
	if move == 'cave':
		cave()
	elif move == 'east':
		forest_01_03()
	elif move == 'west':
		print('You are at the end of the forest')
		# run this program again
		forest_02_02()
	elif move == 'north':
		battlefield()
	elif move == 'south':
		forest_04()
	elif move == 'inventory':
		print(inventory)
		forest_02_02()
	elif move == 'look':
		# start from top of program. it will give the same description as move will
		forest_02_02()
	else:
		print('You must choose from a cardinal direction, look, or inventory.')
		forest_02_02()

def itemless_cabin():
	"""Puts the user in the cabin with no items. Will force the user back into
	the forest."""

	move = input('You now have all the items. You are in the cabin.\n')
	move.lower()
	if move == 'exit':
		# go back into the forest
		forest_01_03()
	elif move == 'inventory':
		print(inventory)
		itemless_cabin()
	else:
		# give a hint
		print("You might want to 'exit' the cabin.")
		itemless_cabin()

def cabin_take():
	""" Forces the user to take all of the items at once."""

	move = input('What would you like to take?\n')
	move.lower()
	if move == 'all':
		inventory.append('bow', 'axe', 'matches')
		itemless_cabin()
	elif move == 'inventory':
		print(inventory)
		cabin_take()
	else:
		print("You need more than just the bow. Hint: Try 'all'")
		cabin_take()

def forest_02():
	""" Will give a brief description of the second forest. This function will
	include the cave. This is function after the user has the sword from the cave.
	The user will then need to enter the cabin in forest_01"""

	move = input('You are in the forest. You see a cave in the distance. \n')
	move.lower()
	if move == 'cave':
		swordless_cave()
	elif move == 'east':
		forest_01()
	elif move == 'west':
		print('You are at the end of the forest')
		# run this program again
		forest_02()
	elif move == 'north':
		battlefield()
	elif move == 'south':
		print("You can't go that far yet!!!")
		# forest_04()
		forest_02()
	elif move == 'inventory':
		print(inventory)
		forest_02()
	elif move == 'look':
		# start from top of program. it will give the same description as move will
		forest_02()
	else:
		print('You must choose from a cardinal direction, look, or inventory.')
		forest_02()

def civilian():
	""" This function will give the user interaction with the civilian."""

	move = input('You start a conversation with the civilian. He asks you '
		'what you think of the flowers.\n Do you like them?\n')
	move.lower()
	if move == 'yes':
		print('The civilian gives you the flowers.')
		inventory = inventory.append('flowers')
		store_exit()
	elif move == 'no':
		print('The civilian tells you to get your own flowers!')
		salesman()
	else:
		print("Try entering 'yes' or 'no'.")
		civilian()

def cabin_01():
	""" If the user enters the cabin before they get they sword the stranger
	will attack them unless they exit first."""

	move = input('You enter the cabin and find a stranger. You startle the stranger.'
		'The stranger quickly pick up his bow with a loaded arrow and points'
		'it at you. You then...\n')
	move.lower()
	if move == 'exit':
		forest_01_01()
	elif move == 'inventory':
		inventory = inventory.append()
	else:
		print('The stranger realized you are from the army and shoots you'
			' with his bow! You lose!!!')
		play()

def forest_01_01():
	""" The user will be forced to go to forest or into the cabin. If user
	goes into the cabin they will die."""

	# if the user reaches so many steps in the function they loose.
	# if they have less than 'x' many of steps they can continue
	# to go through the function

	# start off with 0 steps
	# add a step each time the user makes a move

	
	# steps = 0
	# while steps != 3:
	# 	# run the function and add 1 to steps
	# 	if steps != 3:
	# 		continue
	# 	else:
	# 		print('You loose!')
	# 		return play()
	
		# but when steps is greater than 3
			# have the user lose.
		

	print('You are in the forest and you see a cabin.')
	move = input('\n')
	move.lower()
	# max_moves()
	if move == 'north':
		battlefield()
	elif move == 'east':
		print('You are at the end of the forest.')
		# start forest_01 over again
		forest_01_01()
	elif move == 'south':
		print('You cannot go further yet!')
		forest_01_01()
	elif move == 'west':
		forest_02_01()
	elif move == 'look':
		print('You are in the forest. You see a cabin.')
		# need to run forest_01 all over again
		forest_01_01()
	elif move == 'cabin':
		cabin_01()
	elif move == 'inventory':
		steps = steps + 1
		print(inventory)
		forest_01_01()
	else:
		# steps = steps + 1
		print('Choose from north, east, south, west, look, and cabin.')
		# run forest_01 again.
		forest_01_01()

def village_01():
	""" The user will enter the village where a store is located. The user will
	have to get flowers from the store that is in this section of the village."""

	move = input('You are now in the village. You see a store and have an idea.\n')
	move.lower()
	if move == 'store' or 'enter':
		store()
	elif move == 'inventory':
		print(inventory)
		village_01()
	else:
		print("The 'store' is very appealing.")
		village_01()

def speak():
	""" The user will speak to a civilian and or a clerk."""

	move = input('Speak to whom?\n')
	move.lower()
	if move == 'salesman':
		salesman()
	elif move == 'civilian':
		civilian()
	elif move == 'inventory':
		print(inventory)
		speak()
	else:
		print("The 'civilian' or the 'salesman'?")
		speak()

def store():
	""" The user will enter the store and have to get flowers."""

	move = input('You have entered the stores and see flowers that are for sale .'
		' along with a civilian looking at them. You decide that you would '
		' like to get them and take them home to your family.'
		' You need to speak to someone.\n')
	move.lower()
	if move == 'speak':
		speak()
	elif move == 'inventory':
		print(inventory)
		store()
	else:
		store()

def village_02():
	""" The user enters the part of the village where the home is at."""

	move = input('You are in the part of the village where your home is at.\n')
	move.lower()
	if move == 'home':
		home()
	elif move == 'inventory':
		print(inventory)
		village_02()
	else:
		print("You need to go 'home'.")
		village_02()

def home():
	""" The user enters the home."""
	move = input('You have entered the home with flowers in your hand.\n')
	move.lower()
	if move == 'flowers' or 'give':
		flowers()
	elif move == 'inventory':
		print(inventory)
		home()
	else:
		print("You need to 'give' the 'flowers' to your family.")
		home()

def flowers():
	""" The user gives the flowers to his/her family and wins."""

	print('You give the flowers to your family. You won the game!!!')
	# start the game over again
	play()


def battlefield():
	"""Will tell the user that they have died and will prompt the user to start
	the game over again"""
	print('You have just ran back into battle with no armor.'
			'You have just been killed brutely.')
	# starts the game over again
	play()

def cabin():
	""" Gives a user a brief description of the cabin. The user will find
	someone in the cabin and have to kill them using weapons previously found."""

	move = input('You enter the lighted cabin and find a stranger. You startle the stranger.'
		'The stranger quickly pick up his bow with a loaded arrow and points '
		'it at you. You then...\n')
	move.lower()
	if move == 'exit':
		forest_01()
	elif move == 'inventory':
		print(inventory)
		cabin()
	elif move == 'sword':
		print('You have killed the stranger')
		killed_stranger()
	else:
		print('The stranger is waiting for your next move. Try using exit or sword.')
		cabin()

def killed_stranger():
	""" Explains what happens after you kill the stranger."""

	move = input('The stranger is dead and has the bow laying on ground.'
		'You see an axe and matches laying on the table.\n')
	move.lower()
	if move == 'take':
		cabin_take()
	elif move == 'inventory':
		print(inventory)
		killed_stranger()
	elif move == 'look':
		killed_stranger()
	else:
		print("You need to collect things from here. Hint: Use 'look'.")
		killed_stranger()
			
def sleep():
	""" The user will need to sleep to continue on."""

	move = input('It is getting very late. You are very tired. \n')
	move.lower()
	if move == 'sleep':
	    print('You go to sleep.')
	    day_forest_03()
	elif move == 'inventory':
		print(inventory)
		sleep()
	else:
		print('Hint: What do most people do at night?')
		sleep()
		
def enter_tent():
	""" The user will need to enter the tent and stay the night."""

	move = input('It is getting darker. Your tent is built next to the fire. \n')
	move.lower()
	if move == 'enter' or 'tent':
		print('You have entered the tent.')
		sleep()
	elif move == 'inventory':
		print(inventory)
		enter_tent()
	else:
		print("Hint: The 'tent' looks really nice.")
		enter_tent()

def tent():
	""" The user will build a tent. They will have to build a tent to surivive."""

	move = input('Build a shelter.\n')
	move.lower()
	if move == 'tent':
		print('You have built the tent!!!')
		enter_tent()
		inventory.remove('tent')
	elif move == 'inventory':
		print(inventory)
		tent()
	else:
		print("Hint: You have a '____' in your inventory!")
		tent()

def fire():
	""" The user will build a fire and then be prompt to build the tent."""

	move = input('Build a fire.\n')
	move.lower
	if move == 'matches':
		matches = input('Use matches on what?\n')
		# make the user choose wood
		if matches == 'wood':
			print('You have built the fire!!!')
			tent()
		else:
			fire()
	elif move == 'inventory':
		print(inventory)
		fire()
	else:
		print('Hint: Use ___ to start the fire.')
		fire()

def wood():
	""" The user will have to collect wood that using the axe."""

	move = input('Hint: Collect wood using an ___.\n')
	move.lower()
	if move == 'axe':
		axe()
	elif move == 'inventory':
		print(inventory)
		wood()
	else:
		wood()
		
def forest_03():
	""" The user must build a tent and fire to stay alive. If not, they will
	freeze to death and lose the game."""

	move = input('You are in the forest. It is pitch black and extremely cold.'
		' You must build yourself a fire and pitch the tent. \n')
	move.lower()
	if move == 'fire':
		# prompt the user to get wood
		print('You first need something for that')
		forest_03()
	elif move == 'wood':
		wood()
	elif move == 'inventory':
		print(inventory)
		forest_03()
	else:
		print('Hint: What fuels a fire?')
		forest_03()

def forest_04_01():
	""" This is the forest_04 after the wolf has been killed."""

	move = input('You are in the forest still. It is starting to get darker.\n')
	move.lower()
	if move == 'look':
		# start forest_04_01 over again
		forest_04_01()
	elif move == 'inventory':
		print(inventory)
		forest_04_01()
	elif move == 'north':
		print('You do not want to go north.')
		forest_04_01()
	elif move == 'west':
		print('You are at the end of the forest.')
		forest_04_01()
	elif move == 'east':
		forest_03()
	elif move == 'south':
		print('You are at the end of the forest.')
		forest_04_01()
	else:
		print('Hint: Try using a cardinal direction.')
		forest_04_01()

def wolf_kill():
	""" User can use the bow or the sword to kill the wolf."""
	move = input('\n')
	move.lower()
	if move == 'bow':
		bow = input('Use the bow on what?\n')
		bow.lower()
		if bow == 'wolf':
			print('You have killed the wolf!!!')
		else:
			print('You have been killed by the wolf. You lose.')
			play()
	elif move == 'inventory':
		print(inventory)
		print('There is no time to look! You have been killed by the wolf. You lose.')
		play()
	elif move == 'sword':
		sword = input('Use the sword on what?\n')
		sword.lower()
		if sword == 'wolf':
			print('You have killed the wolf!!!')
			forest_04_01()
		else:
			print('You have been killd by the wolf. You lose.')
			# start the game over again
			play()
	else:
		print('You did not act quick enough! You have been killed by the wolf! You lose!')
		play()

def wolf_attack():
	""" The wolf is attacking the user"""
	
	move = input('The wolf starts running at you!\n What are you going to do?\n')
	move.lower()

	if move == 'bow':
		print('You have killed the wolf!!!')
		# room without the wolf
		forest_04_01()
	elif move == 'inventory':
		print('There is no time to look! You have been killed by the wolf. You loose!')
		play()
	else:
		print('You did not kill the wolf fast enough! You loose!')
		play()

def forest_04():
	""" The user will have to fend off a wild animal."""

	move = input('You are in the forest still. It is starting to get darker. You'
		'can hear a wolf growling in the background. \n')
	move.lower()
	if move == 'look':
		# have the wolf suddenly attack
		wolf_attack()
	elif move == 'north':
		print('You do not want to turn your back on the wolf!!!')
		forest_04()
	elif move == 'west':
		# start forest_04 over again
		forest_04()
	elif move == 'east':
		forest_03()
	elif move == 'inventory':
		print(inventory)
		forest_04()
	elif move == 'south':
		print('You cannot go any further.')
		# start forest_04 over again
		forest_04()
	else:
		print("Hint: 'Look' harder at the wolf.")
		forest_04()

def swordless_cave():
	""" The user is inside a cave without the sword"""

	move = input('You are inside of the cave and have the sword.\n')
	move.lower()
	if move == 'exit':
		forest_02()
	elif move == 'inventory':
		print(inventory)
		swordless_cave()
	elif move == 'look':
		swordless_cave()
	else:
		print('It looks nice outside of the cave.')
		swordless_cave()

def take():
	""" Will allow the user to take the sword."""

	take = ""
	str(take)
	while take != 'sword':
		take = input('What would you like to take?\n')
		take.lower()
		if take == 'sword':
			inventory.append('sword')
			swordless_cave()
		else:
			print("Hint: The sword is for the 'taking'!!!")

def cave():
	""" This function is the cave function. It will allow the user to exit and
	take items that are in the cave."""

	cave_items = ['sword']
	move = input('You are inside of the cave. You see a sword. \n')
	move.lower()
	if move == 'take':
		take()
	elif move == 'exit':
		forest_02_01()
	elif move == 'inventory':
		print(inventory)
		cave()
	elif move == 'look':
		# start cave() over again
		cave()
	else:
		# prompt the user to use look or exit
		print("Try using commands 'look', 'take', or 'exit'.")
		# start cabin() over again
		cave()
		
def forest_02_01():
	""" Will give a brief description of the second forest. This function will
	include the cave."""

	move = input('You are in the forest. You see a cave in the distance. \n')
	move.lower()
	if move == 'cave':
		cave()
	elif move == 'east':
		forest_01_01()
	elif move == 'west':
		print('You are at the end of the forest')
		# run this program again
		forest_02_01()
	elif move == 'north':
		battlefield()
	elif move == 'south':
		# forest_04()
		print('You cannot go this far yet!!!')
		forest_02_01()
	elif move == 'inventory':
		print(inventory)
		forest_02_01()
	elif move == 'look':
		# start from top of program. it will give the same description as move will
		forest_02_01()
	else:
		print("You must choose from a cardinal direction, 'look', 'cave', or 'inventory'.")
		forest_02_01()

def forest_01():
	""" The function the user can use in the first step of the game. Will give
	the user a description of the map"""
	print('You are in the forest and you see a lighted cabin.')
	move = input('\n')
	move.lower()
	if move == 'north':
		battlefield()
	elif move == 'east':
		print('You are at the end of the forest.')
		# start forest_01 over again
		forest_01()
	elif move == 'south':
		print('You cannot go further yet!')
		forest_01()
	elif move == 'west':
		forest_02()
	elif move == 'look':
		print('You are in the forest. You see a cabin.')
		# need to run forest_01 all over again
		forest_01()
	elif move == 'cabin':
		cabin()
	elif move == 'exit':
		forest_01()
	elif move == 'inventory':
		print(inventory)
		forest_01()
	else:
		print('Choose from north, east, south, west, look, and cabin.')
		# run forest_01 again.
		forest_01()

def play():
	play = ""
	""" Will introduce the game to the user based on if the user wants to play."""

	str(play)
	while play != 'yes':
		play = input('Would you like to play this game?\n')
		play.lower()
		if play == 'no':
			break
		elif play == 'yes':
			print('\nYou are a warrior in Mid-evil times that has went A-Wall. '
		' You have nothing on but what clothes the military has provided you'
		' and have decided to take off your armor so it will not weigh you down'
		' throughout your escape. You have lost all of your weapons in the'
		' fierce battle and are just trying to find your way home.'
		' You have ran into the forest to hide from the army so you cannot'
		' be found and can begin to find your way home. It is cold and you are starting'
		' to shiver you need to find shelter and heat before it is completely'
		' dark.\n')
			forest_01_01()
		else:
			print("You must enter 'yes' or 'no'?")
play()