Implementation of https://roadmap.sh/projects/github-user-activity

# Introduction
This CLI application takes in a github username and retrieves all the events that are publicly available for that user on Github and prints each event out along with the summary at the end.

# Installation

```
pip install -r requirements.txt
```

# Running the application

```
python3 app.py --username AgentT30
```

## Output

```
Pushed 1 commit to AgentT30/roadmap_sh repo
Pushed 1 commit to AgentT30/roadmap_sh repo
Created a new event in the repo AgentT30/roadmap_sh
Created a new event in the repo AgentT30/roadmap_sh
Pushed 1 commit to AgentT30/roadmap_sh repo
Created a new event in the repo AgentT30/roadmap_sh
Created a new event in the repo AgentT30/roadmap_sh
Commented on an issue in the repo bhavnicksm/chonkie
Created a pull request on the repo ente-io/ente
Created a new event in the repo AgentT30/ente
Deleted an event in the repo AgentT30/ente
Total number of events in the AgentT30's github: 12
Counts of each of the event types: {'PushEvent': 3, 'CreateEvent': 5, 'IssueCommentEvent': 1, 'IssuesEvent': 1, 'PullRequestEvent': 1, 'DeleteEvent': 1}
```

