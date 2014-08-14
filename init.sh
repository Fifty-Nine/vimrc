#!/bin/bash
set -e
git submodule update --init --recursive
if [ ! -e ${HOME}/.vimrc ]; then
  ln -s ${HOME}/.vim/vimrc ${HOME}/.vimrc
fi
vim -c 'BundleInstall'
./bundle/YouCompleteMe/install.sh --clang-completer
