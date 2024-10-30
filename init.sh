#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]; then
  sudo apt-get install vim-nox build-essential cmake
else
  apt-get install vim-nox build-essential cmake
fi
git submodule update --init --recursive
if [ ! -e ${HOME}/.vimrc ]; then
  ln -s ${HOME}/.vim/vimrc ${HOME}/.vimrc
fi
ex -c 'PluginInstall' -c 'qall'
