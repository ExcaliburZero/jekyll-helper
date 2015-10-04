---
layout: page
title: Jekyll Helper
tagline: A GUI for Jekyll
---
{% include JB/setup %}

**Jekyll Helper** is a program that serves as a basic GUI for [Jekyll](http://jekyllrb.com/). It allows users to more easily test and build their websites by offering a GUI interface for serveral of Jekyll's main functions.

![A screenshot of Jekyll Helper]({{ BASE_PATH }}/assets/images/screenshots/screenshot_01.png)

## Screenshots
To see more screenshots of Jekyll Helper, please see the [screenshots page]({{ BASE_PATH }}/screenshots.html).

## Download
Jekyll Helper primarily supports Linux, however it may be able to run on other operating systems.

### Debian-based Linux distros
To install Jekyll Helper on Linux if you are using a Debian based distro like Ubuntu, you can install Jekyll Helper by running the following commands.

    sudo add-apt-repository ppa:excaliburzero/jekyll-helper
    sudo apt-get update
    sudo apt-get install jekyll-helper

You could also download and install the program from the ".deb" file on the [releases page](https://github.com/ExcaliburZero/jekyll-helper/releases) on GitHub.

### Arch Linux-based distros
This program can be installed from the latest git through the Arch User Repository. It can be created from the AUR manually or through using an AUR client like Yaourt.

The command to install it with Yaourt is the following:

    yaourt jekyll-helper-git

This program can be packaged and installed for Arch Linux via its source code by running the following commands.

    makepkg
    sudo pacman -U PACKAGEFILENAMEHERE

### Other operating systems
If you are not using a Debian-based or Arch Linux-based Linux distro, then you should be able to compile Jekyll Helper from its source code which can be found in the program's GitHub repository.

## Licensing
Jekyll Helper is licensed under [The MIT License](http://opensource.org/licenses/MIT), so feel free to use any portion of it. Jekyll Helper is © <2015> <[Christopher Wells](http://christopher-randall-wells.divshot.io/)>.
