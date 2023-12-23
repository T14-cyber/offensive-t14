#!/user/bin/env python
import subprocess
import optparse

reader = optparse.OptionParser()

reader.add_option("-i", "--interface", dest="interface", help="interface name")

#creating vars
#getting input from the user
interface = input("Enter the interface name: ")
new_mac_address = input("Enter the new MAC address: ")

#adding a print statement for the visual comm

print("Changing the MAC address of interface " + interface + "to " + new_mac_address)
#protecting from vulnerabilities. dafely handle the user input
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
subprocess.call(["ifconfig",interface,"up"])

