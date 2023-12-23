#improved version with variables
#!/user/bin/env python
import subprocess

#creating vars
interface = "eth0"
new_mac_address = "00:11:22:11:11:11"

#adding a print statement for the visual comm

print("Changing the MAC address of interface " + interface + "to " + new_mac_address)
subprocess.call("ifconfig "+interface+ " down", shell=True)
subprocess.call("ifconfig "+interface+ " hw ether" +new_mac_address, shell=True)
subprocess.call("ifconfig " +interface +" up", shell=True)
