import json
# Simplifying the code in Main.py
# Load the following and follower data from JSON files
with open("following.json", "r") as f1, open("followers_1.json", "r") as f2:
    following_data = json.load(f1)['relationships_following']
    followers_data = json.load(f2)

# Extract a list of usernames for the accounts you follow and the accounts that follow you
following = [f['string_list_data'][0]['value'] for f in following_data]
followers = [f['string_list_data'][0]['value'] for f in followers_data]

# Identify accounts that you follow but do not follow you back
not_following_back = set(following) - set(followers)
# Print the usernames of the accounts that don't follow you back
for account in not_following_back:
    print(account + " not following you back")

