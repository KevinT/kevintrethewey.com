---
layout: post
title: "Time, Truth, and Ontology: The Three Axes Your Knowledge System Is Probably Missing Two Of, and that's why it's broken."
date: 2026-03-05
categories: professional
tags: [knowledge-management, organisational-design, software-development, agentic-ai]
description: "Most teams, intentionally or by default, digitally record their knowledge along a single axis - usually time (slack, emails etc). Real knowledge leverage (human and agentic!) comes from using all three axes deliberately and connecting information across them."
image: /assets/img/blog/knowledge-axes.jpg
---

Why most teams, and organisations, can't find anything in their own tools - and why the answer isn't a "better" tool, but a better understanding of what knowledge actually needs from its structure.

## The Problem is Structural, Not Technical

Why is it so hard to find things in Slack? Why does Notion inevitably bloat into a graveyard of half-maintained pages?

It's tempting to blame the tools. But most of the time, the real issue is that we're collapsing fundamentally different kinds of information into a single organising strategy - usually whatever the tool defaults to.

Information that is organised by content and cross-linked into a wider web becomes easier to understand and more discoverable. Other people - or agents - can refine it, contribute to it, or link to it from elsewhere. It grows and enriches over time.

The key insight is this: **there are three natural axes for organising knowledge - time, truth, and ontology - and most teams collapse everything onto just one of them.** The power isn't in choosing between the three. It's in using all three deliberately, for the right kinds of information, and then *connecting across them*.

A decision log (time) should link to the architectural principle it invoked (ontology) and update the system configuration it changed (truth). A team roster (truth) should reference the meeting where the restructure was agreed (time) and connect to the domain concepts that team owns (ontology). When these axes work in isolation, each one eventually fails in predictable ways. When they're connected, they reinforce each other and the whole system becomes more than the sum of its parts.

## The Three Axes (And How Each One Fails Alone)

Each axis has a natural domain where it's the right primary organiser. But each also has a characteristic failure mode - one that is largely *solved by connecting to the other two*.

### 1. Point in TIME

Use this when it matters **when something happened**.

Meeting notes. Chat transcripts. Decision logs. Incident timelines. Who said what, and when.

* **The promise:** A well-structured timeline lets you reconstruct events, track decisions, and maintain accountability. You can always go back and see what was said, when it was said, and by whom - providing clarity and historical context when making decisions.

* **The pitfall:** Time is a never-ending conveyor belt. Information on the belt gets lost as more arrives. It becomes progressively harder to search for, and nearly impossible to discover what the "current truth" is for any given question. You end up re-reading weeks of Slack threads to find the one message that matters.

* **The connection:** Time-based records become far more useful when they link outward. A meeting note that updates a truth record ("we changed the API owner to Team X") and references an ontology entry ("see: API Governance Principles") transforms from a forgettable chat log into a node in a living system. The time record provides provenance; the other axes provide meaning.

### 2. Current TRUTH

Use this when the content represents **the current state of something**.

People profiles. Team compositions. System configurations. Active contracts. Architectural decisions in force.

* **The promise:** A single source of truth ensures alignment across teams, reducing duplication and inconsistencies. When properly maintained, it provides an authoritative and up-to-date reference-making it easy to access accurate information without second-guessing its validity.

* **The pitfall:** As content grows, it becomes progressively harder to know where the single point of truth lives for any given fact. Different systems might disagree about what the truth is, or represent it from different perspectives. Without active curation, truth-oriented systems decay into a collection of confidently wrong pages that nobody trusts.

* **The connection:** Truth records gain credibility and context when they link to their history (time) and their domain (ontology). A team roster that shows *when* it was last updated, *which decision* changed it, and *what domain* that team is responsible for is infinitely more trustworthy than a standalone page that might be six months stale. Time gives truth a lineage. Ontology gives truth a reason to exist.

### 3. Knowledge ONTOLOGY

Use this when information needs to be **connected into a rich web** of related concepts.

Glossaries. Domain models. "What is a PSR?" type questions. Architectural principles. Design patterns and their relationships to each other.

* **The promise:** A well-connected knowledge system fosters deep understanding and discovery. By linking related concepts and providing context, it accelerates learning, enables informed decision-making, and allows knowledge to evolve organically as new insights emerge.

* **The pitfall:** As the knowledge base expands, it can become overwhelming and difficult to navigate. Without clear structure or active curation, connections become tangled - leading to redundancy, outdated information, and contradictions. A poorly maintained ontology devolves into an unmanageable sprawl, making it just as hard to find what you need as if nothing had been recorded at all.

* **The connection:** An ontology that links to current truth records and time-stamped decisions stays grounded. The concept of "API Governance" becomes actionable when it connects to the current API owners (truth) and the decisions that shaped the policy (time). Without those links, ontology drifts into abstraction - a beautifully structured map of a territory that no longer exists.

