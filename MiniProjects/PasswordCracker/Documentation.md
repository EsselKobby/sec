## PASSWORD CRACKER PROJECT

###### 

###### Sec Mini Project
[FORESS TECH](https://linkedin.com/ForessTech)
___
Author:
Bernard Kobina Forson Essel


[SourceCode](https://github.com/EsselKobby/sec/edit/main/MiniProjects/PasswordCracker/Documentation.md)

___

## Table of Contents

- [THE PASSWORD CRACKER PROJECT](#password-cracker-project)
          - [FORESS TECH](#foress-tech)
  - [Table of Contents](#table-of-contents)
    - [Executive Summary](#executive-summary)
    - [Project Analysis](#analysis-of-project)
    - [Key Recommendations](#key-recommendations)
    - [Password Attacks Methodology](#password-attacks-methodology)
     - [Brute Force Attack](#brute-force-attack)
            - [Word List ](#wordlist-enumeration)
        - [DICTIONARY ATTACK](#dictionary-attack)
              - [File Types](#file-types)
        - [Reverse Brute Force Attack](#brute-force-attack)
            - [DETAILED FINDINGS](#detailed-findings)
              - [Brute Force Attack](#brute-force-attack)
            - [Finding Summary](#finding-summary)
            - [Evidence](#evidence)
            - [Affected Resources:](#affected-resources)
            - [Recommendations:](#recommendations)
            - [References:](#references)
              - [Dictionary Attack](#dictionary-attack)
            - [Finding Summary](#finding-summary-1)
            - [Evidence](#evidence-1)
            - [Affected Resources:](#affected-resources-1)
            - [Recommendations:](#recommendations-1)
            - [References:](#references-1)
              - [Reverse Brute Force Attack](#reverse-brute-force-attack)
            - [Finding Summary](#finding-summary-2)
            - [Evidence](#evidence-2)
            - [Affected Resources:](#affected-resources-2)
            - [Recommendations:](#recommendations-2)
            - [References:](#references-2)
      - [CVSS v3.0 Reference Table](#cvss-v30-reference-table)
            - [THE GUI interface](#the-gui-interface)
        - [Project Demonstration](#project-demo.)
    ___
    
## THE PASSWORD CRACKER PROJECT
This a project that creates a python tool to crack passwords. This tool will be able to handle various file types,such as **ZIP**, **Excel**, **Word**, and **PDF** files.
It will make use of different password attack methods, including ***brute force***, ***dictionary***, and ***reverse brute force attacks***. Additionally, I will build an easy-to-use graphical user interface(GUI) to manage and monitor these tasks.
This documentation will show the project's fully functional password cracker that efficiently handles and cracks passwords for different file types using various attack methods.

#### Executive Summary
The Password Cracker is a software tool designed to recover passwords by trying different combinations until the correct one is found. It uses various methods like ***brute force***, ***dictionary attacks***, and ***reverse brute force attacks*** to crack passwords for different types of files and systems.
This tool is a **hybrid** (CPU & GUP) for faster processing.

#### Project Analysis and Workings

I plan on using this project tool to test and improve the security of systems and files. This will help identify weak passwords and vulnerabilities, allowing organizations to strengthen their security measures.

#### Recommendations

###### Advantages
Password Crackers are used by cybersecurity professionals to audit system security, recover lost passwords, and conduct penetration testing. They help improve security protocols and protect sensitive information

###### Disadvantages

The unethical use include unauthorized access to systems, stealing sensitive information, and conducting illegal activities. It is important to use password cracking tools responsibly and within legal boundaries.

#### Password Attacks Methodology

**Brute Force Attack**
This attack systematically tries all possible password combinations until the correct one is found. It is time-consuming but effective for shorter passwords or less complex combinations.

**Dictionary Attack**
This attack uses a list of common passwords or previously breached passwords. It is faster than brute force attacks but reliess on the passwords being in the list.

**Reverse Brute Force Attack**
This attack uses a common password against a list of potential usernames. It targets accounts where the same password might be used, exploitingn weak password practices.

**PROJECT TARGET FILE TYPES**

* Zip Files
* Pdf Files
* Excel Fike

**PACKAGE REQUIREMENTS**
msoffcrypto-tool==4.12.0
pyzipper==0.3.5
PyPDF2==3.0.1
colorama==0.4.6
tqdm==4.65.0
tabulate==0.8.9
requests==2.28.1
Pillow==9.4.0
tk==0.1.0
