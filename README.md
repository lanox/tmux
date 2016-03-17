# TMUX RANDOM session name generator.

Tmux random name session generator, inspired by Docker.
This is small plugin that will generate random session name every time you open new Terminal session or it will reconnect your previously disconnected sessions.

![alt tag](https://github.com/lanox/tmux/blob/master/screenshoots/tmux-session-generator.png)
![alt tag](https://github.com/lanox/tmux/blob/master/screenshoots/tmux-session-generator1.png)

## Installation

Script is written in Python3. So you may need to setup pyenv or get python3 from Homebrew.

iTerm2 Specific.

1. Clone this repository somewhere on you drive.
2. Preferences -> Profiles -> General
   * Under **Command Section:**
    * **Send test at start:** Add tmux.py

This will start tmux.py everytime you open new window.

## Usage

Open New terminal session.

## Inspired

If Docker can generate random names every time it creates container so can tmux.

## Credits

Inspired by Docker.
