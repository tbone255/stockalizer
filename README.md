# stockalyzer
Stockalyzer uses Twitter's API to see what stocks people are talking about most, and reports that information back along with news, price info, and technical indicators for those stocks.


# Instructions for setting up
1. Check [here](https://help.github.com/en/enterprise/2.18/user/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) to set up a ssh key with github
2. Copy the whole ssh url from "Clone or download" at the top right of the stockalizer repository
3. Open a terminal, navigate to where you want your local copy of the project to reside
4. Make sure Python 3 is installed on your computer by running `python3`, you should be presented with the python3 shell
5. Run `pipenv`, if it says command is not found, run `pip3 install pipenv`
6. Use `git clone <url>` to clone the repository here
7. Use `pipenv sync` to install all of the dependencies the project currently has


# Instructions for commiting code
1. `git remote update` will download any new code in the repository and keep it in the .git folder (meaning it doesn't merge with your current code)
2. So if master branch has updates, check with `git status` to see if you are on the master branch
3. If you are on the master branch, you can run `git pull origin master` to use the new code in your local branch
4. To make a new branch off of your current branch, run `git checkout -b <branch name>`
5. To add changes, check `git status`, and it'll show you what has changed and how to add these changes
6. After adding changes, make a commit with `git commit -m <commit message in quotes>`
7. Push your changes to the remote with `git push`, but make sure you aren't pushing to the master branch
8. Commit messages should be well written and relatively short, nothing like "Fix" or "Test". It should be like "Fixed Ticker model's CharField being too short".
