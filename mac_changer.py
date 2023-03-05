import subprocess
import optparse
import re

# A function to get user inputs
def getInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!") # An argument for the user to enter which interface to change.
    parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adress") # An argument for the user to enter the new MAC address.
    return parse_object.parse_args()

# A function to change the MAC address
def macChange(userInterface,userMac):
    subprocess.call(["ifconfig",userInterface,"down"]) # First, we put the relevant interface in a closed position.
    subprocess.call(["ifconfig",userInterface,"hw","ether",userMac]) # We change the MAC address.
    subprocess.call(["ifconfig",userInterface,"up"]) # We re-open the relevant interface.

# A function to check if the MAC address has been changed
def controlMac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface]) # We get the configuration information of the relevant interface.
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) # We search for the relevant expression to extract the MAC address.
    if newMac:
        return newMac.group(0) # We return the MAC address.
    else:
        return None

# A message indicating the start of the program is printed.
print("myMacChanger started")

# We get the user inputs.
(userInput,arguments) = getInput()

# We change the MAC address of the desired interface.
macChange(userInput.interface,userInput.mac_adress)

# We check the final MAC address to see if it has been changed or not.
finalMac = controlMac(str(userInput.interface))

# If the operation is successful, "Success!" is printed. Otherwise, "Error!" is printed.
if finalMac == userInput.mac_adress:
    print("Success!")
else:
    print("Error!")
