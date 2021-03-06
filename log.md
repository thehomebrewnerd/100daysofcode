# 100 Days Of Code - Log

## Since I developed my own progress log web application all my future posts will there instead of in this log. [Click here to check out the website log.](https://code100blog.herokuapp.com)

### R1D1: Jan 4, 2018

**Today's Progress**: Forked GitHub repo and personalized files. Added several reference links. Worked through [this tutorial](https://medium.freecodecamp.org/how-to-build-an-ai-game-bot-using-openai-gym-and-universe-f2eb9bfbb40a) on building an AI game bot. Attempted to change the game to an Atari 2600 game but got stuck with the required libraries not installing correctly. Pushed all the updated code to GitHub

**Thoughts:** There are two main things I would like to accomplish duing my 100 days:
1. I want to build a successful AI Bot that will be able to successfully play (dare I say master) a classic video game (think Atari or NES). Why? Becasue I want to improve not only my coding skills but learn more about AI and reinforcement learning in particular.
2. I want to learn to develop and deploy web applications with Django. Why? I have an idea for a new web app that I want to develop. Why Django? I am already pretty familiar with Python so Django seems like a good place to start.

**Link to work:** Nothing for today - stay tuned!

### R1D2: Jan 5, 2018

**Today's Progress**: Got the right OpenAI libraries installed for Atari games. Followed [these instructions] (https://gym.openai.com/docs/) for the initial install. Then I installed `cmake` with the command `brew install cmake` since I'm running OSX. Finally, I installed the Atari dependencies with these [instructions](https://github.com/openai/gym#atari). Got a basic Ms. Pacman game running with random moves for now.

**Thoughts:** Not a lot of coding today - mostly reading and installing the right libraries so I can do what I want in the future. Gotta start somewhere!

**Link to work:** [Ms. Pacman Game Code](https://github.com/thehomebrewnerd/100daysofcode/blob/master/ai-game-bot/simple-ms-pacman.py)

### R1D3: Jan 6, 2018

**Today's Progress**: Switched gears a little bit and starting building a Django blog app from [this tutorial](https://djangoforbeginners.com/blog/). Eventually hope to use that blog as my place to log my 100 days progress. Got everything working locally today, but for now can only create posts via the Django admin interface.

**Thoughts:** Quite a bit more to do on the blog app. Need to add a form to allow posts to be created and add a login page to allow multiple users to use the site. Also want to updated the fields to be consistent with this log format. Finally need to get it hosted online somewhere.

**Link to work:** 

### R1D4: Jan 7, 2018

**Today's Progress**: Added a form to add new posts to the blog app. Also added the ability to modify and delete posts. Also added some CSS styling to make the page look a bit like an old monochrome computer terminal with a black/green color palette.

**Thoughts:** Next up, I need to add a login page to allow multiple users to use the site. Need to add fields to track created and updated dates, and a the ability to add a link to work. Finally need to get it hosted online somewhere.

**Link to work:** 

### R1D5: Jan 8, 2018

**Today's Progress**: Added the ability for new users to create accounts and login/logout. Also updated the post data model to include date created and date updated, along with a link to work.

**Thoughts:** Need to do a bit of cleanup so that users can only edit/delete thier own posts. Also want to require signing up and logging in before creating a new post. Need to do a bit of layout and CSS cleanup as well. Finally need to get it hosted online somewhere. Also need to look into switching from SQLite to something more production ready like PostgreSQL.

**Link to work:** 

### R1D6: Jan 9, 2018

**Today's Progress**: Did some cosmetic CSS work today - added better navigation. Added a cool interesting animation based on [this post](https://blog.carbonfive.com/2015/01/07/vintage-terminal-effect-in-css3/). Made it so users can edit only thier posts and that new posts can only be created by people who are logged in.

**Thoughts:** Soon, I need to get it hosted online somewhere, and need to look into switching from SQLite to something more production ready like PostgreSQL.

**Link to work:** 

### R1D7: Jan 10, 2018

**Today's Progress**: Fixed a couple bugs that would have allowed people who were not logged in to create/edit/delete entries or to modify posts from others. Installed PostgreSQL locally and migrated the database to that from SQLite.

**Thoughts:** Getting pretty close to being ready to push it live. Just a few more minor display issues to take care of first.

**Link to work:** 

### R1D8: Jan 11, 2018

**Today's Progress**:  Figured out how to default the post author to the currently logged in user! Also managed to fix a couple minor formatting issues at least.

**Thoughts:** Next, up I think I'm ready to push this live and start using it for my log in the future...and will let others use it as well.

**Link to work:** 

### R1D9: Jan 12, 2018

**Today's Progress**:  Completed some modules on [Treehouse](https://teamtreehouse.com/home) on Python and Django. Didn't do as much coding as I would have liked today, but did start building out the shell for a homebrewing web app idea I have.

**Thoughts:** Hopefully this weekend I can get the blog app pushed to a server somewhere so it can go live, and also hope to make some more progress on the homebrewing web app.

**Link to work:** Nothing for today

### R1D10: Jan 13, 2018

**Today's Progress**:  Did some cosmetic clean up on the submit/edit forms to align all the field, increased the text size. Added a couple new fields to the model to capture Round and Day information.

**Thoughts:** Hopefully this weekend I can get the blog app pushed to a server somewhere so it can go live, and also hope to make some more progress on the homebrewing web app.

**Link to work:** Nothing for today

### R1D11: Jan 14, 2018

**Today's Progress**:  Started trying to deploy the blog app to Heroku, but since I am using Anaconda instead of virtualenv to manage my environment, it's not a simple as I hoped. Taking a break and working through some Treehouse modules instead. Will come back to deploy tomorrow..

**Thoughts:** Nothing much today - kinda of taking a little break from coding to recharge today. Hope to get back into it a bit more tomorrow.

**Link to work:** Nothing for today
