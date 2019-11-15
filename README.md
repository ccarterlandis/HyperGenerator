# HyperGenerator
-----------------
I use [Karabiner Elements](https://pqrs.org/osx/karabiner/) to implement my keyboard shortcuts. 
When I first stumbled upon it, I recall finding what I thought was the most useful shortcut in the world:
remapping the useless Caps Lock (which is taking up prime real estate) into a whole new modifier key which
was easily programmable and flexible. I've never looked back.

One constant pain point, however, was actually configuring these shortcuts. For all its praise, Karabiner
for some god-forsaken reason uses JSON as its config file. I detest JSON as config for many, many reasons,
but primarily for its lack of comments - which are essential in any configuration file - and its highly structured nature.
JSON was designed to enable communication between programs: that is, a program creates it, and a program consumes it.
While humans do write these programs which create the JSON, very rarely do they have to edit it manually: it's usually generated for them.
JSON is at its core a data transfer format, not a markup language.

Using something like YAML, on the other hand, is much easier for a human to read, and still easy for a machine to parse. It's only every written by a human,
so it's easily understood and changed, unlike JSON's rigorous KVP structure.

My configurations quickly got out of hand - I was having to edit a 2000 line JSON file any time I wanted to update my shortcuts. However, if I missed a single
`}` or `]`, the whole config would be rendered invalid and my shortcuts would disappear until I fixed the issue. Before recent improvements to the logging of Karabiner,
I would have to find these manually, which was just near impossible.

As a result of this frustration of constantly accidentally breaking my config, I wrote this short Python script that reads the `mappings.txt` file and auto-generates my Karabiner
config file. Each mapping is either to a shell command or a key code combination, as those are the two primary shortcuts I use. They have a rigorously defined format, but one that
both easily read and easily edited. As a result, I'll now be able to change my shortcuts confidently as I see fit, allowing me to refine my development process further than I already have.
