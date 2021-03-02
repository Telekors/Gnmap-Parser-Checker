# Gnmap-Parser-Checker

## About
This is a simple script designed to be used alongside [jasonjfranks] Gnmap-Parser.sh script `https://github.com/jasonjfrank/gnmap-parser`. This script will check to see if shodan sees any hosts in your scope that have open ports that you might have missed during your nmap enumeration.

## Install
1. Clone into directory: `https://github.com/Telekors/Gnmap-Parser-Checker.git`
2. Install Requirements: `pip install -r requirements.txt`
3. Open python file and insert Shodan API Key

## Usage:
`Gnmap-Parser-Checker.py (-k FILE -s FILE -m FILE) [-o FILE]`
`Gnmap-Parser-Checker.py scan (-k FILE -s FILE -m FILE) [-o FILE]`

## Options:
* -h, --help             Prints this Message
* -s FILE, --scope=FILE  Initial Nmap Scope File (-iL)
* -k FILE, --key=FILE    Shodan API Key File
* -m FILE, --matrix=FILE TCP-Services-Matrix.csv File
* -o FILE, --output=FILE Your output file location

## Credit: 
* [KyleEvers] - https://github.com/KyleEvers (Thanks for showing me the light of docopt)
* [jasonjfrank] - https://github.com/jasonjfrank/gnmap-parser (Creator of gnmap-parser)

## Created by: [Telekors] - https://github.com/Telekors

## Credit: 
* [KyleEvers] - https://github.com/KyleEvers (Thanks for showing me the light of docopt)
* [jasonjfrank] - https://github.com/jasonjfrank/gnmap-parser (Creator of gnmap-parser)
