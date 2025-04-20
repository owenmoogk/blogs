---
title: "Coding Adventures: Making an Awesome Personal Portfolio"
date: 
tags:
  - tech
  - coding_adventures
image: portfolio.png
---
## Coding Adventures: Making an Awesome Personal Portfolio

I’ve been working on my personal website ([https://owenmoogk.github.io](https://owenmoogk.github.io)) for a long time now. Like, more than 5 years (that’s more than 25% of my lifetime!). In doing so, I learned a lot and have gone through many solutions for hosting and organization of files.

Structuring the website has been a really big challenge that I switched solutions for multiple times, as my needs for data storage, pages, flexibility, continuity, and useability have evolved over time.

I wanted to share how I’m organizing and serving my website, and why I think it’s a good solution. If it’s helpful to someone else making a portfolio, that’d be fantastic (and I’d love to have a look, [email me](mailto:owenmoogk@gmail.com)), but if it doesn’t help anyone that’s great too. I need to work on my technical writing anyway 😊.

## Getting Started

I started making my personal website when I was learning website development, so naturally, it was quite garbage. I still keep them live though, sometimes it’s a nice nostalgia trip or even just a reminder of how far I’ve come. All my old websites are archived as [releases on the repository](https://github.com/owenmoogk/owenmoogk.github.io/releases).

As a small timeline, I built websites first using plain HTML and CSS, then added JavaScript to make it a bit *spicier*, and then moved to ReactJS, which is wayyyyy better (I’ll get into why later, don’t worry).

I’ve generally had a few pages on my websites:

* Homepage
* Projects
* Work
* Contact
* Resume
* And more recently: Blog

Some of these are easy to code. A homepage is just a simple (almost static) webpage, a contact page is too. Work, Projects, and a Blog are a bit harder because data sources need to be organized, and flexibility needs to be maintained. So, the question was: how do I build these pages?

## Building a cool project page 😎

These sections detail some solutions I’ve tried, along with what I’m doing right now. So *if* you’re using this as a guide, read the whole thing before making any decisions.

### First Attempt: HTML

V2 of my website was the first with a project portfolio, and I made it using pure HTML. Looking back, it makes me want to barf… but I was naive.

I had a project homepage, with a picture, name, and description for each project:

![](https://cdn-images-1.medium.com/max/3270/1*O89s9T8kCFloM5lkczwxAQ.png)

And each project had it’s details page:

![](https://cdn-images-1.medium.com/max/2458/1*PXjx_pCPBJNLUQhZC20f3Q.png)

The issues with this:

* Every bit of code was repeated… way too many times (each page was just written in plain HTML).

* Content was repeated: If I wanted to change a project name, I had to do it in a bunch of places.

* It was slow to write. When I wanted to make a change to a project, I would have to add the proper divs, headers links, etc. All in all, it took too long to add content.

I stuck with this method until version 4 of my website when I decided to mix it up.

### Attempt 2: XML

Inspired by a friend of mine, I moved to XML to store project data. Not sure if I can give a reason as to why I chose XML, other than “I was stupid”. Nevertheless, I made it work. This was the first time I separated data from page structure, which was a game-changer. This was very important because code can get messy when the actual pages contain data. So, I tucked all my project information into a /assets folder and loaded it with some scrappy XML loading code. And when I say scrappy, I mean it (I guess I hadn’t heard about the Fetch API…):

    function loadProjects() {
        // make new http request, its a js thing
        var xmlhttp = new XMLHttpRequest();
    
        // GET, file location and name, and some other propertie i forget
        xmlhttp.open("GET", "../assets/projects.xml", true);
        xmlhttp.send();
    
        // when there is a change in the request's state, 
        // it'll check all is green and run the table loading function
        xmlhttp.onreadystatechange = function () {
            // all green
            if (this.readyState == 4 && this.status == 200) {
                loadEntries(this);
            }
            // cant find the xml
            if (this.status == 404) {
                console.log("couldn't find the xml file")
            }
        }
    }

This did the trick for loading XML documents, and then I had to render them to the page. Writing this now, I’m so used to React that I almost forgot how annoying this is with pure HTML / JS.

The *official* way to do this is to use DOM techniques. That would go something like…

    let newDiv = document.createElement('div');
    
    newDiv.id = 'myNewDiv'; // Setting an ID
    newDiv.className = 'myClass'; // Setting a class
    newDiv.textContent = 'Hello, World!'; // Setting the text content
    
    document.body.appendChild(newDiv); // Appending to the body element

But this is really tedious, so… innerHTML to the rescue!! (I’m not joking). I built the whole page using HTML strings:

    if (elementType == 'image'){
        txt += '<div class="img"><img src="'+elementData+'" class="img"></div>'
    }
    else if (elementType == 'render'){
        txt += '<div class="render"><img src="'+elementData+'" class="img"></div>'
    }

Because I wasn’t yet using React, I still had different HTML pages for each project. They were smaller, but almost every project page was identical. They all did the same thing: load in metadata, make a body div, and load the project:

    <!DOCTYPE html>
    <html>
        <head>
            <title>Owen Moogk - Projects</title>
            <meta name="author" content="Owen Moogk">
            <meta name="keywords" content="Owen, Moogk, Owenmoogk">
            <meta name="description" content="Just a little bit about me :)">
            <link rel="stylesheet" href="../../../css/navbar.css">
            <link rel="stylesheet" href="../../../css/projects/project-pages.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap">
            <script src="../../../js/navbar.js"></script>
            <script src="../../../js/projects/project-pages.js"></script>
        </head>
        <body>
            <div id="nav"></div>
            <div class="body"></div>
        </body>
        <script>loadMenuItems()</script>
        <script>loadProjectPage('../../../assets/projects/engine.xml')</script>
    </html>

Except for the XML link used as an argument when loading the project page, I had to copy and paste this code for EVERY project. This isn’t a good solution.

Lastly, XML is not fast to write/edit. This is what a title, some images, and a link look like in this XML format. It’s pretty verbose:

![](https://cdn-images-1.medium.com/max/2000/1*mFfNdyEcBujbxeO_Ok4T6Q.png)

So to summarize, this was not a good solution because:

* Projects needed to still have an HTML page (with entirely repeated code)

* My Javascript loading method used HTML strings (*horrible* practice)

* XML is slow to write and edit.

What’s better than XML…?

### A good solution: JSON!

JSON is XML, except better (at least for this use case). In converting my project files to JSON, I even made a [conversion website](https://owenmoogk.github.io/xml-json-convertor/)!

JSON is better for this application because it doesn’t require opening and closing tags, so data can be much cleaner. Also, it can be loaded into a JavaScript Object fairly easily (after all, it is JavaScript Object Notation).

It turned that previous mess of tags into this:

![](https://cdn-images-1.medium.com/max/2000/1*8XNY70qdPJ69VMPuQCIrdA.png)

All of the structuring tags were replaced by brackets, allowing them to be parsed and implemented easily. This coincided with my switch to ReactJS and allowed me to create one project page, which loaded data for whatever project was requested. This enabled me to delete A LOT of HTML code, that was repeated all over, in favor of a singular component. This is why React is better.

And that was it! It worked well, and was a fairly scalable solution! When I wanted to make a new project, I added it to the directory (just a list of strings of projects), and made its JSON file…

### A good solution, Part 2: Markdown

Except I really hated making JSON files. I still had to get the structure right, I needed a whole bunch of brackets everywhere, and it was getting annoying. I finally decided to switch to using Markdown. If you’re unfamiliar, this is what GitHub uses in its README files, and can nicely render text as HTML from the markdown file. I decided to do the same, so I moved all the content over.
>  Note: I wanted all of the content to be kept in the markdown files, however I kept the metadata for each project in it’s JSON file. This is beacuse its more easily parsable, and has a set data structure. This enables features like search, sort, external links, and a boolean featured field.

The next step was rendering this markdown file. Turns out, there is a plugin called [Showdown](https://www.npmjs.com/package/react-showdown) that renders markdown files, so it was actually quite simple. I just had to render the component, and pass its related markdown!

I put that code snippet below (for the full code check [my GitHub](http://github.com/owenmoogk)), and notice how I have to parse the markdown before loading it. This is so links are properly formatted (for images, videos, and hyperlinks), and point to the right directory. Otherwise, they would point to something that doesn’t exist. Although not strictly necessary (links could be typed in a more verbose manner), it means in the markdown file I can do something like `![Image](render1.png)` to load an image, and the parseMarkdown function will do the rest.

    function parseMarkdown(data: string) {
    
      if (!data) return "";
    
      // this replaces the image paths to point to the proper project directory
      // https://stackoverflow.com/questions/52852425/change-image-source-in-markdown-text-using-node-js
      // it's called a 'capture group' in regex
      // however, it doesn't match anything with https:// because that means it's an external link
      // also, it doesn't match anything that starts with a slash, because that means it wants the root directory (eg "contact me" is /contact, and not the project dir)
      data = data.replaceAll(/\]\((?!https?:\/\/)(?!\/)(.+?)(?=(.+))/g, `](${process.env.PUBLIC_URL}/assets/projects/${name}/$1`)
    
      // replace the src on video tags
      data = data.replaceAll(/<video src=("|')(.+?)\1><\/video>/g, `<video src=\"${process.env.PUBLIC_URL}/assets/projects/${name}/$2\" controls></video>`);
    
      return (data)
     }
    
    // the actual markdown component
    <MarkdownView
          markdown={parseMarkdown(projectData ?? "")}
          options={{ tables: true, emoji: true }}
    />

Lastly, I load the metadata from the JSON file:

    {
        "title": "Hydraulic Arm",
        "date": "May 31, 2018",
        "types": [
            "Solidworks"
        ],
        "description": "Hydraulic powered arm, with 3D printed claw.",
        "featured": true
    }

    <div className="title">
         {metaData.title}
    </div>
    <p className='subtitle'>{metaData.date}</p>

And, it looks pretty good! You can see at the top the metadata being loaded, and below is the markdown content.

![](https://cdn-images-1.medium.com/max/2000/1*0SUzK5qeCuHyZj7V6jfQxQ.png)

![](https://cdn-images-1.medium.com/max/2000/1*DpE6yrxYrBdW8nwWAGsHUg.png)

One more thing. Since I’m a nerd, sometimes I make 3D renders. And *sometimes*, I layer them on top of each other so they’re interactive, like this:

![](https://cdn-images-1.medium.com/max/2000/1*vNNs4NOxXjlGIX8U4e2dmw.png)

I want to keep this feature, however this can’t be done in markdown. Luckily, Showdown has a feature for this. I mapped the H4 onto a custom component, so I could input something like this: #### overlay1.png,overlay2.png , and wrote a custom handle so the website would load the image overlay renderer. It looks like this:

    <MarkdownView
          markdown={parseMarkdown(projectData ?? "")}
          options={{ tables: true, emoji: true }}
          components={{
           h4(props) {
            console.log(props.children[0].split(","))
            var [image1, image2] = props.children[0].split(",")
            return (
             <div className='sliderContainer'>
              <ReactCompareImage 
               leftImage={"/assets/projects/" + name + "/" + image1} 
               rightImage={"/assets/projects/" + name + "/" + image2} 
               aspectRatio='taller' 
               handle={
                <button style={{
                 height: '50px',
                 outline: 'none',
                 width: '10px',
                 border: 'none',
                 borderRadius: '5px',
                }}></button>
              } />
              <span className='subtitle'>Move the slider to see inside.</span>
             </div>
            )
           }
          }}
         />

This tells it that when it sees an H4, it will pass it to my custom handler, which will render the ReactCompareImage component instead of a regular H4. This way, I maintain my custom functionality while not having to make a custom parser, or use JSON!
> # “Great success!!” — Borat

Phew, that was a lot. It’s a bit all over the place, but that was the journey I followed. To recap, my ‘optimal’ (at least so far) project page flow is as follows:

* Project metadata stored in JSON

* Project content stored in markdown

* Project directory, just a list of all of the projects (JSON)

* React, using the ShowdownJS to render, and a custom handler for the H4, which allows for custom component rendering.

Why this is optimal (for me):

* Adding a project is super easy (add to directory, make metadata, write content)

* It’s flexible. Everywhere that I need projects ( /projects , /projectDirectory , /project/[projectName] ), the data is fully accessible. Since it’s all available at https://owenmoogk.github.io/assets/projects , even other projects that I have made can use this data, on different websites and domains.

* Pages are dynamic. I can change the featured flag on a project, and it changes where it loads on the website. Similarly, I can change the date or tech used, and the searching features respond to that.

* When making a project, I really need to do the bare minimum. My goal was to ONLY be adding content (and not boilerplate code), which is almost fully true (the only exceptions to this are adding to the directory, and a few JSON brackets in the metadata, however, this is acceptable for me).

### GitHub Integration

The last point I want to touch on, and why I think organizing projects this way is optimal, are the associated integrations that come along with it. Most of my projects have GitHub repos associated with them. So, by default, I add a link to the GitHub repo, with a flag to add a custom one or turn it off in the metadata. This way, if I make a project called f1-stats , the website *automatically *links to a GitHub repo called /f1-stats . One needs to ensure a project has the same handle on the website as it does on GitHub, however, if this isn’t the case it’s very simple to add an override for a custom link.

Similarly, if a project has an associated website, it can be turned on via a flag (no URL required). Since all of the GitHub pages are hosted at [myDomain]/[projectName] , this flag can add a button to automatically link to the website.

So, a project like my F1 Stats project will have a GitHub link and an external website link generated automatically on the project page, only by modifying one flag in the metadata:

![Notice the “Github” and “External Link” buttons.](https://cdn-images-1.medium.com/max/2000/1*lszy1hY4uP9yFXt36MXZFQ.png)

Ok, that’s all I have to say for projects. It’s a lot, but definitely the most complex part of the website, that has also gone through the most iterations.

## A Work Page, that isn’t tedious to update.

I think everyone will be happy, that I have less to say for this section! Still a few useful bits though.

For reference, I treat my work page similar to my resume. It’s a bit more through and verbose, but with largely the same content. Jobs, volunteering experiences, extracurriculars, etc.

Like with the projects, I started the work page with pure HTML, then XML, moving to JSON. However, I found a different workflow that I like much more than JSON… and it’s not what you would expect.

### The issue with JSON

I actually don’t have that much of an issue with JSON in this regard. I don’t typically include any media in my work descriptors (unlike with projects), and I’m not adding experiences often enough that the structure of JSON is the annoyance.

The true reason I don’t like storing my work data in a JSON file is that I don’t want to store it in any file! I already write about work on my resume, on my LinkedIn, on my GitHub, and now on my website too?! It’s too much.

### My Ideal Solution

If I could pick a perfect way to do this, it would be as follows: Have a master copy of all ‘blurbs’ for all experiences. From there, everywhere could reference these blurbs, and choose where to use each. If you wanted a different blurb for the same experiences, you could have an alternate version (where you select which version you want in each scenario).

The workflow would look something like this: I get a new job. I write about the new job in my master document/app/website/whatever. I say, “I want this job on my LinkedIn, GitHub, resume, and website”. I hit ‘go’. That’s it.

This is very similar to components in React, or pointers in C++. My LinkedIn will just point to this master document, and when I update the master it will automatically update. If I want a slightly different blurb on my LinkedIn than my resume, I can just say “Make a modification of this”, and it will inherit from the previous. From there, modifications can be made that only show up on the desired platform.

Why is this unfeasible? Many reasons. Most involve companies not playing nice (not like they should, it’s an unreasonable expectation. However it doesn’t make me want it less). I build my resume in Microsoft Word, which is clunky (at best) at retrieving outside data. And further, LinkedIn and GitHub have paid APIs, which would be quite messy to work with. For now, this remains a dream…

### My not-ideal-but-not-so-bad solution

Ok, some of the above requirements are harsh. I don’t write almost anything on my GitHub, it's usually just an oneliner on my homepage README. Also, my resume is usually quite tailored anyway. The two times a year I update it or make changes, it’s probably acceptable for me to copy and paste from somewhere else. After all, if I have a job it doesn’t really need to be up to date (it would be nice… but I can sacrifice this). Also, a resume had additional space requirements, and different types of writing (usually in past tense, third person), so I would have to modify a lot of the ‘blurbs’ anyways.

This leaves LinkedIn and my website. I want them both to be almost identical and not have to modify them twice. Pushing content to LinkedIn automatically is very hard, so I’ll have to make the changes on LinkedIn, and then find a way to get them into my website.

Turns out, there’s a way to do that! [joshuatz](https://github.com/joshuatz) made a [LinkedIn to JSON Chrome extension](https://chromewebstore.google.com/detail/json-resume-exporter/caobgmmcpklomkcckaenhjlokpmfbdec)! This automatically downloads the entirety of one’s LinkedIn to a JSON file, to be used wherever! This means, that I can update my LinkedIn, download it, and then just chuck the file into the assets folder of my website, and my website is updated! Not bad!

![Joshua Tzucker’s Conversion Tool](https://cdn-images-1.medium.com/max/2560/0*FW4_ck91ueJZ3azR)

There’s some code to put the data into React components, it’s not hard. If you want you can find it on [my GitHub](http://github.com/owenmoogk).

## Blogging: Why not.

I’ve started to write blogs in Medium, which has been fantastic. It’s a good way to be intentional… about whatever I end up discussing. I have been usually talking about music, engineering, learning, and life experiences. It’s led to me listening more intently to my music, being more thoughful about my designs, learning more in social situations, and being more intentional about life choices. Highly recommend it, even if you’re writing for nobody.

But, I kind of don’t like my blogs being stored on Medium. It’s ironic, because that’s the platform that I’m using right now to edit this blog… but it’s true. Self-hosting is almost always the way to go, if it’s at all possible. I wanted to be able to add features that Medium didn’t support, such as sorting/categorizing my posts for an audience (kind of like on SubStack, Joss’s [Boxx](https://boxx.substack.com/) is a good example of what I was going for). But of course… I wanted this to be integrated seamlessly into my website. I consided using a well-placed/styled iframe, but I know that can get messy from experience. It’s a good thing that a blog is basically….

### Markdown!

Instead of using Medium as an external provider (meaning that my content isn’t really *controlled* by me), I could use markdown to write and post my blogs on my website. I’ve already played with using markdown files for projects, so this was pretty simple to implement. I had to scrape all of my blogs off of Medium, and turn them into markdown, and then integrate it into my site! This way, everything was owned by me (running on a GitHub pages site)!

I structured this a bit differently than you might expect. Since I wasn’t (and am still not) 100% committed to this being a subpage of my personal website, I wanted to have a bit of seperation. Also, I didn’t want blog posts to show up in my commit history of my personal website. Some “seperation of church and state” was in order.

I created a seperate repository for my blogs, which I kept private. However, it’s currently up on GitHub pages. Something about this service that few people know about… is that you can use it for simple static file serving. After all… that’s really what a website is anyways. So, you can go to the url of the pages website and pull JSON files (you don’t need a frontend!).

Taking advantage of this, I in essence setup a “blogs API”; a collection of blog posts accessible (in raw file format) in a repository, along with a GitHub workflow to autogenerate metadata for each blog. All of this is accessible over HTTP!

My website knows about these endpoints, so I just hit them whenever I need to load the blog posts for a user… and ta-da! A blog page complete!
>  A sidenote on GitHub’s business model: How they can stay afloat while providing these free services is beyond me (even now as a branch of Microsoft). I am endlessly appreciative because it alone has enabled my journey into learning programming and web development, however there’s not a single other service that exists, with the amount of freedom in a free plan.
>  This isn’t the first time a company had to scale down it’s free option. Twitter and Yahoo API’s were publically availible previously, and not even [rate limited](https://www.youtube.com/watch?v=BxV14h0kFs0).
>  However, those days came to an end. As more people started using the internet, free compute became a luxury that companies couldn’t afford to give away for free. The “wild west” of the internet was over. We shifted from the age of unlimited API requests to that of paid-for compute credits.
>  And GitHub still stands; offering unlimited repositories, free hosting, workflow runs… the whole 9 yards. All that to say: I’m impressed and grateful.

## More to Come!

I’m nowhere near done this website, and I don’t see a day where I am. There’s always new ideas floating around in my head, largely inspired by my friends, co-workers, and the occasional YouTube video or blog post.

My notebooks are filled with new ideas for more things to share, interactive UI ideas, and page designs. I’ll come back and update this, or link to another post, for anything substantial (especially if I had to solve a problem that was both hard *and* new).

One idea I had is a self-hosted VSCO, since traditional social media has always rubbed me the wrong way (it’s actually live right now, but only to those who know the URL from stalking me on GitHub😊). This is just a little bit for me to share what I’ve been up to.

Another idea that I’ve had is to to add a travel page. I’m not going to become a travel blogger (at least I hope not 😋), but the ability for a new place to inspire and teach has had a profound and unexpected impact on myself and my world views, so I’d like a way to share it.

But… those are all of the goals, problems, and solutions I worked through when building this. It might be similar for you… or it might be completely different. Either way: time to get coding!

![](https://cdn-images-1.medium.com/max/2000/0*NIp5waNg9oZcB4yF.gif)

## Bonus: Personal Improvements

I don’t think many people will read this (let alone make it this far), but if you have and are thinking… “this is complex, I can’t do this”: I’ve been there. As I previously mentioned, there were a lot of designs and tech stacks I tried before I settled on something nice.

As some motivation (and a *little flex* of how far I’ve come), here are some images of terrible designs of previous websites).

![Version 1 Homepage (what a header🤦‍♂️)](https://cdn-images-1.medium.com/max/3786/1*SY_RgCaFRhXUXK649gTLxA.png)

![Version 3 Project Page (not sure what I was thinking with a background on the navbar 😅)](https://cdn-images-1.medium.com/max/3744/1*q_kGmxO1a9IAdkfG0oEtAA.png)

![Version 4 projects page (it’s actually not terrible… but doesn’t fit the vibe)](https://cdn-images-1.medium.com/max/3802/1*ReR1GU8SQhRJtqJ5pTd5DQ.png)

![Version 4 contact page (in fairness… it was more colorful!)](https://cdn-images-1.medium.com/max/2346/1*ynZ9L67WBCJcWideTZ1NBg.png)

![Version 5 Project Page (the colors are determined based on the tech stack… something I’m actually considering re-implementing)](https://cdn-images-1.medium.com/max/3800/1*JYSuB0vfaxS1l-gGwhpTuw.png)

So… varying degress of success. But, it’s about the journey, learning, and experience. That’s 8 website versions down, so here’s to the next 8 versions!
