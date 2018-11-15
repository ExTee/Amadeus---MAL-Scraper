import utilities

def main():
	#Loop through all clubs

	#Serialized run
	for forum_id in range(1,1750000):
		utilities.get_users_from_forum_thread(forum_id)



if __name__ == '__main__':
	main()
