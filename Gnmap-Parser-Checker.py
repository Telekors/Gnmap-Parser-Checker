"""
 ██████╗ ███╗   ██╗███╗   ███╗ █████╗ ██████╗     ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗██╔██╗ ██║██╔████╔██║███████║██████╔╝    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Usage:
    Gnmap-Parser-Checker.py (-k FILE -s FILE -m FILE) [-o FILE]
    Gnmap-Parser-Checker.py scan (-k FILE -s FILE -m FILE) [-o FILE]

Options:
    -h, --help             Prints this Message
    -s FILE, --scope=FILE  Initial Nmap Scope File (-iL)
    -k FILE, --key=FILE    Shodan API Key File
    -m FILE, --matrix=FILE TCP-Services-Matrix.csv File
    -o FILE, --output=FILE Your output file location
"""

#Created by: [Telekors] - https://github.com/Telekors

#Credit: 
#    [KyleEvers] - https://github.com/KyleEvers (Thanks for showing me the light of docopt)
#    [jasonjfrank] - https://github.com/jasonjfrank/gnmap-parser (Creator of gnmap-parser)



from shodan import Shodan
from netaddr import IPNetwork
from docopt import docopt
import sys
import socket

def main(scope_file, tcp_services_file, api_file, outfile):
        missing = []
        f = open(api_file,"r")
        apikey = (f.read())
        f.close()
        api = Shodan(str(apikey.strip()))
        scope = open(scope_file,"r")
        for scope_line in scope:
                try:
                       IPNetwork(str(scope_line))
                except:
                        error = (str(scope_line) + ": ", sys.exc_info()[1])
                        debug_print(error)
                        continue
                for ip in IPNetwork(str(scope_line)):
                        try:
                                ipinfo = api.host(str(ip))
                        except:
                                error = (str(ip) + ": ", sys.exc_info()[1])
                                debug_print(error)
                                continue
                        host_print(ipinfo)
                        for port in ipinfo['ports']:
                                full_string = (str(port) + ",TCP," + str(ip))
                                debug_print (full_string)
                                with open(tcp_services_file, "r+") as file:
                                        for line in file:
                                                if full_string in line:
                                                        debug_print ("match")
                                                        break
                                        else:
                                            if arguments["scan"] is True:
                                                if (nmap_scan(str(ip),str(port))) is True:
                                                    missing.append(str(ip) + "," + str(port))
                                            else:
                                                missing.append(str(ip) + "," + str(port))

        print ("Your matrix file is missing: ")
        print ("=============================")
        print("IP, Port")
        for ip_port in missing:
            print (ip_port)

        if outfile is not None:
            f = open(outfile, "w")
            f.write("IP Address, Port\n")
            for ip_port in missing:
                f.write(ip_port + "\n")
            f.close()


def nmap_scan(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip,int(port)))
    if result ==0:
        s.close()
        return True
    s.close()
    return False

def debug_print(input):
        #print(input)
        x = 1

def host_print(ipinfo):
        debug_print(ipinfo['ip_str'] + ": " + "".join(str(ipinfo['ports'])))


if __name__ == "__main__":
        arguments = docopt(__doc__, version='Gnmap Parser Checker 1.0')
        main(arguments["--scope"], arguments["--matrix"], arguments["--key"], arguments["--output"])
