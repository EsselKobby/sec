#! python3 
# pwlock.py - A password locker program.

# Import of Python Modules
import sys
import pyperclip


#Program Design and Data Structures
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'freefood': '12345'} 


# Needed requirement for the account name
if len(sys.argv) < 2:
    print('Usage: python pwlock.py [account] - copy account password')
    sys.exit()

# Command line argument assignment
account = sys.argv[1] 

# Account Checkup in PASSWORDS dictionary

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account +' copied to clipboard')
else:
    print('There is no account named '+ account)

