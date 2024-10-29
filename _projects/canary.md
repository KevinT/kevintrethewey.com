---
layout: project
title: Chaos Canary
date: 21 Sep 2017
screenshot:
  src: /assets/img/projects/canary@0,25x.jpg
  srcset:
    1920w: /assets/img/projects/canary.jpg
    960w: /assets/img/projects/canary@0,5x.jpg
    480w: /assets/img/projects/canary@0,25x.jpg
caption: Gives you confidence that your team's environment is healthy and reminds you what to do about it as soon as it isn't.
description: >
  Chaos Canary was a simple to use wiki-based tool for teams to track what they know about their digital environments, and keep an eye on the real-time health of anything that they depend on to get their work done or keep their customers happy.
---

__Note: This project is currently on hold. I still believe in it, but don't have the resources to expand further on the product right now. One day!__

**Canary** was a wiki-based system where you captured information on running infra, services and applications that your team owned or depended on. The tool then created a "Canary" associated with that item. When the Canary [found life challenging](https://en.wiktionary.org/wiki/canary_in_a_coal_mine), all the information you captured on why you care about that item, what was done in the past if there were issues, along with other history and guidance was readily available for the team to take the actions needed to save the bird.

The seed for Canary was planted when we were building software as a set of teams in a South African bank. The system we were building extracted data from around seventy different source systems and provided analysis to decision makers. If any one of those source systems was unstable our customers saw it as our failure. To thrive in this environment we needed to keep track of all the things we cared about, the state we expected them to be in, and what to do when they went down or flaked out so that responses were proactive and effective.

The purpose built tool was evolved and production hardened in this very demanding environment - it didn't have to be pretty, it had to work.

In 2016, the client for which we evolved the tool made an open source cut of the codebase, which we took and spent considerable thought and effort making it a product that is friendly for any team to install and use, even if they aren't technically inclined.

After Driven closed its doors the project was put on hold.
