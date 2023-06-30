# command_not_found
simple shit code to fetch the install command from https://command-not-found.com/ and ask if it should be ran.

only works properly on arch based distros but all you have to do is change a couple of lines of code but
i will not say which ones, just guess :> 

to install the required modules, run dis:
```sh
pip install inputimeout beautifulsoup4 requests
```

add dis to ur .zshrc to utilize it:
```sh
command_not_found_handler() {
    echo "zsh: command not found: $1" >&2
    python3 /path/to/main.py $1
}
```

[![asciicast](screencast.gif)](https://asciinema.org/a/eUY0dFGnxOi2xDdIag3BFbbiQ)

