# W26-Coding-Workshop

Welcome to the Winter '26 Intro to GitHub & Coding Workshop!

In this workshop, CBS members will learn:
- The fundamentals of Git and GitHub workflow
- The fundamentals of Python and R programming
- How to contribute to a programming project on a shared repository

First, make sure you have Git downloaded. Download the correct version based on your operating system here: https://git-scm.com/install/

Here's a GitHub tutorial you can also refer to: https://docs.github.com/en/get-started/start-your-journey/hello-world

---

## Git Workflow
### 1. Create your own copy of the repository
#### Forking
Forking allows you to create a copy of an existing repository on your own account. This lets you make your own changes without changing the original repository. <br/>
Let's try forking this repository! Click the fork button at the top right corner of this workshop repository to create your own copy.
<img width="600" alt="image" src="https://github.com/user-attachments/assets/77505364-91f6-4ae5-b4ec-2e9c855a0d79" />

#### Cloning
Cloning creates a version of the repository on your computer so you can make edits locally. <br/>
Try cloning your forked repository to your local machine. In VS Code or your terminal, run the following command:
```
git clone <your-fork-url>
```
To find your fork url, click on the green code button and copy url as shown below. <br/>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/2cb59a57-5466-4cb2-8d39-fd8b07490974"/>

If you're getting an error saying "Invalid username or token", you may need to create a Personal Access Token. <br/>
Go to Settings -> Developer Settings (at the bottom left) -> Personal Access Tokens. Then generate a token (classic), give access to repo, and set expiration to 7 days. Paste the token when prompted and this should solve the error.

You should now have a local version of the repository on your computer. Open the repository folder on VS Code. The folder structure should look something like this: <br/>

<img width="256" height="173" alt="image" src="https://github.com/user-attachments/assets/b7afc7a2-6b51-4f58-80b5-dd7a0a855a91" />


### 2. Create a branch
Branching creates an individual environment for you to make your own changes, without affecting the main branch. Once you submit your branch, it will be reviewed and your changes can be merged back to the main branch. This allows multiple people to safely collaborate on a project.

First, make sure you're inside the repository using:
```
cd W26-Coding-Workshop
```
Then, create a branch with a descriptive name using:
```
git checkout -b <your-name-python>
```
To check the branch you're currently working on, use:
```
git branch
```
The current branch will have a `*` next to it. <br/>

**Note:** If you want to switch to another branch, use the command:
```
git checkout <branch-name>
```

### 3. Make and save changes
Now that you're working on your own branch, let's practice some programming skills! <br/>
Navigate to the folder of the language you want to work on using:
```
cd python
# or
cd r
```
Create a new file using the following naming structure so we can keep track of your work:
```
touch yourname_task.py
# or
touch yourname_task.R
```
On VS Code, you can also create a new file by right clicking in the designated folder (either python/R), and selecting New File.

**Practice:** Each folder will have a README.md file with fundamentals of each programming language. Use these tutorials to create a small programming exercise that showcases a fundamental python or R skill. Be sure to save your work as you go!

To see your new file and any modified files, use command:
```
git status
```

### 4. Push to GitHub


### 5. Open a pull request
### 6. Sync your local repo

---

## Repository Structure
This repository is organized into:
- `challenges/` — Optional coding challenges
- `python/` — Python exercises
- `r/` — R exercises

Each folder contains its own README with contribution instructions.
