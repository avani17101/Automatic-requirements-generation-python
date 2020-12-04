# Automatic generation of requirements.txt 

This is a script for generating requirements.txt given any folder conatining python files.
It is made to make our lives easier in cases where requirements.txt is not provided and we need to scan through each python file to check libraries needed.

# Usage
```bash
 python3 requirements_gen.py <path dir> <sub_flag>
```
<path dir> is the path of directory to be scanned 
if <path dir> is not given it scans the current directory
<subdir_flag> is 1 if user wants to get libraries of sub directory
 
#### Example (again to make life easier)
* Scan the current directory
 ```bash
 python3 requirements_gen.py 
```

* Scan the current directory and it's subdirectories
 ```bash
 python3 requirements_gen.py 1
```

* Scan the directory given in path
 ```bash
 python3 requirements_gen.py <path>
```


* Scan the directory and subdirectories in directory whose path given
```bash
 python3 requirements_gen.py <path> 1
```


