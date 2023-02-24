# mac_changer
You can follow these steps to run this Python script:

Open this script in a text editor and save it (e.g. save it as "macchanger.py").

Open the command prompt and navigate to the directory where the script is located.

Use the following command to run the script:

python macchanger.py -i [interface] -m [new_mac_address]

Here, [interface] represents the network interface to be changed, and [new_mac_address] represents the new MAC address to be set.

For example, for a sample with network interface "eth0" and new MAC address "00:11:22:33:44:55", the command would be:

python macchanger.py -i eth0 -m 00:11:22:33:44:55

After running the script, the program will shut down the network interface, change the MAC address, and then bring the network interface back up. Finally, the changed MAC address is checked, and if the process is successful, "Success!" will be printed; otherwise, "Error!" will be printed.
