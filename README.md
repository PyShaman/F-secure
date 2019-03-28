# F-secure
_User guide_
###### Author: Michał Bek
###### Email: michal.bek@gmail.com


**List of contents**

**1. Python version and installation**

**2. Installing required packages**

**3. Usage**

_1. Python version and installation_

This test framework is written in Python 3.5+ and it should be ran on 
this version or higher. User can download newest version of Python at 
[Python download site](https://www.python.org/downloads/).

For Windows users there are many tutorials 
[for example](https://www.howtogeek.com/197947/how-to-install-python-on-windows/).

For Linux distribution 
[users](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-debian-8).

After installing Python on your OS user should clone project 
[repository](https://github.com/PyShaman/F-secure.git).
The main branch will be the _master_.

_2. Installing required packages_

After cloning repository locally user should enter F-secure folder and install 
required packages using following command:

```
> pip3 install -r requirements.txt
```

This will automatically download and install following packages: 
[behave](https://pypi.org/project/behave/) and [selenium](https://pypi.org/project/selenium/).


_3. Usage_

```
> behave -D browser=chrome
```
or
(not working yet, due to geckodriver problems)
```
> behave -D browser=firefox
```