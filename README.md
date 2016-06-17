# ZenPacks.community.BrocadeSW

#Description
The ZenPacks.community.BrocadeSW ZenPack monitors Brocade Storage Switches.

Tested on next models:

1.SN6000B 16Gb 48-port/24-port Active Power Pack+ Fibre Channel Switch

2.HP 8/8 Base (0) e-port SAN Switch

3.HP 8/40 SAN Switch Power Pack+

4.HP StorageWorks 4/16 SAN Switch

5.HP StorageWorks SAN Switch 2/8V

and next firmware:

-v7.2.1d

-v7.0.2a

-v5.3.2c

-v5.3.2b


#Features

Overview:

    -Firmware Version
    -Seial Number
    -Device Title
Graphs:

    -CPU (if supported)
    -Memory (if supported)

Components:

    -Sensors:
        -Temperature
        -Fan
        -Power Supply
    -FC Port (many port properties see screenshot Copmonents_FCPorts2.png)
Events:

    -Status change of device and all components (with auto clear)
    -Perfomance threshold
        -Max usage
        -Errors

# Screenshots
See the screenshots directory.

#Device Support
This ZenPack only requires very basic Unix commands on the target devices.

#Requirements & Dependencies
Zenoss Versions Supported: 4.x
Python libriry binascii

#ZenPack installation
This ZenPack can be installed from the .egg file using either the GUI or the zenpack command line.
zenpack --install ZenPacks.community.BrocadeSW
Restart zenoss after installation.

#TODO
1. Default sort FC port by number
2. Get device model
3. SAN Fabric Information and monitoring
