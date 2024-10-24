#!/bin/bash
set -e
sudo apt-get install vim-nox build-essential cmake
git submodule update --init --recursive
if [ ! -e ${HOME}/.vimrc ]; then
  ln -s ${HOME}/.vim/vimrc ${HOME}/.vimrc
fi
vim -c 'PluginInstall'
