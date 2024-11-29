import sys
import requests
import argparse

argparse = argparse.ArgumentParser()
argparse.add_argument('--username', type=str, required=True)
args = argparse.parse_args()

username = args.username

response_data = requests.get(f"https://api.github.com/users/{username}/events")
if not response_data.status_code == 200:
    if response_data.status_code == 404:
        print(f"Error! The user {username} does not exist on GitHub!")
    else:    
        print(f"Error getting the event data for the username {username}")

    sys.exit(0)
    
github_data = response_data.json()

event_counts = {}

for event in github_data:
    event_counts[event['type']] = 1 if not event['type'] in event_counts.keys() else event_counts[event['type']] + 1

    if event['type'] == 'PushEvent':
        print(f"Pushed {len(event['payload']['commits'])} commit to {event['repo']['name']} repo")
    elif event['type'] == 'CreateEvent':
        print(f"Created a new event in the repo {event['repo']['name']}")
    elif event['type'] == 'IssueCommentEvent':
        print(f"Commented on an issue in the repo {event['repo']['name']}")
    elif event['type'] == 'IssueEvent':
        print(f"{event['payload']['action']} an event in the repo {event['repo']['name']}")
    elif event['type'] == 'PullRequestEvent':
        print(f"Created a pull request on the repo {event['repo']['name']}")
    elif event['type'] == 'DeleteEvent':
        print(f"Deleted an event in the repo {event['repo']['name']}")

print(f"Total number of events in the {username}'s github: {len(github_data)}")
print(f"Counts of each of the event types: {event_counts}")

