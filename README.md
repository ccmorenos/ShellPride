# ShellPride 🏳️‍🌈 :transgender_flag:

Shell scripts of pride flags to decorate the console.

## Installation

### From command

ShellPride is installed running one of the following commands, using ether
`curl` or `wget`.

```shell
# Whith curl
bash -c "$(curl -fsSl https://raw.githubusercontent.com/ccmorenos/ShellPride/main/tools/install.sh)"

# Whith wget
bash -c "$(wget -O- https://raw.githubusercontent.com/ccmorenos/ShellPride/main/tools/install.sh)"
```

### From Source

To install ShellPride from source, first clone the repository.

```shell
git clone https://github.com/ccmorenos/ShellPride.git

cd /ShellPride

```

Then install the package ether in `/usr/local/bin`.

```shell
sudo make install
```

Or in ``

```shell
make install-user
```

This installation will add the following line in the resource file, to make
sure that `~/.local/bin` is in the `PATH`.

```shell
export PATH=$PATH:~/.local/bin
```

## Usage
