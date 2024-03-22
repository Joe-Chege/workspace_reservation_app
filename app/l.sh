#!/bin/bash

# Add and commit individual changes

# Add and commit changes to app.db
git add app.db
git commit -m "Update app.db"

# Add and commit changes to app/__init__.py
git add app/__init__.py
git commit -m "Update app/__init__.py"

# Add and commit changes to app/bookings/__init__.py
git add app/bookings/__init__.py
git commit -m "Update app/bookings/__init__.py"

# Add and commit changes to app/bookings/routes.py
git add app/bookings/routes.py
git commit -m "Update app/bookings/routes.py"

# Repeat the above process for each file that needs to be committed individually

# After adding and committing all individual changes, push the changes to the remote repository if needed
git push origin main
