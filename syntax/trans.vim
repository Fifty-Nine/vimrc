if version < 600
  syntax clear
elseif exists("b:current_syntax")
  finish
endif

syn keyword transKeyword

