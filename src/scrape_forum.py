import utilities



def main():
	#Loop through all forums

	#Serialized run
	for forum_id in range(276068,1751000):
		try:
			utilities.get_users_from_forum_thread(forum_id , ignore_present = True)
		except:
			pass


if __name__ == '__main__':
	main()
