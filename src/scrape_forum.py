import utilities

def main():
	#Loop through all clubs

	#Serialized run
	for forum_id in range(3274,1751000):
		try:
			utilities.get_users_from_forum_thread(forum_id)
		except:
			pass


if __name__ == '__main__':
	main()
