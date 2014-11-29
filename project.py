inventory = []
# code inventory in all functions
# code take into cave()
# put hint to kill the stranger
# create a new cabin with dead stranger so user can go back without having to kill the stranger again
# fix take function for inside of the cabin.
# don't allow user to go south until after killing the stranger
#

def village_01():
	""" The user will enter the village where a store is located. The user will
	have to get flowers from the store that is in this section of the village."""

	move = input('You are now in the village. You see a store and have an idea.\n')
	move.lower()
	if move == 'store':
		store()
	elif move == 'look':
		village_01()

def store():
	""" The user will enter the store and have to get flowers."""

	move = input('You have entered the stores and see flowers that are for sale .'
		' along with a civilian looking at them. You decide that you would '
		' like to get them and take them home to your family.'
		' You need to speak to someone.\n')
	move.lower()
	if move == 'speak':
		speak()

def speak():
	""" The user will speak to a civilian and or a clerk."""

	speak = input('Speak to whom?\n')
	speak.lower()
	if speak == 'salesman' or 'clerk':
		salesman()
	elif speak == 'civilian':
		civilian()
	else:
		speak()

def salesman():
	""" The user will have a conversation with the salesman."""

	move = input('You have striked a conversation with the salesman. You now'
		' need to convince the salesman to help you out and get some flowers.'
		' You have two options: steal or ask')
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
		inventory = inventory.append('flowers')
		store_exit()
	else:
		salesman()

def store_exit():
	""" Allows the user to exit the store."""
	village_01_01()

def village_01_01():
	""" The user now has the flowers and needs to go home to his/her family."""

	move = input('You now have the flowers and are excited to go home to your '
		'family\n')
	move.lower
	if move == 'north':
		print('That is the forest, you want to go home.')
	elif move == 'east':
		village_02()
	elif move == 'south':
		print('You are at the end of the village.')
	elif move == 'west':
		print('You are at the end of the village.')
	elif move == 'look':
		print('You see your home in the east.')
	else:
		village_01_01()

def village_02():
	""" The user enters the part of the village where the home is at."""

	move = input('You are in the part of the village where your home is at.\n')
	move.lower()
	if move == 'home':
		home()
	else:
		print('You need to go home.')
		village_02()

def home():
	""" The user enters the home."""
	move = input('You have entered the home with flowers in your hand.\n')
	move.lower()
	if move == 'flowers':
		flowers()
	else:
		print('You need to give the flowers to your family.')
		home()

def flowers():
	""" The user gives the flowers to his/her family and wins."""

	print('You give the flowers to your family. You won the game!!!')
	# start the game over again
	# play()


def battlefield():
	"""Will tell the user that they have died and will prompt the user to start
	the game over again"""
	print('You have just ran back into battle with no weapons or armor.'
			'You have just been killed brutely.')
	# starts the game over again
	play()

def cabin():
	""" Gives a user a brief description of the cabin. The user will find
	someone in the cabin and have to kill them using weapons previously found."""

	move = input('You enter the cabin and find a stranger. You startle the stranger.'
		'The stranger quickly pick up his bow with a loaded arrow and points'
		'it at you. You then...\n')
	move.lower()
	if move == 'exit':
		forest_01()
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
	cabin_items = ['bow', 'axe', 'matches']
	if move == 'take':
		take = input('Take what? \n')
		take.lower()
		if take == 'bow':
			inventory = inventory.append('bow')
			cabin_items = cabin_items.remove('bow')
			take_bow()
		elif take == 'matches':
			inventory = inventory.append('matches')
			# remove item from the cabin
			cabin_items = cabin_items.remove('matches')
		elif take == 'axe':
			inventory = inventory.append('axe')
			cabin_items = cabin_items.remove('axe')
		else:
			print("You need to collect things from here. Hint: Use 'look'.")
			killed_stranger()
	elif move == 'look':
		killed_stranger()
	else:
		print("You need to collect things from here. Hint: Use 'look'.")
		killed_stranger()

def day_forest_03():
	""" The user will wake up and see the village."""

	move = input('It is now morning. You exit the tent and can see your village'
		' south from where you are standing!\n')
	move.lower()
	if move == 'look':
		day_forest_03()
	elif move == 'north':
		forest_01()
	elif move == 'east':
		open_field()
	elif move == 'south':
		village_01()
	elif move == 'west':
		forest_04_01()
	elif move == 'inventory':
		return inventory
	else:
			day_forest_03
			
def sleep():
	""" The user will need to sleep to continue on."""

	move = input('It is getting very late. You are very tired. \n')
	move.lower()
	if move == 'sleep':
	    print('You go to sleep.')
	    day_forest_03()

	else:
		sleep()
		
def enter_tent():
	""" The user will need to enter the tent and stay the night."""

	move = input('It is getting darker. Your tent is built next to the fire. \n')
	move.lower()
	if move == 'enter':
		print('You have entered the tent.')
		sleep()
	else:
	    enter_tent()

