import utilities

def main():

	#Loop through all clubs
	for club_id in range(1,100000):
		utilities.get_users_from_club(club_id)



if __name__ == '__main__':
	main()