# ShellPride

<span style="margin-right: 10px; background: rgb(255, 0, 0); color: rgb(255, 0, 0)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(92,206,250); color: rgb(92,206,250)">-------------------------------------------</span><br/>
<span style="margin-right: 10px; background: rgb(255, 142, 0); color: rgb(255, 142, 0)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(245,169,184); color: rgb(245,169,184)">-------------------------------------------</span><br/>
<span style="margin-right: 10px; background: rgb(255, 255, 0); color: rgb(255, 255, 0)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(255,255,255); color: rgb(255,255,255)">-------------------------------------------</span><br/>
<span style="margin-right: 10px; background: rgb(0, 142, 0); color: rgb(0, 142, 0)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(255,255,255); color: rgb(255,255,25592)">-------------------------------------------</span><br/>
<span style="margin-right: 10px; background: rgb(0, 192, 192); color: rgb(0, 192, 192)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(245,169,184); color: rgb(245,169,184)">-------------------------------------------</span><br/>
<span style="margin-right: 10px; background: rgb(64, 0, 152); color: rgb(64, 0, 152)">-------------------------------------------</span> <span style="margin-right: 10px; background: rgb(92,206,250); color: rgb(92,206,25052)">-------------------------------------------</span><br/>

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
