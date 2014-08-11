#!/bin/bash

cd ${HOME}/.vim
git submodule update --init
ln -s ${HOME}/.vim/vimrc ${HOME}/.vimrc
