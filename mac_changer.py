import subprocess
import optparse
import re

def getInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adress")
    return parse_object.parse_args()

def macChange(userInterface,userMac):
    subprocess.call(["ifconfig",userInterface,"down"])
    subprocess.call(["ifconfig",userInterface,"hw","ether",userMac])
    subprocess.call(["ifconfig",userInterface,"up"])

def controlMac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if newMac:
        return newMac.group(0)
    else:
        return None


print("myMacChanger started")
(userInput,arguments) = getInput()
macChange(userInput.interface,userInput.mac_adress)
finalMac = controlMac(str(userInput.interface))

if finalMac == userInput.mac_adress:
    print("Success!")
else:
    print("Error!")