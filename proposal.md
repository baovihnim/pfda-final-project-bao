# I Spy Screen

## Repository
< https://github.com/baovihnim/pfda-final-project-bao >

## Description
Inspired by I Spy books, this code should create a similar experience: randomizing the positions of a selection of item images, and having the user search for select items within the randomized display. 

## Features
- Menu and theme selection
    - There should be an opening screen/landing menu that branches into the actual I Spy portions of the code. This will likely utilize pygame-menu.
- Asset Position Randomization
    - Likely will utilize random and randrange, in order to vary the position of the images whenever the game is reset. 
- Point and Click User Interaction
    - Certain listed image assets will be made able to be found and clicked. Selecting the proper item will gray out the image. 
- Item Counter
    - There should only be a certain number of findable items per screen--a counter should be made, tied to the point and click assets to keep track of completion.

## Challenges
- Pygame will have to be further researched and utilized for point and click elements. 
- Pygame needs to be further researched in its implementation of menu screens/levels. It looks like you can use the original Pygame library, or a specific pygame-menu library. 
- I would like to look into optimization, storage, and sorting for large amounts of images/assets.

## Outcomes
Ideal Outcome: 
- The ideal outcome is an interactive screensaver-esque program. Taking inspiration from I Spy books, the program should be able to utilize a group of image assets and randomize their position within a screensavor/display. This display should also have user interaction--the program should select a few items from the image assets and list them for the user to "find." These assets should be made interactable within the display, so that the user can search for and click on the items. Ideally there will be different (likely around 3) levels or themes that the user can select from (which would require a menu/selection screen as well)

Minimal Viable Outcome: 
- The minimal result likely would not need to have the multiple levels or menu screen. The main features for the minimal outcome are the randomized location of the item image assets and the ability for some of them to be clicked and added to a counter for "spied"/found items.

## Milestons
- Week 1
    1. Asset Collecting/creating: designing items or editing pngs that can be arranged by the code
    2. Creating Base Screen Display and superimposing assets on top: find a way to randomize position without creating too much overlap

- Week 2
    1. Implementing User Interaction for select items: will also need to figure out how the items meant to be "found" will be listed for the user to know, as well as editing the image once it is "found" to differentiate it from the rest of the screen
    2. Item Counter: keeps track of "completion" of a level/how many of the items made to be interacted with have been interacted with properly

- Week N (Final)
    1. Menu Screen and Level Branching: different levels utilize same code as standard level/as each other, just with a different item asset list likely
    2. Polishing