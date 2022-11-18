# CAP Git and GitHub Workshop 
## Task 1 - Installation and Repo Setup
### a)
First, install git! You can do so by following the instructions [at this link](https://git-scm.com/downloads).

### b)
Now initialise your first git repository. First, create the folder you will store your repository in - call it `cap-shopping-list`. Then navigate into the folder and run the following command:
```sh
git init
```
This will create your repository in the folder! By default, no commits are created, and you will begin in the `main` (or maybe `master`) branch.

## Task 2 - Make some commits!
### a)
First, lets create 2 files and call them `list.txt` and `list2.txt`. Edit the lists to look like this:

**`list.txt`**
```
- Milk
- Eggs
- Carrots
- Cherry tomatoes
```

Now, we're going to make a commit to add the file into version control. 
First, we add the file to the **staging area**, like this:
```
git add list.txt
```
Everything that is **staged** (that is in the staging area) will be added to version control as part of the next commit.

Then, we actually commit our changes:
```
git commit -m "Add list"
```
This will add the commit to version control! The `-m` and following text is the commit message, which should describe what's in your commit.

### b)
Now we'll make some changes to our shopping list. This sheet is a very simple example, but in general each commit should represent one thing done (e.g. adding part of a feature, fixing a bug).

First, add another item, `- Avocados`, to the shopping list. Then commit it like this:
```sh
git add list.txt
git commit -m "Add avocados to list"
```

Next, we're going to make a change to our existing items! Change `cherry tomatoes` to `apples`. Then try figuring out the add/commit commands yourself!

### c)
You should now have 3 total commits. You can check them using the following command:
```
git log
```
Verify you can see all the commits you have made! Press `Q` if you get stuck in this menu.

## Task 3 - Branching out
### a)
We're now going to work with branches to make major changes to our repository. Let's create and move to a new branch called `numbered-list`:
```
git checkout -b numbered-list
```
(`git checkout` moves to a new branch - adding `-b` will create the branch if it doesn't already exist)

In this branch, no make a new commit that changes the list into a numbered list, so it looks like this:

**`list.txt`**
```
1. Milk
2. Eggs
3. Carrots
4. Apples
5. Avocados
```
Make the commit just like you did in task 2.

### b)
Now, let's move back to the `main` branch and see what happens:
```
git checkout main
```
Check `list.txt` again. Your numbering changes should have disappeared! They are now only present (committed) in the `numbered-list` branch.

Now, let's make another branch coming off from `main` - `priority-list`:
```
git checkout -b
```
Make sure you do this in `main`, not `numbered-list`!

In here, make the list a priority list instead of a numbered one like this:

**`list.txt`**
```
- (High) Milk
- (High) Eggs
- (Low) Carrots
- (Low) Apples
- (Critical) Avocados
```
Stage and commit these changes.

### c)
Now, we're going to look at merging - bringing different branches of the repository back together. For our example, we'll be merging `numbered-list` into `main`. 

Merging works by applying all the commits from the source branch (for us `numbered-list`) into the target branch (`main`).

First, move to `master`
```
git checkout main
```
Then, merge in `numbered-list`
```
git merge numbered-list
```
You should now see the changes from `numbered-list` in main!

### d)
Finally, we're going to look at something a bit trickier - merge conflicts. Merge conflicts happen when one commit changes something that another commit also chages.

While still in `main`, try to merge in `priority-list`
```
git merge priority-list
```
This should give you a merge conflict. The lines in `list.txt` have had incompatible commits applied to both - Git now leaves it to you to fix this. `list.txt` should now look like this:

**`list.txt`**
```
<<<<<<< HEAD
1. Milk
2. Eggs
3. Carrots
4. Apples
5. Avocados
=======
- (High) Milk
- (High) Eggs
- (Low) Carrots
- (Low) Apples
- (Critical) Avocados
>>>>>>> priority-list
```

The top part of the divider is the lines found in `main`, while the bottom ones are the ones you are trying to merge.

Now manually edit the file to elegantly fix the merge:

**`list.txt`**
```
1. (High) Milk
2. (High) Eggs
3. (Low) Carrots
4. (Low) Apples
5. (Critical) Avocados
```

Finally, make a commit to merge the resolved changes.

### Task 4 - Pushing and pulling
As a final activity, try hosting this repository, with the full commit history, on GitHub. You'll need to be doing this for the agile project!
