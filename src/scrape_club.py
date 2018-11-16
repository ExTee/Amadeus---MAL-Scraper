import utilities
import multiprocessing as mp

def main():
	#Loop through all clubs

	#Serialized run
	for club_id in range(30000,100000):
		utilities.get_users_from_club(club_id,"../data/club_usernames/30000-100000/", ignore_present = True)


'''
	Scrapes clubs from ClubID start to end. Used for Parallelization.

	Args:
		r	: tuple (start, end)
'''
def parallel_scrape_club_range(r):

	start = r[0]
	end = r[1]

	for club_id in range(start, end):
		utilities.get_users_from_club(club_id)

'''
	Sends requests parallel.
	Use at your own risk. Requests migh
'''
def parallel_scrape_club_usernames():
	#Parallel run
	pool = mp.Pool(processes = 4)

	pool.map(
		scrape_club_range,
		[(1000,1005),(1005,1010), (1010,1015), (1015,1020)]
		)



if __name__ == '__main__':
	main()
