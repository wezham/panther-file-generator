# About 

This tool does the job of:

1. Creating collections of files you will need when creating a rule, scheduled rule or helper file
2. Linking those files were necessary. For example it links a scheduled rule and scheduled query

# Usage

```
usage: panther-generate TARGET_DIR [rule,scheduled-rule,helper] FILE_NAME

Generates the boilerplate files for creating panther detections in code

positional arguments:
  item-type             What you would like to create [rule,scheduled-rule,helper]
  target directory      Specifies the directory you would like to create the files in

optional arguments:
  -h, --help            show this help message and exit
  --file-name [file-name]
                        Name of the item you are creating. For example onepassword_account_access
```

# Installation

1. `git clone`
2. `cd` into package
3. `pip install .`

# Contributing 

TBC