## A common anti-pattern: Folder/File Thinking

There's a fourth pattern that deserves attention, not because it's a good organising axis, but because it's the one many people have been pattern-entrained into thinking with: **hierarchical folder structures**.

Folders feel intuitive because they mirror physical filing cabinets. But they impose a rigid ontology (!) that breaks down almost immediately in practice. Where does a document about a client's technical architecture go-under the client folder, the architecture folder, or the project folder? The moment you have to choose one location for something that belongs in multiple contexts, you've created a discoverability problem.

Folder structures force single-inheritance thinking onto information that is inherently multi-dimensional. They work for personal file storage where one person's mental model is the only one that matters. They fail at organisational scale, where multiple people with different mental models need to find the same things.

The pathology is predictable: people create shortcuts, duplicates, and "see also" files. The structure becomes a fiction maintained by convention rather than utility. Eventually, everyone just uses search-which means the folder hierarchy was doing nothing useful in the first place.

## Why This Matters More in the Age of Agents

If you've been following my recent thinking on [agentic AI and organisational design](/blog/professional/2025-03-21-2-agentic-ai-challenges-to-traditional-org-design/), you'll recognise why this connected, multi-axis approach matters more than ever.

Autonomous agents need to find, understand, and act on information. They can't tap a colleague on the shoulder and ask "where did we put that decision about the API migration?" They need information to be discoverable without ambient human context, unambiguous about whether it represents current truth or historical record, and connected to related concepts so they can reason about implications.

Here's the critical point: **an agent's ability to reason effectively is directly proportional to how well your knowledge axes are connected.** An agent operating against a time-organised Slack history will drown in noise. An agent operating against isolated truth pages won't understand *why* things are the way they are. But an agent operating against a connected system-where truth records link to their decision history and anchor into a domain ontology-can trace reasoning chains, verify currency, and make contextual decisions.

This means your knowledge management strategy isn't just an internal productivity concern anymore. It's becoming **infrastructure for autonomous work**. The organisations that build well-connected knowledge systems will have agents that can operate with meaningful autonomy. Those that dump everything into a single time-ordered stream will find their agents are only as good as the disorganised knowledge they're built on top of.

## The Connective Tissue

Understanding the three axes individually is necessary but not sufficient. The real leverage comes from the links *between* them. Think of it as a triangle where each edge represents a different kind of connection:

* **Time → Truth:** Every time-based event that changes the current state of something should update-or at least link to-the relevant truth record. "We decided in Tuesday's architecture review to deprecate Service X" should result in the Service X truth page reflecting that deprecation, with a link back to the decision.

* **Truth → Ontology:** Every truth record should be anchored in the ontology. A team roster entry doesn't just say who's on the team-it links to the domain concepts that team owns. A system configuration page links to the architectural patterns it implements.

* **Ontology → Time:** Concepts in the ontology should link to their history. When did we adopt this pattern? What decisions led to this principle? This gives newcomers (human or agent) the ability to understand not just *what* the current knowledge is, but *why* it's that way.

When all three edges of this triangle are maintained, you get something qualitatively different from any single axis alone: a knowledge system that is simultaneously navigable, trustworthy, and historically grounded. Each piece of information has context, currency, and connections. That's the difference between a knowledge base and a knowledge *system*.

## Practical Heuristics

Each piece of information should have a **primary** axis-the one that determines where it lives and how it's structured:

**Primary axis is time** when the sequence matters more than the current state. Audit trails. Communication records. Incident response logs. Decision journals.

**Primary axis is truth** when people (or agents) will ask "what is X right now?" Team rosters. System ownership. Active architectural decisions. Configuration.

**Primary axis is ontology** when the relationships between concepts matter more than any single fact. Domain knowledge. Organisational playbooks. Design principles and their trade-offs.

But regardless of which axis is primary, **always ask: what should this link to on the other two axes?** That question-more than any tool selection or taxonomy design-is what separates knowledge management that compounds from knowledge management that decays.

## Moving Forward

The next time you're setting up a new Notion workspace, choosing how to structure your Confluence, or designing the knowledge layer that your agent fleet will operate against - don't just ask "what is the primary organising axis here?" Ask the harder question: **how will information on this axis connect to the other two?**

The tools don't matter nearly as much as the strategy behind how you use them (see [Spine Model](https://spine.wetware.works/)!). A Notion page with the right links is worth more than a perfectly categorised folder tree. A Slack thread that updates a truth record and references a concept is worth more than a thousand unlinked messages.

Information architecture isn't glamorous work. But in a world where both humans and agents need to find, understand, and act on shared knowledge, the organisations that connect their knowledge across all three axes - time, truth, and ontology - will find that their information compounds rather than decays. And that might be the most leveraged investment you can make.
