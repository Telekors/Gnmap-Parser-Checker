from shodan import Shodan
from netaddr import IPNetwork
import sys

def main(scope_file, tcp_services_file):
api = Shodan('<API KEY GOES HERE>')
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
                       full_string = (str(ip) + ",TCP," + str(port))
                       debug_print (full_string)
                       with open(tcp_services_file, "r+") as file:
                               for line in file:
                                       if full_string in line:
                                               debug_print ("match")
                                               break
                               else:
                                       print (full_string + " - Missing")

def debug_print(input):
        #print(input)
        x = 1

def host_print(ipinfo):
        debug_print(ipinfo['ip_str'] + ": " + "".join(str(ipinfo['ports'])))

if __name__ == "__main__":
try:
scope_file = sys.argv[1].strip()
tcp_services_file = sys.argv[2].strip()
except IndexError:
print "Check My Work! (Scope File is single ip or cidr range per line)"
print "[-] Usage: %s </Full_Path/To_Scope> </Full_Path/Parsed-Results/Port-Matrix/TCP-Services-Matrix.csv>"
sys.exit()
main(scope_file, tcp_services_file)
