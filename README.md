# Template for making a Python CLI script installable via pip

This demonstrates making a CLI pip-installable.

It provides a command called `pi` that takes the number of decimal places as its sole argument.

e.g.,

```
$ pi 80
3.14159265358979323846264338327950288419716939937510582097494459230781640628620899
```

It accepts a `-v` argument that will show a progress bar.

## Installation

```
pip install git+https://github.com/WHOIGit/pip-installable-cli@v0.1.0
```
