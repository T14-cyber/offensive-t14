#!/user/bin/env python
import subprocess
import optparse

reader = optparse.OptionParser()

reader.add_option("-i", "--interface", dest="interface", help="interface name")
reader.add_option("-m", "--mac", dest="new_mac_address", help="New Mac Address")
(values, keys)= reader.parse_args()
#creating vars
#getting input from the user
interface = values.interface
new_mac_address =  values.new_mac_address
#adding a print statement for the visual comm

print("Changing the MAC address of interface " + interface + "to " + new_mac_address)
#protecting from vulnerabilities. dafely handle the user input
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
subprocess.call(["ifconfig",interface,"up"])

