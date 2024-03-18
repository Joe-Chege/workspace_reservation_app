#!/bin/bash

# Add and commit each HTML file in the rooms directory
git add app/templates/rooms/create.html
git commit -m "Add create.html for rooms"

git add app/templates/rooms/details.html
git commit -m "Add details.html for rooms"

git add app/templates/rooms/index.html
git commit -m "Add index.html for rooms"

git add app/templates/rooms/update.html
git commit -m "Add update.html for rooms"

# Add and commit each HTML file in the bookings directory
git add app/templates/bookings/accept.html
git commit -m "Add accept.html for bookings"

git add app/templates/bookings/complete.html
git commit -m "Add complete.html for bookings"

git add app/templates/bookings/create.html
git commit -m "Add create.html for bookings"

git add app/templates/bookings/details.html
git commit -m "Add details.html for bookings"

git add app/templates/bookings/update.html
git commit -m "Add update.html for bookings"

# Add and commit each HTML file in the auth directory
git add app/templates/auth/account.html
git commit -m "Add account.html for auth"

git add app/templates/auth/login.html
git commit -m "Add login.html for auth"

git add app/templates/auth/register.html
git commit -m "Add register.html for auth"

echo "All files added and committed successfully."
