---
layout: post
title: An Engineering Leaders Guide to Recalibrating for the Agentic Era
tags: [AI, leadership, software teams, future of work]
comments: true
description: >
  As experienced engineering leaders, we need to recalibrate our understanding of how software will be built in the age of AI. Here's my current perspective on where to start and what to recalibrate. Subject to change as the landscape shifts underneath us.
---

After 25+ years in software engineering and leading global teams across platforms and industries, I’ve seen multiple waves of technological change. But the emergence of agentic AI—systems that *act*, not just assist—represents a shift more profound than anything prior. It’s not just an evolution in tooling. It’s a transformation in how software is created, operated, and evolved.

This post is a checkpoint for myself—and a guide for others who’ve spent years building mature, human-centered engineering teams. If you already know how to lead teams that deliver, now’s the time to recalibrate. The ground is shifting quickly.

We need you.

## What’s Changing?

| Traditional Software Thinking           | Agentic Software Thinking                                |
|----------------------------------------|-----------------------------------------------------------|
| Code is written line-by-line           | Code is described, delegated, and evolved by agents       |
| Tools support engineers                | Agents are collaborators                                  |
| Architecture is defined up front       | Architecture is shaped with agents over time              |
| Developer productivity is key          | System-level throughput is key                            |
| Expertise drives quality               | Context curation enables quality                          |
| Engineers act in prod with guardrails  | Agents act in prod, sometimes unpredictably               |
| Deep specialization prized             | Synthesis, integration, and orchestration valued          |

If we think of agentic tools merely as faster ways to write software, we’re falling into “faster horses” thinking. The shift isn't just about building the same systems faster—it's about *different forms* of systems, made and operated in fundamentally new ways.

The rise of agentic AI tooling is more than a wave of productivity hacks or code co-pilots. It’s a **fundamental shift in how we conceptualize software creation, collaboration, and execution**. And if you haven’t been hands-on with these tools yet, you're not just missing out—you may be planning for a world that's already disappearing.

Agentic systems don’t just assist—they *act*. They operate across tools, interpret context, pursue goals, and make decisions—sometimes intelligent, sometimes deeply flawed. Crucially, these agents run *in the real world*, not just in test environments or behind review gates. They update data, trigger deployments, reconfigure infrastructure, and take domain-specific actions that no one explicitly coded line-by-line.

So if you’re still thinking in terms of "tools that support engineers," it’s time to shift to "systems that *are* engineers." That requires a recalibration of long-held beliefs.

## Start with Your Existing Mental Models

If you're like me, you've developed strong intuitions about what makes good software and effective teams. These aren’t wrong—they’re just incomplete for the new context we're entering. The principles of clean code, clear architecture, and strong team dynamics remain crucial, but they need to be viewed through a new lens.

## Mental Models & Principles to Recalibrate

### 1. Expertise as Bottleneck → Context as Substrate

We’ve long prized deep human expertise as the cornerstone of quality. But agents thrive not on knowing more, but on being given *the right context*. Your new job: shaping that context. Standardizing interfaces. Curating knowledge. Designing work in ways that make it legible to machines.

### 2. Architecture as Fixed Plan → Architecture as Dialogue

In the agentic paradigm, architecture emerges iteratively. Agents can critique, revise, and prototype structures continuously. The architecture function becomes less about upfront definition and more about constraint management and pattern evolution over time—often *with* agents, not just *for* them.

### 3. Developer Productivity → System Throughput

We’ve measured impact by individual productivity, or for those thinking systemically, team throughput. Now, the key metric is *system* throughput: how effectively your team *and its agents* can solve problems end-to-end. We'll need to rewire how we think about velocity, contribution, and team design.

### 4. Code as Conversation

Traditional development involved writing code line-by-line, with reviews focusing on implementation details. With AI tools, code becomes more conversational—you describe intent and outcomes, and the AI proposes implementations. This shifts the focus from "how to write it" to **"how to describe what we want"**, and continually monitor for drift in the real world.

### 5. Velocity vs. Understanding

AI tools can generate code rapidly, but this speed can mask comprehension gaps. Your role becomes less about reviewing syntax and more about ensuring your team:
- Understands the system's architecture and boundaries
- Can effectively communicate requirements to AI tools
- Maintains a clear mental model of **both the codebase and the domain**

### 6. From Specialist to Synthesist

Deep technical specialization is still valuable—but increasingly needs to be paired with:
- Strong system design principles
- Effective prompt engineering skills
- Ability to validate and integrate AI-generated solutions while they are running

## Where to Start If You’re Already Playing with AI

If you're already familiar with ChatGPT or using code copilots, it's time to move beyond enhanced software construction and look at how the **systems themselves** will be designed differently in an agentic world.

- **Use the Tools Personally**  
  Install GPT-based agents locally or in agent-enabled IDEs like Cursor or Continue.dev. Try multi-agent frameworks like AutoGen, crewAI, or LangGraph. Give yourself *real* tasks to solve (repeat them kata-style). Don’t outsource the learning—experience the new ergonomics of agency.

- **Codify What You Know**  
  The best agents are trained on *your* ways of working. Document your playbooks, architectural heuristics, and domain insights as structured prompts or decision trees. You're not just enabling people—you’re enabling your future AI collaborators.

- **Rethink the “Team” Interface**  
  Think beyond roles. Rethink ownership, observability, and accountability in systems where decision-making is increasingly non-human in origin.

- **Model the Future**  
  Sketch the org you *would* build if agents could replace 40% of your engineering effort. How would onboarding change? How would you pair? What would code reviews look like? This isn’t about cost cutting—it’s about *adaptation*.

## How to Start From Scratch

If you're completely new to agentic tools:

1. **Start Small**
   - Use AI for documentation, test case generation, or bug explanations
   - Ask AI to explain existing code before generating new code
   - Refactor small components with AI assistance

2. **Build New Muscles**
   - Learn to write clear, specific prompts
   - Practice validating AI output against architectural intent
   - Establish feedback loops to iteratively improve how you work with agents

3. **Lead by Example**
   - Share your journey and learning curves openly with your team
   - Create guidelines for AI-assisted development
   - Encourage shared libraries of effective prompts and system design patterns

## Looking Ahead: The Next 18 Months

The rate of change in AI tooling and agentic architecture is exponential. Where you focus will depend on your context, but key foundations are universal:

- Emphasize architectural integrity over implementation correctness
- Evolve code review practices to include AI-generated contributions
- Maintain strong documentation of system boundaries and responsibilities
- Instrument your systems deeply—**observability is the best early surface for experimenting with agents**
- Make sure you're thinking about data effectively

For more, see my articles that focus more deeply on:

1. [Agentic AI]({% post_url 2025-03-21-2-agentic-ai-challenges-to-traditional-org-design %})
2. [Data as a strategic asset]({% post_url 2025-03-21-3-data-strategic-asset %})

## Conclusion

Agentic AI won’t replace seasoned engineering leadership. But it *will* reward those who retool their experience for this new collaborative frontier.

We’re not just getting better tools—we’re gaining new collaborators. Our role is shifting from crafting every line of code to directing and curating a human–AI partnership.

Start small. Stay curious. Share what you learn.

Let’s shape what’s next.