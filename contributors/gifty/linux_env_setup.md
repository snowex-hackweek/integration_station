# Setting up in linux / coumpute clusters / virtual environment to access SnowEx Data at the NSIDC DAAC

Instructions on how to set up linux environment to download snowex data from NSIDC with python APIs

## Getting Started

This codes will be run directly from the linux terminal.

### 1. Logging into computing systems (not necessary in linux machines) 

SSH into working environment 

Example below is for sharnet graham clusters (different based on system being used)

```
ssh -Y user@graham.computecanada.ca
```
Enter password after line below

```
user@graham.computecanada.ca's password:
```

### 2. Creating python virtual environment(1. Computing clusters 2. linux)
#### 1. Creating python virtual environment in computing clusters eg.graham clusters
Load python module

```
[user@server ~]$ module load python/3.6

```

Create virtual environment ("venv" in this case is the name of virtual environment directory-any preferred name can be used)

```
[user@server ~]$ virtualenv --no-download venv

```
Activate virtual environment

```
[user@server ~]$ source venv/bin/activate
```
Upgrade pip

```
(venv) [user@server ~]$ pip install --no-index --upgrade pip
```

Deactivate virtual environment

```
(venv) [user@server ~]$ deactivate

```

#### 2. Creating python virtual environment in linux
Install pip if not in system

```
user@computer:~$ sudo apt-get install python3-pip

```
Install virtual env

```
user@computer:~$ pip install virtualenv
```
Check installation

```
user@computer:~$ virtualenv --version
```
Create virtual environment ("venv" in this case is the name of virtual environment directory-any preferred name can be used)

```
user@computer:~$ virtualenv venv
```

Activate virtual environment

```
user@computer:~$ source venv/bin/activate
```

Deactivate virtual environment

```
(venv) user@computer:~$ deactivate

```

### Prerequisites to access NSIDC data

#### Software packages ncessary to access and process NSIDC data

Packages
```
os
geopandas
shapely
pandas as pd 
requests
json
pprint
getpass
netrc
platform 
getpass
urllib
CookieJar
ElementTree
time
zipfile
io
shutil

```

#### Software packages to be installed in virtual environment
Most of the packages are already installed in the python environment and the rest will be installed while installing geopandas 

Install geopandas
```
(venv) user@computer:~$ pip install geopandas

```

Install requests
```
(venv) user@computer:~$ pip install requests


