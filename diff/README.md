diff
======================


About
----------------
- Make diff for each file in every folder and subfolder and create diff directory which contain the diff directory for each file separatly
- This also can copy those which are not the same from new folder


Get started for diff
----------------
- put your old files to old folder,
- put your new files to new folder,
- run: <br>
$ cd diff <br>
$ ./diff <br>
- the diff files will be in diff/old folder (sry for script mess)

Get started for make
----------------
- put your new files into new/diff/diff/ (again sry about this one couldn't make it right :D)
- run: <br>
$ cd diff <br>
$ ./make <br>
- the diffrent files from new folder will be in make folder


NOTE
----------------
- if there's a file in old folder that is not exist in new folder it will be written into terminal but will ignore it
- if there's a file in new folder that is not exist in old folder it will be ignored and won't give you any warn
- you can see an example in old and new folder that has created a diff folder

