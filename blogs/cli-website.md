---
title: "Coding Adventures: Making a CLI-themed Personal Website"
date: 
tags:
  - coding_adventures
  - tech
image: portfolio.png
---
## Coding Adventures: Making a CLI-themed Personal Website

Recently, I’ve been inspired by [https://natanel.ca/](https://natanel.ca/), a website created by a friend of mine. Making a personal website in the interface of a CLI is super nerdy, and I love it.

I knew immediately when I saw it I wanted to make a similar version for my website.

## Goal for this project

My goal for this project is to implement the functionality that I want (which you’ll find below), in a manner that is **modular**, **scalable**, and **maintainable**. Software for personal projects is often none of these things, which is generally acceptable. After all, you’re the only one working on them, so as long as you can accept the consequences of your code, it’s fine. However, I’ve seen enough shitty code in industry, and have written plenty of poorly designed software myself, that I’m making it a deliberate goal for this project to make *every line* as elegant as possible.

## Design

### Design Planning

As a CLI themed website, I wanted to implement the most important CLI commands. I was originally thinking of having commands for each subpage, and then an instruction for each. However, I think this would be very simple to implement and it would be more complex to have all the features I would want (it could get cluttered). Because of all of these reasons, I want to implement directories. It adds some complexity in structuring commands, and adds room to implementing cd and ls commands. This way, it separates functionality into subdirectories, and isn’t super overwhelming for a user.

I wanted to be intentional about how this integrates with my current website platform. I’ve spent A LOT of time making it modular, storing all of the assets separately, so modifying the content and changing the design of the website are two completely separate tasks. I want to use all of this work in the new version of the website, so when I update content, it automatically is updated on the CLI (probably using a fetch request).

I currently have my website hosted at [owenmoogk.github.io](https://owenmoogk.github.io/), and subprojects, hosted in subpages. For example, my pathfinding visualization project is found at [owenmoogk.github.io/pathfinding-visualizer](https://owenmoogk.github.io/pathfinding-visualizer/). I decided to keep my previous website, but instead build this as an addition. So, it would be stored in a subpage, /os or /cli or something like that.

By using the same homepage, it probably also makes fetch requests easier too (they’re not cross origin). Not 100% sure about that though, don’t know enough about web security.

### Off to the Races

As with *almost all *projects, I got off to the races. I knew this was bad… but I thought I had it figured out. I did a good job of getting ChatGPT to write the general page layout and CSS, and had to do some fiddling with the input focus, because if the user clicked off of the input box and started typing, the website still had to recognize it. And it actually looked decent!

![Using some basic commands (ls, help, about)](https://cdn-images-1.medium.com/max/3762/1*a4ObB1cUa60wdo0BZ283GQ.png)

Some small issues, but generally going well! The bigger issue: I didn’t have an idea of how I wanted to implement file paths.

I thought it would be fine, as I had no problem implementing commands, and even made classes and types to structure the flow of code. However, immediately when I tried to think about how directories would be implemented I ran into issues.

### Making Directories

I went to my first Socratica working session this week! It’s a nice place to meet people and spend some dedicated time on work (that's not schoolwork). I liked the vibe of everyone dedicating time to something that they loved doing, not to land a job. In the spirit of this new intentionality, I decided to draw out some plans for how I would surpass these issues (for good).

My initial plans (don’t worry, I’ll explain the messiness below):

![](https://cdn-images-1.medium.com/max/2000/1*xWSW_4gpFjlNBbAJhnc9gw.png)

![My messy block diagram — trying to implement directories](https://cdn-images-1.medium.com/max/2000/1*6xfE9cDIl1yI2PWuTaTJ3g.png)

The first block is straightforward, take some input text from the user, and hand it off to the command handler. The command handler has the functionality of parsing the input, and getting the specific command and arguments. Then, it will get the current path class (in red).

I decided to split each path up into a class (or instance of a type), because it will have it’s own functions and path name. This way, path specificity can be implemented (ie. A command can be valid in the /projects directory, but not in the root directory). This is helpful for a command like openproject .

From there, it can get the function, run it, harvest the return value, and pass it back to the CLI handler. Notice the green text, I say “This is probably bad practice”. Instead of the command being able to output to the console, it has to pass its output back to the handler. This is because of how states are implemented in react: updating a state causes a re-render of the page), so updating the state twice can lead to issues with asynchrony. Because I’m storing inputs/outputs in a state, it causes problems. This is somewhat limiting, because a command can’t have its own inputs, and has to output everything all at once. However, for these purposes… I’m making the decision that it’s ok.

### Global Path

There’s one issue left, how to implement global commands? The first thought I had was to make a global class that just had the global commands (this would work for commands like about, help, open, as they all have an essentially hard-coded output). However, this wouldn’t directly work for commands like cd and ls . They require path-specific knowledge to operate, however, should operate everywhere.

![Path Structure](https://cdn-images-1.medium.com/max/2128/1*DAbIuo67H6Co0L3J-kSMQw.png)

Each path instance will have its name, and pointers to it’s children (shown in red). We also have a global class, that contains the global functions. Maybe we could pass the path and path info to the global class, so cd and ls can do their jobs? Or maybe, we could combine them…

### Weighing Options

When deciding how to implement cd and ls, I had a few thoughts. I think when presented with a design choice, it’s important to not jump to the first conclusion, but instead list a few viable options and then narrow it down. This gives more time for brainstorming, and maybe an idea that would have never been brought to the table otherwise.
>  **A small tangent on this exact point:**
>  When working at a R&D design hub this winter, I was brainstorming ways to implement some mechanical functionality using hardware, 3D printing, and some actuators (I’m intentionally being vague so I don’t get sued). I thought I had a pretty good idea, and drew it on the whiteboard. I had been having some debates with a co-worker about design planning, between the philosophy of “jump right into SolidWorks” VS “draw and plan first”. I asked for some feedback on my design, and we both agreed it wasn’t bad. However, I didn’t want to rush it. This was a big undertaking that would last a few months, and I didn’t want to get stuck in a bad design.
>  
>  I spent the next hour drawing different ideas on the board, and they were all pretty awful. It was like brainstorming how to get to space, drawing a rocket, and then saying “let’s go back to first principles”, drawing a space elevator, a massive slingshot and a nuclear bomb. Most of my ideas were not only bad, but also probably not viable given the use cases. I sat back, looking at my 6 drawings, thinking to myself “I should have just gone with the first one”. However, I was committed to optimization, so I weighted up the pros and cons. The first idea was pretty good. It was far better than it’s immediate successors. However, the last idea I had come up with had some advantageous aspects, so I explored it a bit further. After discussing with my coworkers, we combined helpful aspects of both designs, noticing some previously unforeseen flaws in the first design. We were able to easily surpass them by combining our brainstormed ideas.
>  
>  All of a sudden, I was quite relieved. I thought about how the design process would have gone if I had just gone with my first plan. I realized that we would have ran into issues months into development, and we avoided it through an hour with a whiteboard, some shitty ideas, and a small dose of critical thinking.
>  I think about this a lot. It keeps coming back to me whenever I’m working on any design. And most importantly, it gives me a reason to think through alternatives, even when I think I have the best solution.

Whew! That was a longer tangent than I expected it to be!

So, applying this knowledge I weighed up some options. Some thoughts I had for implementing these cd and ls commands:

 1. Define the functions locally in every path. This is one of those ideas that pop into your head immediately, however, I would hope most software developers (and really anyone with a brain) are quick to reject (or at least dispute). This would mean a lot of repeated code, and also hard-coded paths, which would lead to a less modifiable codebase (if I change a file path/structure, how many other places do I have to update the code..? Ideally: zero).

 2. Define it in the command handler as a special case. This is not inherently bad and would implement all of the functionality we want. It would divide global commands into two separate places, which could get messy for adding more commands, and for reusing and modifying code.

 3. Put these functions in the global path class. This is the ideal solution because it keeps all of the global functions together, and can make them all use the same dependencies (without too much headache for imports in multiple spots). This also would be similar to how Windows works with environment PATH variables, so even though it’s a completely different subset of problems, it gives me some confidence that other developers came up with a similar solution.

After weighing the pros and cons listed above, option 3 is probably the best. You might ask… “Owen, you just said this wouldn’t work because it doesn’t know the current path. How would this work?” Well, we can just pass the path info! In hindsight, this is the obvious solution, but it took me some time to get here! It’s almost a full circle, and I had to go through a bunch of other ideas to get there.
>  Sidenote:
>  I actually didn’t even realize how similar this is to the big tangent above. Have a decent idea, go through a bunch of bad ones, and end with an even better one.
>  Glad I’m writing this blog… I probably wouldn’t’ve picked up on that! Gives me some more faith in the design process *😅.*

Ok… that’s a lot of design, for something I thought was going to be quite simple! I’m going to try and code it up!

### A complete project! (kind of)

After coding it up, it works really well! I’ve been able to play around with it and expand it to include projects, contact, and a work directory, and they work really well. I even made it expandable for nested directories.

A small change that I had to make was having the children directories point to their parents, instead of the other way around. It makes some of the cd logic a bit more complex, however this simplified many of the processes in storing the path, and navigating up a level. Ideally, this would be a two-way linked tree (kind of like a doubly linked list, except in this case it would be the child and parent both referencing each other). However, I decided to abandon this because I don’t have database enforcement, it’s all hard-coded in .tsx files. It would have made the code simpler, however when I added or modified a directory, it would have to change in two places. And, forgetting this would break the directory structure.

I got a GPT model to give me some cd code that works really well (there’s actually some nuance to account for relative paths, ../ identifiers, and absolute paths. With some through testing I’m happy with what it gave me 😅.

Additionally, I split up the global commands slightly differently as described in the above diagram. I actually included the about and the open commands in the root directory, because I thought it was quite cluttered to include those in the so-called PATH, available everywhere in the terminal.

### API Integration

Something I enjoy about my current website is that all of the source files are JSON files, that are accessible publicly via an API. I go into more detail into that in my ‘[Building an Awesome Portfolio](https://medium.com/@owenmoogk/making-an-awesome-personal-portfolio-8ade5cfc52ce)’ blog, but in essence anything can pull the most up-to-date content from my website, without changing code.

Using this, I actually made the projects directory use this API, so if I ever add a project to my website, it will automatically be added to this CLI as well! It’s a nice way to only write things once and not have multiple sources to update, which I’m quite happy about (and saved me from hard-coding a lot of content)!

This is the sort of design decision that I hope will keep this project alive and relevant, long after I stop maintaining it.

## Learnings

I actually left this project in the works for almost 6 months, untouched. In the meantime, I had completed an internship where I *massively *improved my coding skillset.

However, coming back to the project, I was actually still pretty impressed with the state of the project. Using this blog — which was in progress at the time — was a great way to get caught up, and back into the frame of mind that I was in when making these design decisions. Although somewhat a small project, this has really shown that internal documentation is quite important for any project that doesn’t have people actively working on it. Even without turnover (in this example, I was the person working on it both before and after a break), it’s still incredibly helpful to remember *why *a decision was made. This can prevent a ton of rework, and making the same mistakes twice.

Some anecdotal evidence of this: I was actually about to redesign and rework the directory structure for this project, but I had a read over my previous documentation and remembered that I had already tried — and failed — at the strategy I wanted to implement.

And now it’s done! I published it at [https://owenmoogk.github.io/os/](https://owenmoogk.github.io/os/), and hopefully it’s usable (at least as much as it can be for a command line). One idea I have as a future improvement is an autocomplete feature that would allow a user to hit tab to select commands and arguments, but it’s pretty minor. I already implemented arrow control to go through command history, and that makes me happy enough that I probably won’t make more usability improvements, but you never know (it’s good enough!).

Huge shoutout to Natanel, at [https://natanel.ca](https://natanel.ca), for the inspiration. I didn’t copy any of his code, but without the inspiration I would have definitely not made this.

[Check it out](https://owenmoogk.github.io/os)!
