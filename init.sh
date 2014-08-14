#!/bin/bash
set -e
git submodule update --init --recursive
ln -s ${HOME}/.vim/vimrc ${HOME}/.vimrc
vim -c 'BundleInstall' -c 'quit'
