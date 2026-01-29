# Step 1: Create a new GH Repo on GH Platform with .gitignore, README.md, liscense, description, title, etc.

# Step 2 - a: Copy that GH Repo's link; Go to your desired location on your PC where in VSC open integrated terminal; Write: git clone pasteLink
# Step 2 - b: Create a folder on your PC & open it in VSC integrated terminal; git remote add origin pasteLink; git push --set-upstream origin master

# Step 3: git init ; git add . ; git commit -m "Initial Commit" ; git push ; git status
# Step 4: (create & switch to a new branch) git checkout -b feature/my-profile | OR | git switch -c feature/my-profile
# Step 5: echo "# Line 01" < README.md  ;  echo "## Line 02 To Not Replace Previous Line" << README.md
# Step 6: ..............................;  git push --set-upstream origin feature/my-profile

# Other Useful Git Command Line: git log --oneline (View commit history); git diff (View differences before committing); git remote -v (View remote repositories); git reset --soft HEAD~1 (Undo last commit but keep changes); git reset --hard HEAD~1 (Undo last commit and discard changes (careful!)); cd / mkdir / touch;

print("Hello World!")