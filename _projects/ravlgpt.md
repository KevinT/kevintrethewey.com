---
layout: project
title: RavlGPT
date: 19 Sep 2025
screenshot:
  src: /assets/img/projects/ravlgpt@0,25x.jpg
  srcset:
    1920w: /assets/img/projects/ravlgpt.jpg
    960w: /assets/img/projects/ravlgpt@0,5x.jpg
    480w: /assets/img/projects/ravlgpt@0,25x.jpg
caption: An AI-native framework for autonomous agentic loops that learn and improve with every iteration.
description: >
  RavlGPT is an open-source framework for building agent loops around RAVL (Reflect-Act-Verify-Learn), a four-phase protocol for agents that diagnose their own failures and get measurably better at a task each time they run it.
links:
  - title: GitHub
    url: https://github.com/KevinT/RavlGPT
---

**RAVL (Reflect-Act-Verify-Learn)** is a pattern I designed for agent loops that need to do more than answer a single prompt well: an agent reflects on what it currently believes about a problem, acts by generating and executing code or tool calls, verifies the outcome against hard checks rather than its own say-so, and learns by updating its assumptions for the next pass. It's a minimal strange-loop structure that keeps running until improvement drops below a threshold or the budget runs out.

[RavlGPT][github-repo] is a framework that implements the protocol. It handles the infrastructure every agent loop tends to need — LLM provider fallbacks, dependency management, prompt-token normalisation, health-check diagnostics — so that a loop's own code can stay focused on the domain problem it's solving rather than on plumbing. One feature I'm particularly happy with is self-healing data ingestion: loops that call flaky or unfamiliar APIs classify failures semantically (auth, schema, rate limit, pagination, and so on), record what they learned, and regenerate their own code on the next attempt instead of just falling over.

I first wrote about the underlying idea in [Agents, Paradigms and Strange Loops][agents-post], and have since built it out into a proper framework, released [here][github-repo] under the MPL-2.0 license.

[agents-post]: /blog/professional/2025-09-19-agents/
[github-repo]: https://github.com/KevinT/RavlGPT