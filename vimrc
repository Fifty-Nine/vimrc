" Force vim
set nocompatible
filetype plugin indent on

" Set 256 colors for CSApprox
set t_Co=256

colorscheme desert
syntax on
set hls
set mouse=a

" Fixup PgUp/PgDown
nnoremap <silent> <PageUp> <C-U><C-U>
vnoremap <silent> <PageUp> <C-U><C-U>
inoremap <silent> <PageUp> <C-\><C-O><C-U><C-\><C-O><C-U>

nnoremap <silent> <PageDown> <C-D><C-D>
vnoremap <silent> <PageDown> <C-D><C-D>
inoremap <silent> <PageDown> <C-\><C-O><C-D><C-\><C-O><C-D>

" Make home key consider indentation
function! SmartHome()
  let s:col = col(".")
  normal! ^
  if s:col == col(".")
    normal! 0
  endif
endfunction
nnoremap <silent> <Home> :call SmartHome()<CR>
inoremap <silent> <Home> <C-O>:call SmartHome()<CR>

" Tell vim to remember certain things when we exit
"  '10 : marks will be remembered for up to 10 previously edited files
"  "100 : will save up to 100 lines for each register
"  :20 : up to 20 lines of command-line history will be remembered
"  % : saves and restores the buffer list
"  n... : where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo

" Use shell-style tab completion
set wildmode=list:longest

" Make backspace behave
set backspace=indent,eol,start

" Handle mac file formats
set fileformats=unix,mac,dos

" Highlight lines longer than 80 characters
au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)

" Recognize LLVM
augroup filetype
    au! BufRead,BufNewFile *.ll set filetype=llvm
    au! BufRead,BufNewFile *.td set filetype=tablegen
    au! BufRead,BufNewFile *.tpp set filetype=cpp
augroup END

" Vim bundles
set rtp+=~/.vim/bundle/vundle
call vundle#rc()

Bundle 'gmarik/vundle'
if v:version > 703 || (v:version == 703 && has('patch584'))
  Bundle 'Valloric/YouCompleteMe'
endif
 
Bundle 'scrooloose/syntastic'
Bundle 'rosenfeld/conque-term'

" YouCompleteMe settings
let g:ycm_extra_conf_globlist = [ '*' ]
let g:ycm_global_ycm_extra_conf='~/.vim/.ycm_extra_conf.py'

" Custom key mappings
map <F2> :vsplit<CR>:A<CR>
map <F7> :cprev<CR>
map <F8> :cnext<CR>
map <F9> :clist<CR>
map <F10> :clist!<CR>
map <F12> :make<CR>

