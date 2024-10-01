# PASSWORD LOCK MANAGER

### PROJECT DESCRIPTION

######  PASSWORD MANAGER

This is a project based on my personal problem and challenge of having accounts on many different websites. I know it is a **bad practice** to 
use the same password for each of them because if any of those sites has 
a security breach, the hackers will learn the password to all of your other 
accounts. It’s best to use password manager software on your computer that 
uses one master password to unlock the password manager. Then you can 
copy any account password to the clipboard and paste it into the website’s 
Password field.

###### CAUTION
This project is not secured but I will continue to apply and build on it so as to make it more secure for users. The project report/documentation offers a basic demonstration of how this program work.

### PROJECT DOCUMENTATION

###### PROGRAM DESIGN & DOCUMENTATION

This program is designed to run with a command line argument 
that is the account’s name—for instance, email or blog. That account’s 
password will be copied to the clipboard so that the user can paste it into 
a Password field. This way, the user can have long, complicated passwords 
without having to memorize them.

**Python Module Import**

This program makes use of the system variables and command line functions,there is the need for a system import.We then use:

**system module**

> import sys

**copy module**
> import pyperclip

**Requirement**
* string for the filename
* first command line argument

**Right Password Copy**

The program checks up the key:value pair in the dictionary to validate if it is already saved up.

