---
title: Spotify API Fun, Design Planning, and a Musical Guessing Game
date: Mar 29, 2024
tags: ["reflection", "tech"]
---

## Spotify API Fun, Design Planning, and a Musical Guessing Game

This week, I had lots of fun getting deeper with some tech, and learned a lot about GitHub commit signing (I just made a whole blog post about that [here](https://medium.com/@owenmoogk/pretending-to-hack-github-and-some-git-security-notes-0ded981eeb37)).

Firstly, I spent a few hours this week working with Spotify and the Spotify API. I have a whole folder of MP3s (about 500 files), from before I got Spotify. And surprisingly, I actually did a pretty good job of organizing them! They were all named with the same convention: song title as the file name, and the artist and genre attached to the file metadata.

I’ve gone back a few times for a nostalgia trip, and knew I wanted to import them into Spotify. However, searching for 500 songs is way too much work, especially when I know how to code in Python.

Without getting too much into the details, I used the [SpotiPy](https://spotipy.readthedocs.io/) package to log into my account and search for all of the songs. Then, I added them all to a playlist and kept a text file for songs that either found a partial match or weren’t found at all. Then, I just had to fix a few small errors, and Voila, all of my songs perfectly imported into Spotify!

Once completed, I also wanted a backup of all this music, so I used the open-source [SpotMyBackup](http://www.spotmybackup.com/) to create a massive JSON file of my entire library, so I don’t have to be worried about losing all that music!

As far as other things on the internet go, I’ve come across [The Jargon File](http://catb.org/jargon/html/), which has some interesting ‘hacker slang’ and funny jokes, for those in software. One that I’ve found funny is [The P-convention](http://catb.org/jargon/html/p-convention.html), a hackish way of asking a predicate/boolean question.

Lastly, I’ve came across [A Better Design Process](https://www.youtube.com/watch?v=gbuWJ48T0bE) by Wintergatan, which really resonates with me. I’ve done a few projects with good planning, and many more without it, and I think he perfectly encapsulates why engineering projects need planning and up front intentionality.

The three big takeaways for me:

* The **Iteration Cycle Length**: **The amount of time it takes to make a change / fix a problem in an iteration cycle. Iteration cycle lengths are very small in the planning, brainstorming, and decision making phase, meaning mistakes aren’t that costly. However, trying to solve the same problems in prototyping or production will be far too expensive, and cause major headaches. This is why planning is important, as you want to be able to figure out as much as possible, and solve the problems before moving forward.

* The **Maximum Virtual Product**: The furthest you can get without starting any work (this is the point at which planning ends and production starts). This could be a cardboard prototype, or a lot of design sketches, however it is a way of describing the plan that contains as much detail as possible, and one on which no more work can be completed until tangible progress is made.

* And a quote to end it off “*Projects don’t go wrong, they start wrong”.*

Phew, that was more than I usually write, however those were both pretty interesting things got my brain thinking this week. Something lighter now:

[Bandle](https://bandle.app/)! This is a Wordle-inspired musical guessing game, where a song is built starting with drums, then a bassline, and so on. I’ve been playing this with my co-workers every morning, and it’s a blast. I’ve only been able to guess the song from only the drums once, but it feels good to get it with only a bassline.

Lastly, the [Wintergatan Marble Machine](https://www.youtube.com/watch?v=IvUU8joBb1Q) never fails to impress me…

Until next week!
Owen
