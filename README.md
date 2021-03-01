# Gnmap-Parser-Checker

## About
This is a simple script designed to be used alongside [jasonjfranks] Gnmap-Parser.sh script `https://github.com/jasonjfrank/gnmap-parser`. This script will check to see if shodan sees any hosts in your scope have open ports that you might have missed during your nmap enumeration.

## Install
1. Clone into directory: `https://github.com/Telekors/Gnmap-Parser-Checker.git`
2. Install Requirements: `pip install -r requirements.txt`
3. Open python file and insert Shodan API Key

## Run
* `python Gnmap-Parser-Checker.py <Path_To_Scope> <Path_To_Port-Matrix.csv>`
