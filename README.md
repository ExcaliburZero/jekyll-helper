# Jekyll Helper [![Travis CI Status](https://api.travis-ci.org/ExcaliburZero/jekyll-helper.svg)](https://travis-ci.org/ExcaliburZero/jekyll-helper) [![Coverage Status](https://coveralls.io/repos/ExcaliburZero/jekyll-helper/badge.svg?branch=master)](https://coveralls.io/r/ExcaliburZero/jekyll-helper?branch=master)

Jekyll Helper is a GUI for the static website generator [Jekyll](http://jekyllrb.com/).

![Screenshot of Jekyll Helper](/data/media/screenshot.png)

#Table of Contents
- [External Links](#external-links)
- [Licensing](#licensing)
- [Installation](#installation)
  - [Linux](#linux)
    - [Debian-based Distros](#debian-based-distros)
      - [PPA](#ppa)
      - [Deb package](#deb-package)
    - [Arch Linux](#arch-linux)
      - [AUR](#aur)
      - [Package from source](#package-from-source)
    - [Compile from source](#compile-from-source)
  - [Other](#other)
- [Development](#development)
  - [Running from source](#running-from-source)
  - [Translations](#translations)
  - [Editing help pages](#editing-help-pages)
  - [Updating program version](#updating-program-version)

## External Links
- [Jekyll Helper's website](https://excaliburzero.github.io/jekyll-helper/)
- [Jekyll Helper's Launchpad entry](https://launchpad.net/jekyll-helper)

## Licensing
This program is licensed under [The MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more information.

## Installation
Below are some instructions on how to install Jekyll Helper. If there are any other installation instructions that should be added, then feel free to add them via a pull request.

Note that before you install Jekyll Helper you should first install Jekyll. Without Jekyll installed, Jekyll Helper will still install, but it will not be able to perform any functions using Jekyll.

### Linux
#### Debian-based Distros
##### PPA
This program can be installed on Debian-based Linux distros through the following personal package archive `ppa:excaliburzero/jekyll-helper`. The commands to install it via that ppa are as follows:

```
sudo add-apt-repository ppa:excaliburzero/jekyll-helper
sudo apt-get update
sudo apt-get install jekyll-helper
```

##### Deb package
This program can also be installed on Debian-based Linux distros through the `.deb` packages that are included in the released versions of the program. The `.deb` packages for each version of the program can be found on the program's [releases page](https://github.com/ExcaliburZero/jekyll-helper/releases).

#### Arch Linux
##### AUR
This program can be installed from the latest git through the Arch User Repository. It can be created from the AUR manually or through using an AUR client like Yaourt.

The command to install it with Yaourt is the following:

```
yaourt jekyll-helper-git
```

##### Package from source
This program can be packaged and installed for Arch Linux via its source code by running the following commands.

```
makepkg
sudo pacman -U PACKAGEFILENAMEHERE
```

#### Compile from source
This program can be compiled from it source code. It is generally packaged via Quickly, however it should be able to be compiled through other methods.

If you are able to successfully compile this program from it source, please add the method you used to here via a pull request.

### Other
If you are not using Linux, then you should be able to compile Jekyll Helper from its source code.

If you are able to successfully compile this program from it source, please add the method you used to here via a pull request.

## Development
The following is information regarding the development process for Jekyll Helper.

### Running from source
Jekyll Helper can be run via it's source code using Cannonical's Quickly program. In order to do so, you must first enter the jekyll-helper directory in the terminal and run the `quickly run` command.

### Translations
This program uses Gettext for its translations and handles the creation of its translation files through the [translations section of its Launchpad entry](https://translations.launchpad.net/jekyll-helper). The translation files are then downloaded and added into the GitHub hosting of the program.

### Editing help pages
The help pages for Jekyll Helper are located in the `/help/C/ directory`. They use the [Mallard](http://projectmallard.org/1.0/) markup language.

In order to be able to read the help pages when running Jekyll Helper from source, you first need to temporarily change the following line in `/jekyll_helper_lib/Window.py`

```
show_uri(self, "help:%s" % get_help_uri())
```

To the following:

```
show_uri(self, "ghelp:%s" % get_help_uri())
```

This is due to some issue with the installed version of Jekyll Helper requiring the use of "help", while when running Jekyll Helper from source, "ghelp" is required.

### Updating program version
To change the version number of Jekyll Helper a few things need to be updated.

- Manual page - Needs to have the version number updated as well as the last update date. `/doc/jekyll-helper.1`
- About window - Needs to have the version number updated. `/data/ui/AboutJekyllHelperDialog.ui`
- Config library file - Needs to have the version number updated. `/jekyll_helper_lib/jekyll_helperconfig.py`
- Setup file - Needs to have the version number updated. `/setup.py`
- Debian changelog - Needs to have an entry added for the version update. `/debian/changelog`
