#write script to change a MAC address
#!/user/bin/env python

import subprocess
#step 1 check out your mac by ifconfig eth0
#ifconfig eth0 down ( for that we need to import subprocess)
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:01:23:45", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
