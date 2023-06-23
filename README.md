# command_not_found
simple shit code to fetch the install command from https://command-not-found.com/ and ask if it should be ran.

add dis to ur .zshrc to utilize it (arch based distros only):
```sh
command_not_found_handler() {
    echo "zsh: command not found: $1" >&2
    python3 /path/to/main.py $1
}
```
