# hyper-helper
-----------------
I use [Karabiner Elements](https://pqrs.org/osx/karabiner/) to implement my "Hyper Mode" keyboard shortcuts. Simply put, I remap Caps Lock to a custom "Hyper" modifier key, and then use the new "Hyper" key to run scripts or input other keyboard shortcut in a more convenient way.

Useful as they were, actually configuring these shortcuts was hellish. Karabiner uses JSON as its config file, and when you have 87 shortcuts that each take up at least 5 or 6 lines, you end up with a 2200 line JSON file that has to be edited by hand. In the year 2020 nobody should have to edit a 2200 line JSON file by hand, or at least if they don't want to.

As a result of my pent-up frustration at accidentally breaking my config every time I changed, I wrote this short Python script that reads a `mappings.txt` file and generates the Karabiner
config file. Each mapping is either to a shell command or a key code combination. They have a custom format, one that is admittedly not the easiest to read but is far more easily edited than a JSON file. If you want to view my mappings file, you can find it [here](https://raw.githubusercontent.com/ccarterlandis/dotfiles/master/.config/hyper-helper/mappings.txt) with all my other dotfiles. To generate them, after you install Karabiner place a `mappings.txt` file in your `$HOME/.config/hyper-helper/` directory. Then, clone this repo and run `create.py` with a valid Python 3.6+ interpreter.

TL;DR

```bash

$ cd $HOME/
$ curl -o .config/hyper-helper/mappings.txt https://raw.githubusercontent.com/ccarterlandis/dotfiles/master/.config/hyper-helper/mappings.txt
$ git clone https://github.com/ccarterlandis/hyper-helper.git
# assuming you have Python 3.6 is installed under python3
$ python3 hyper-helper/create.py

```