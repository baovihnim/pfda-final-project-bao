# 🔎 **I Spy Screen** 
Inspired by I Spy books, this code creates a similar experience: randomizing the positions of a selection of item images, and having the user search for a specified item within the randomized display. 

When the program first starts up, there is a starter screen with instructions: esc key to quit, and space to play. Upon pressing the space key, a selection of randomized items will be displayed, and at the bottom of the screen will tell you what to look for. 

> *I spy with my little eye ... a _____!*

The user can then look for the item, and clicking it will bring them to a win screen. Pressing the space bar again will then repeat, with new randomized positions for the item. Each item found will increase a counter on the win screen, until the I Spy is exited and the counter resets. 

## Repository
< https://github.com/baovihnim/pfda-final-project-bao >

## Demonstration Video
<>

## Repository Files
Outside of the Markdown files and the python program itself, the repository contains a folder of the images that will be randomized within the display. Images are drawn by various friends of mine.

## Design Considerations 
- **Image Adjustment**: items are rescaled to the same dimensions (longest dimension = 175) which allows for all the items to fit in the screen and be roughly uniform in size to have a display that isn't too distracting/confusing. Their location coordinates are chosen through random number generators, which allows for every run of the game to be a little bit different and not too boring. 

- **Collision Prevention**: When the coordinates for the image are first created, they are tested against the items already placed in the display. If the image rectangles collide, or overlap, then the coordinates for the item are regenerated. This is repeated until there is no overlap, to ensure all items can be clearly seen and to prevent the item needed to be found from being hidden by other items. 

- **Point and Click**: Each screen randomly selects one item for the player to find. This item's dimensions are turned into a mask that can be interacted with; the user clicking on this one item's area triggers the win screen. 

## Future Areas for Improvement
- Return to menu: should be able to be navigatable from within the game to, if the player would like to quit the level and switch to a different one, rather than requiring them to quit the game entirely
- Phantom level button: the buttons in which you choose the theme technically remain there the whole game; if the player were to accidentally hit it, it would reset the level/change the theme entirely. 
- Part of the original proposal was that there were multiple findable items per screen. While I think the one item keeps the program simple, it would be interesting to have the originally intended multiple items to find and counter within the I Spy screen/level. 
- I think an added challenge to the search could be fun, such as a timer. If the player doesn't find the item within a certain time, then they lose/automatically quit the level, rather than having it be an infinite loop until the player quits themself. Alternatively, it could be a timer that just tracks how long the player takes to find the item, so that they are trying to get faster and faster if they wish.
- Aesthetics of the game: I think added backgrounds might be fun rather than just the screen filled with a single color. Items could better be sorted, by theme or otherwise, so that the levels look more cohesive. 
- I think just in general I tend to code rather clunkily. Functions could be broken down into more functions as to create greater legibility for others, but it made sense for me to have things combined as I did. 