---
layout: project
title: Federated Context Protocol
date: 30 Jun 2026
screenshot:
  src: /assets/img/projects/fcp@0,25x.jpg
  srcset:
    1920w: /assets/img/projects/fcp.jpg
    960w: /assets/img/projects/fcp@0,5x.jpg
    480w: /assets/img/projects/fcp@0,25x.jpg
caption: A protocol for reasoning across all of your context while sharing only what each audience should see.
description: >
  FCP (Federated Context Protocol) lets a person, or an AI agent acting for them, reason over every context they hold — work, family, mentorship, friendships — while guaranteeing that each audience only ever sees the slice meant for it.
links:
  - title: GitHub
    url: https://github.com/KevinT/federatedcontextprotocol
---

You're many things at once — an employee, a parent, a mentor, a friend — and each of those contexts needs its own way of thinking and its own boundary. Pour everything into one shared place and it leaks: your employer shouldn't see your private journal, your friends shouldn't sit inside your family's logistics. But you still want an intelligent system that can reason over as much of your context as possible.

FCP resolves that with a simple structural rule: knowledge lives in version-controlled repos, sharing happens at the repo boundary, and reasoning happens at the workspace boundary — an agent mounts several repos at once and reasons over their union, with nothing leaking between audiences. The result is a hub-and-spoke federation: a private *root* you never share, collaborative *domain* repos for each long-running context, and *constituent* repos beneath them, some yours and some shared. Context only ever crosses a boundary as a deliberately published projection, never by reference, and every part of the map carries provenance — whether it's actively stewarded, a proxy, inferred, or unowned.

I designed FCP after running into the limits of a single personal folder bolted onto an employer's repository — it hard-codes one orientation and physically co-locates content that belongs to mismatched audiences. v0.1 is out now, specified as a set of tool-agnostic principles plus a canonical implementation (git repos, event-sourced context streams, folded views) that adopters can implement however suits them, and versioned like any other protocol via semantic versioning and decision records.
