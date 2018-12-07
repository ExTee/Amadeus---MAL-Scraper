import utilities
from tqdm import tqdm

def main():
    #Loop through all 
    username_file_path = '../data/processed/usernames.csv'

    with open(username_file_path, 'r') as f:
        usernames = [line.strip() for line in f]
    
    num_scraped = 0
    for username in tqdm(usernames):
        print()
        num_scraped += utilities.get_anime_list_from_user(username)
        print(num_scraped)



if __name__ == '__main__':
    main()
