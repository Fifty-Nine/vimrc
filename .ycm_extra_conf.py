# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def FindDatabase(cwd):
  cd_path = cwd + "/compile_commands.json"
  if os.path.exists(cd_path):
    return ycm_core.CompilationDatabase(cwd)

  if cwd == "/":
    return None

  return FindDatabase(os.path.dirname(cwd))

def GetAlternateName(filename):
  return os.path.splitext(filename)[0] + ".cpp"

# These are the compilation flags that will be used in case there's no
# compilation database found.
default_flags = [
'-Wall',
'-Wextra',
'-Wundef',
'-Wwrite-strings',
'-Wno-format-security',
'-Wno-unused-parameter',
'-Wno-mismatched-tags',
'-Wno-unused-function',
'-Wno-format',
'-Wno-switch',
'-std=c++11',
'-Wno-deprecated',
'-I', '.',
'-I', '..',
]
# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
database = FindDatabase(os.path.abspath(os.getcwd()))

def GetFlagsFromDatabase(filename):
  if database is None:
    return None

  # Bear in mind that compilation_info.compiler_flags_ does NOT return a
  # python list, but a "list-like" StringVec object
  compilation_info = database.GetCompilationInfoForFile( filename )
  
  if len(compilation_info.compiler_flags_) == 0:
    compilation_info = database.GetCompilationInfoForFile(GetAlternateName(filename))

  if len(compilation_info.compiler_flags_) == 0:
    return None

  return MakeRelativePathsInFlagsAbsolute( 
    compilation_info.compiler_flags_, compilation_info.compiler_working_dir_ )

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) ) 

def RelocationDirectory(filename):
  return DirectoryOfThisScript()

def FlagsForFile( filename ):
  flags = GetFlagsFromDatabase(filename)
  
  if flags is None:
    flags = MakeRelativePathsInFlagsAbsolute( 
        default_flags, RelocationDirectory(filename) )

  return {
    'flags': flags,
    'do_cache': True
  }
