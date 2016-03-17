# Project Name

Tmux random name session generator, inspired by Docker.
This is small plugin that will generate random session name every time you open new Terminal session or reconnect to 
prevousely disconnected sessions.

![alt tag](https://github.com/lanox/tmux/blob/master/screenshoots/tmux-session-generator.png)
![alt tag](https://github.com/lanox/tmux/blob/master/screenshoots/tmux-session-generator1.png)

## Installation

Script is written in Python3. So you may need to setup pyenv or get python3 from Homebrew.

iTerm2 Specific.

1. Clone this repository.
2. Preferences -> Profiles -> General
   * Under Command Section:
   * Send test at start: Add tmux.py

This will start tmux.py everytime you open new window.

## Usage

If you have got steps above right, every time you open new iTerminal you should either be reconnected to a disconnected session, or new session will be created with random session name.

## Contributing

Happy for any contribution to be send.

## History

If Docker can generate random names every time it creates container so can tmux.

## Credits

Inspired by Docker.
