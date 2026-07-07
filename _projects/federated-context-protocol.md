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
  FCP (Federated Context Protocol) lets a person, or an AI agent acting for them, reason over every context they hold - work, family, mentorship, friendships - while guaranteeing that each audience only ever sees the slice meant for it.
links:
  - title: GitHub
    url: https://github.com/KevinT/federatedcontextprotocol
---

You're many things at once - an employee, a parent, a mentor, a friend - and each of those contexts needs its own way of thinking and its own boundary. Pour everything into one shared place and it leaks: your employer shouldn't see your private journal, your friends shouldn't sit inside your family's logistics. But you still want an intelligent system that can reason over as much of your context as possible.

[FCP][github-fcp] resolves that with a simple structural rule:

- **Knowledge lives in version-controlled repos.** Sharing happens at the repo boundary - many small repos, each scoped to exactly one audience.
- **Reasoning happens at the workspace boundary.** An agent mounts several repos at once and reasons over their union, with nothing leaking between audiences.
- **The shape is hub-and-spoke.** A private *root* you never share, collaborative *domain* repos for each long-running context, and *constituent* repos beneath them - some yours, some shared.
- **Crossing is one-way and deliberate.** Context only ever crosses a boundary as a published projection, never by reference.
- **Every part carries provenance.** A curation marker says whether it's actively stewarded, a proxy, inferred, or unowned.

The boundary is only half the job - what lives inside each context unit is meant to be an ontology map, not a data dump: the mental models, relationships and skills needed to reason about that context, each with its own curation marker. FCP is deliberately silent on how the raw ingestion, entity extraction, or answer synthesis happens underneath that map; it's a substrate for boundaries and provenance, not a brain.

That's intentional, and it's meant to be complementary to, not competing with, tools like [GBrain][gbrain], which build a self-wiring knowledge graph and do synthesis and gap analysis over a body of ingested data:

- **GBrain is a natural fit *inside* a single FCP context unit** - doing the ingestion, entity extraction and graph-building it's good at.
- **FCP does the thing GBrain's shared-brain-scoped-by-login model doesn't attempt** - keeping reasoning genuinely isolated per audience, as separate context units, rather than access-controlled rows inside one shared store.

Each patches a hole the other leaves open.

I'm designing FCP after running into the limits of a single personal folder bolted onto an employer's context and data systems - which hard-coded one orientation and physically co-locates content that belongs to mismatched audiences. 

[v0.1 is out now][github-fcp], specified as a set of tool-agnostic principles plus a canonical implementation (git repos, event-sourced context streams, folded views) that adopters can implement however suits them, and versioned like any other protocol via semantic versioning and decision records.

[github-fcp]: https://github.com/KevinT/federatedcontextprotocol
[gbrain]: https://github.com/garrytan/gbrain