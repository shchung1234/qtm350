#!/bin/bash
git init
git add .
git commit -m "First commit"
git remote add origin remote repository URL #please change this part to your remote repository url
git remote -v 
git push -u origin master
