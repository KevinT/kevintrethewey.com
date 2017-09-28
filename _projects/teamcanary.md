---
layout: project
title: Team Canary
date: 21 Sep 2017
screenshot:
  src: /assets/img/projects/teamcanary@0,25x.jpg
  srcset:
    1920w: /assets/img/projects/teamcanary.jpg
    960w: /assets/img/projects/teamcanary@0,5x.jpg
    480w: /assets/img/projects/teamcanary@0,25x.jpg
caption: Gives you confidence that your team's environment is healthy and tells you what to do about it as soon as they aren't.
description: >
  TeamCanary is a simple to use wiki-based tool for teams to track what they know about their digital environments, and keep an eye on the real-time health of anything that they depend on to get their work done or keep their customers happy.
links:
  - title: Homepage
    url: http://teamcanary.io
---

I planted the seed for [TeamCanary][canary] when I was building software as a consultant in a team in a bank. The team was extracting data from around seventy different source systems and providing analysis to internal customers in the bank. If any one of those source systems was unstable our customers saw it as our failure. To thrive in this environment we needed to keep track of all the things we cared about, the state we expected them to be in, and what to do when they went down or flaked out.

The tool was evolved and production hardened in this very demanding environment, but not much focus was put on making it pretty, it just had to work.

A year or so ago, the client we evolved the tool made an open source cut of the codebase, which we took and have spent considerable thought and effort making it a product that is friendly for any team to install and use, even if they aren't technically inclined.

[TeamCanary][canary] it is a wiki-based system where you capture information on the item you care about. It could be a server, a process on a server, a web service, data in any kind of data store or file system - with easy pluggability to add new ones. The tool then creates a Canary to keep track of that item. When the Canary bites the big one the tool hands you back all the information you captured on why you care about that thing, what your past self thought you should do about it, along with a whole lot of useful history for it.

[canary]: http://teamcanary.io
