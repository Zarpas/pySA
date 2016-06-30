from termcolor import colored
import subprocess
import os
import sys

man_lines = ['.\\" Manpage for pySA.\n', '.\\" Contact https://gitter.im/pySA-dev for help.\n', '.TH man 1 "27 June 2016" "0.0.1" "pySA man page"\n', '.SH NAME\n', 'pySA \\- a commandline tool for structural analysis\n', '.SH SYNOPSIS\n', 'pySA [flag]=[INPUT]\n', '.SH DESCRIPTION\n', 'pySA aims at making structural analysis of a beam easy by giving a detailed desription on how to solve for Shear Force and Bending Moment diagrams.\n', '.SH OPTIONS\n', '.PP\n', '-l: span of the beam\n', '.PP\n', '-p: point loads on the beam.\n', '.PP\n', '-u: uniformly distributed loads on the beams.\n', '.PP\n', '-s: supports on the beam (Use 2 pin or 1 fixed supports).\n', '.PP\n', '-f: To take input from a file (Use 2 pin or 1 fixed supports).\n', '.SH EXAMPLES\n', 'Check out examples at https://github.com/pySA-dev/pySA/wiki/Examples\n', '.SH BUGS\n', 'Please report any bugs at https://github.com/pySA-dev/pySA/issues\n', '.SH AUTHOR\n', 'Sri Sanketh Uppalapati(iamjustice443@gmail.com)\n', '.SH COPYRIGHT\n', 'MIT License\n', 'Copyright (c) 2016 Sri Sanketh Uppalapati\n', 'https://github.com/pySA-dev/pySA/blob/master/LICENSE.txt\n']

def generate_page(file_name, lines):

    f = open(file_name, 'w')
    f.writelines(lines)

def delete_page(file_name):

    os.remove(file_name)

def main():

    try:
        if(sys.argv[1]=='install'):
            generate_page('pySA', man_lines)
            subprocess.call("sudo python3 setup.py install", shell=True)
            subprocess.call("sudo cp pySA /usr/share/man/man1/pySA.1", shell=True)
            subprocess.call("sudo gzip /usr/share/man/man1/pySA.1", shell=True)
            delete_page('pySA')
        elif(sys.argv[1]=='uninstall'):
            subprocess.call("sudo rm -rf /usr/local/bin/pySA", shell=True)
            subprocess.call("sudo rm -rf /usr/share/man/man1/pySA.1.gz", shell=True)

    except:
        print(colored('Enter valid arguments', 'red'))
        print(colored('Valid arguments:', 'red'))
        print(colored('1. install - To install pySA package', 'red'))
        print(colored('2. uninstall - To uninstall pySA package', 'red'))

main()