def tent():
	""" The user will build a tent. They will have to build a tent to surivive."""

	move = input('Build a shelter.\n')
	move.lower()
	if move == 'tent':
		print('You have built the tent!!!')
		enter_tent()
	else:
		tent()

def fire():
	""" The user will build a fire and then be prompt to build the tent."""

	move == input('Build a fire.\n')
	move.lower
	if move == 'matches':
		matches = input('Use matches on what?\n')
		# make the user choose wood
		if matches == 'wood':
			print('You have built the fire!!!')
			tent()
		else:
			fire()

def wood():
	""" The user will have to collect wood that using the axe."""

	move = input('Collect wood.\n')
	move.lower()
	if move == 'axe':
		axe = input('Use axe on what?\n')
		axe.lower()
		if axe == 'tree':
			inventory.append('wood')
			# prompt the user to use the wood to start fire
			fire()
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
	else:
		forest_03()

def forest_04_01():
	""" This is the forest_04 after the wolf has been killed."""

	move = input('You are in the forest still. It is starting to get darker.\n')
	move.lower()
	if move == 'look':
		# start forest_04_01 over again
		forest_04_01()
	elif move == 'north':
		forest_02()
	elif move == 'west':
		forest_04_01()
	elif move == 'east':
		forest_03()
	elif move == 'south':
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
	elif move == 'sword':
		sword = input('Use the bow on what?\n')
		sword.lower()
		if sword == 'wolf':
			print('You have killed the wolf!!!')
			forest_04_01()
		else:
			print('You have been killd by the wolf. You lose.')
			# start the game over again
			play()

def wolf_attack():
	""" The wolf is attacking the user"""
	wolf_kill()

def forest_04():
	""" The user will have to fend off a wild animal."""

	move = input('You are in the forest still. It is starting to get darker. You'
		'can hear a wolf growling in the background. \n')
	move.lower()
	if move == 'look':
		# have the wolf suddenly attack
		wolf_attack()
	elif move == 'north':
		forest_02()
	elif move == 'west':
		# start forest_04 over again
		forest_04()
	elif move == 'east':
		forest_03()
	elif move == 'south':
		# start forest_04 over again
		forest_04()

def swordless_cave():
	""" The user is inside a cave without the sword"""

	move = input('You are inside of the cave and have the sword.\n')
	move.lower()
	if move == 'exit':
		forest_02()
	elif move == 'look':
		swordless_cave()
	else:
		swordless_cave()

def take():
	""" Will allow the user to take the sword."""

	take = ''
	while take != 'sword':
		take = input('What would you like to take?\n')
		if take == 'sword':
			swordless_cave()
		else:
			print('The sword is up for the taking!!!')

def cave():
	""" This function is the cave function. It will allow the user to exit and
	take items that are in the cave."""

	cave_items = ['sword']
	move = input('You are inside of the cave. You see a sword. \n')
	move.lower()
	if move == 'take':
		take()
	elif move == 'exit':
		forest_02()
	elif move == 'look':
		# start cave() over again
		cave()
	else:
		# prompt the user to use look or exit
		print("Try using commands 'look' or 'exit'.")
		# start cabin() over again
		cave()
		
def forest_02():
	""" Will give a brief description of the second forest. This function will
	include the cave."""

	move = input('You are in the forest. You see a cave in the distance. \n')
	move.lower()
	if move == 'cave':
		cave()
	elif move == 'east':
		forest_01()
	elif move == 'west':
		print('You are at the end of the forest')
		# run this program again
		forest_02()
	elif move == 'north':
		battlefield()
	elif move == 'south':
		forest_04()
	elif move == 'inventory':
		return inventory
		forest_02()
	elif move == 'look':
		# start from top of program. it will give the same description as move will
		forest_02()
	else:
		print('You must choose from a cardinal direction, look, or inventory.')
		forest_02()

def forest_01():
	""" The function the user can use in the first step of the game. Will give
	the user a description of the map"""
	print('You are in the forest and you see a cabin.')
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
	else:
		print('Choose from north, east, south, west, look, and cabin.')
		# run forest_01 again.
		forest_01()

def play():
	play = ""
	""" Will introduce the game to the user based on if the user wants to play."""

	str(play)
	while play != 'yes':
		play = input('You are a warrior in Mid-evil times that has went A-Wall. '
		' You have nothing on but what clothes the military has provided you'
		' and have decided to take off your armor so it will not weigh you down'
		' throughout your escape. You have lost all of your weapons in the'
		' fierce battle and are just trying to find your way home.'
		' You have ran into the forest to hide from the army so you cannot'
		' be found and can begin to find your way home. It is cold and you are starting'
		' to shiver you need to find shelter and heat before it is completely'
		' dark.\n Would you like to play?\n')
		play.lower()
		if play == 'no':
			break
		elif play == 'yes':
			forest_01()
		else:
			print("You must enter 'yes' or 'no'?")
play()