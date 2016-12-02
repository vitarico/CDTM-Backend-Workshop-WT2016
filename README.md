# CDTM-Backend-Workshop

## Introduction
This repository contains everything to conduct a 'Basics Of Backend Development' Workshop targeting people with limited programming experience. In order to successfully use the content provided in this repository, please read the following instructions.

I want to ...
  2. [host a workshop and teach others the 'Basics Of Backend Development'](#1-host-a-workshop)
  1. [do this course just for myself](#2-do-this-course-privately)
  


## 1 Host a workshop 
**IMPORTANT:** This repository is the initial point for conducting a backend workshop with a class of students. It is important that you **DO NOT MODIFY** the repository itself. Instead follow these steps:

### Workflow
1. Either fork or duplicate this repository
   * Fork: Just press the button. 
   * Duplicate
        1. Mirror the repository according to [Mirroring a repository](https://help.github.com/articles/duplicating-a-repository/#mirroring-a-repository)
        2. Duplicate the wiki
           1. Create a wiki page for your new repository
           2. Clone this repository's wiki repository: `git clone https://github.com/FroeMic/CDTM-Backend-Course.wiki.git`
           3. Force push the wiki repository to your new repository's wiki repository: `cd CDTM-Backend-Course.wiki` and `git push --force https://github.com/YOURUSERNAME/YOURNEWREPOSITORYNAME.wiki.git` 
 2. Prepare repository for students
    1. Checkout both the 'master' and 'solution' branch on your local machine
    2. Force delete the remote 'solution' branch (don't delete the branch in your local copy)
 3. Let students fork your new repository. The will only see the 'master' branch
 4. Let the students add your repository's master branch as 'upstream' 
    * Sourcetree Instructions:
        1. Open your forked repo in SourceTree.
        2. Select Repository ➫ Repository Settings… in the menu (or press ⇧⌘,).
        3. In the Remotes pane, press Add.
        4. Enter any name you like (often upstream or master) and the URL / path to the parent repo.
        5. Press OK, then OK.
     * Git Console:
        https://help.github.com/articles/configuring-a-remote-for-a-fork/
 5. Everytime you want to publish a step to the students, merge the specific commit from you **local** 'solution' branch into 'master' and push your changes.
 6. For the students to receive the changes, let them pull from upstream
    * Sourcetree:
        1. Select 'upstream' from 'pull from repository' dropdown
        2. Select 'master' from 'pull from repository' dropdown
        3. Press ok
    * Git console
        https://help.github.com/articles/syncing-a-fork/
  
 **IMORTANT:** For this to work, the students should only work in the folders specified in the exercise instructions.

## 2. Do this course privately
  Please follow the following steps to go trough the workshop
### Workflow
  1. Fork this repository
  2. Check out the master branch of your forked repository locally (e.g. with SourceTree)
  3. For each Tag in the 'solution' branch, beginning with the earliest one
    1. Merge the commit with the respective tag into your 'master' branch
    2. Go through the newly provided lecture material and follow the exercise instructions
    3. Merge the next tagged commit (solution) to get the demo code.
    4. Repeat :-)
