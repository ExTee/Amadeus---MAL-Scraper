import utilities

def main():
	#Loop through all clubs

	#Serialized run
	for forum_id in range(3003,1751000):
		utilities.get_users_from_forum_thread(forum_id)
#3002 skipped


if __name__ == '__main__':
	main()
