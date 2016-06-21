# Software Development Methodologies

In software (as in most complex task sets), it is common to break up the larger process into discrete activities to better organize the process and predict the outcomes.

There are [many ways to organize software projects](https://en.wikipedia.org/wiki/List_of_software_development_philosophies). Collectively these are known as [software development methodologies](https://en.wikipedia.org/wiki/Software_development_process).

------

## Waterfall

[Waterfall](https://en.wikipedia.org/wiki/Waterfall_model) describes a software development lifecycle (SDLC) where each of several stages is completed before the next stage begins. The following is a common set of stages in the SDLC:

1. Requirements gathering
1. Analysis
1. Design
1. Development
1. Testing
1. User acceptance
1. Maintenance

One problem with waterfall is that, because requirements are only gathered at the beginning of the project, stakeholders take a “kitchen sink” approach and list every possible feature as a requirement just in case it ends up being needed. This results in bloated software.

Using the waterfall approach, it is exceedingly common for customers to see a finished product that meets all of the original requirements, but isn’t exactly what they want. Agile methodologies were developed as a way to mitigate this phenomenon.

------

## Agile

Agile as a software methodology was conceived of in the 1990s and popularized around 2001 by a group of seasoned programmers who came together over a snowy weekend in Utah to agree on a better way to develop software.

The result of that weekend’s conversations was [The Agile Manifesto](http://www.agilemanifesto.org/). It stated, in part, that the signees valued:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

In other words, while there is value in the things on the right side, they agreed that they valued the things on the left side more.

The [full list of principles](http://www.agilemanifesto.org/principles.html) is worth reading. All modern agile methodologies were influenced by them.

Two of the most popular Agile methodologies are Scrum and Kanban.

### Scrum

Scrum is an approach to building software that emphasizes team self-organization around rapid iterations (called “sprints”). It was developed in response to the waterfall process as an acknowledgment that customers will (and should!) change their minds over the course of most software projects.

Scrum describes the following, three primary roles:

1. **Product owner**
    - Represents the stakeholders and is the voice of the customer
    - Maintains an absolutely ordered backlog of issues, written from the perspective of the user (user stories)
1. **Development team**
    - Responsible for delivering potentially shippable increments (PSIs) of product at the end of each sprint
     - Teams are typically cross-functional and self-organizing
1. **Scrum master**
    - Facilitates Scrum activities such as sprint planning, daily stand-ups, and retrospectives
    - Acts as a buffer between the team and potentially distracting influences
    - Removes impediments to the team accomplishing its goals

Work under Scrum is broken up into sprints. The length of a sprint can be anywhere from a week to a month or two, but should only be as long as the amount of time the business can go without changing its mind.

Sprints typically consist of the following rituals:

1. **Sprint planning —** The team agrees on a scope of work for the coming sprint
1. **Daily standups —** What I did yesterday, what I’ll do today, impediments
1. **Sprint review —** Demos
1. **Sprint retrospective —** Stop, start, and continue doing

A criticism of Scrum is that it is essentially a series of mini-waterfall lifecycles. While this is an improvement over true waterfall, there are methodologies that are conceived of as more continuous flows. One of those is Kanban.

### Kanban

[Kanban](https://en.wikipedia.org/wiki/Kanban) was originally developed by Taiichi Ohno as a way for Toyota to more efficiently manage assembly lines and other manufacturing processes.

Ohno said there were the following “seven wastes” common to manufacturing:

1. Delay, waiting or time spent in a queue with no value being added
1. Producing more than you need
1. Over processing or undertaking non-value added activity
1. Transportation
1. Unnecessary movement or motion
1. Inventory
1. Reduction of Defects

Kanban has fewer rituals and artifacts than Scrum, but it does prescribe a few.

1. Visualize the workflow ([Trello](https://trello.com) is really good for this!)
1. Lead using a team approach
1. Reduce the Batch Size of your Efforts (BASE) (i.e. use [decomposition](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/4/decomposition.md) to limit work in progress [WIP])
1. Learn and improve continuously

------

Sources:

1. [List of software development philosophies](https://en.wikipedia.org/wiki/List_of_software_development_philosophies)
1. [Software development process](https://en.wikipedia.org/wiki/Software_development_process)
1. [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model)
1. [The Agile Manifesto](http://www.agilemanifesto.org/)
1. [Principles behind the Agile Manifesto](http://www.agilemanifesto.org/principles.html)
2. [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development\))
1. [Kanban](https://en.wikipedia.org/wiki/Kanban) (manufacturing)
2. [Kanban](https://en.wikipedia.org/wiki/Kanban_(development\)) (software development)
1. [Open Kanban Introduction](https://www.infoq.com/articles/open-kanban-introduction)
