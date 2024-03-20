#!/bin/bash

# Loop through the modified files
for file in $(git status | grep "modified:" | awk '{print $NF}')
do
    # Add the file to the staging area
    git add "$file"
    
    # Commit the file with a descriptive message
    git commit -m "Update $file"
done

# Display status after committing all files
git status
