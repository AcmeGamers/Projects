Host Names
==========
Int_Router
Internet 
Ext_Router
MAP KEY  = present11

Passwords
=========
IPS      = re-assure22
Internet = Database11
External = Security33
MAP KEY  = wento
#########################
## To re-write password:
## ---------------------
## enable password Manik
## do write memory
#########################

www.google.com
192.168.50.4
########################
CODE
enable secret Security33
########################

https://newbedev.com/shell-dhcp-router-without-dhcp-server-packet-tracer-code-example

# part 1:
# 24 = 255.255.255.0
## switch 0 = Finance DMZ Network = 192.168.50.0/24
## switch 3 = Internal Network    = 192.168.30.0/24 
## switch 5 = External Site Net   = 192.168.40.0/24
## switch 4 = Public Netwrok      = 192.168.60.0/24


our ips:
Internal Network    = 192.168.30.0/24 (24 = 255.255.255.0)
External Site Net   = 192.168.40.0/24
Finance DMZ Network = 192.168.50.0/24
Public Netwrok      = 192.168.60.0/24



Conencting three Servers
=========================
HWIC-2T port for server cables


Creating DHCP Server
====================
Steps:
# Creating Network Topology
## The topology contains fast ethernet connection from router, switch, and pc
# Giving Clients DHCP configuration from IP address.
# Configuring the router now.
### Open Routers > CLI

### Open Routers > CLI
#### This method will assign the first pool to the switches which will assign ip to clients
#### Switch 3 (Internal Network = IN)
ip dhcp pool Internal
network 192.168.30.0 255.255.255.0
default-router 192.168.30.1
exit

#### This method will assign the second pool to the switches which will assign ip to clients
#### Switch 0 (Finance DMZ Network = FN)
ip dhcp pool Finance
network 192.168.50.0 255.255.255.0
default-router 192.168.50.1
exit

### Open Routers > Config > FastEthernet 0/0
IP address  > 192.168.30.1
Subnet Mask > 255.255.255.0
CLI > no shut
CLI > exit


### Open Routers > Config > FastEthernet 1/0
IP address  > 192.168.50.1
Subnet Mask > 255.255.255.0
CLI > no shut
CLI > exit

## External Site Net = 192.168.40.0/24
ip dhcp pool External
network 192.168.40.0 255.255.255.0
default-router 192.168.40.1
exit

## Internet = 192.168.60.0/24
ip dhcp pool Public
network 192.168.60.0 255.255.255.0
default-router 192.168.60.1
exit


### Putting Clients IP to Dynamic
### DHCP server == Complete!



DNS Server
==========
# Configure DHCP Server
Server DHCP > Desktop >  IP Configuration > Static

ip address      > 192.168.50.3
Subnet Mask     > 255.255.255.0
Default Gateway > 192.168.50.1
DNS Server      > 192.168.50.4


Server DHCP > Services > DHCP 
Service: On

Pool Name       > Server Pool
Default Gateway > 192.168.50.1
DNS Server      > 192.168.50.4
Static IP addre > 192.168.50.10
# Save  

Pool Name       > Server Pool v2
Default Gateway > 192.168.30.1
DNS Server      > 192.168.50.4
Static IP addre > 192.168.30.10
# Add

# All Clients > IP Configuration > Dynamic IP


Configuring DNS 
---------------
DNS Server > Desktop > IP configuration > Interface > Static

ip address      > 192.168.50.4
Subnet Mask     > 255.255.255.0
Default Gateway > 192.168.50.1
DNS Server      > 192.168.50.4

Server DHCP > Services > DHCP 
DNS Service: ON

DNS Server > Service > DNS
Resource Records > Name > www.dns.com
Resource Records > Address > 192.168.50.3 # address of webserver
# Add Record


# Open a client system > ip configuration > wait for the DNS to assign 
# (switch from dynamic to static) > once done > Web Browser > 10.0.0.2
# Or you can also use www.google.com instead of 10.0.0.2 



Web Server
==========
# Creating Topology with three servers, dns, dhcp, web  

Server WEB > IP configuration > Interface > Static

ip address      > 192.168.50.3
Subnet Mask     > 255.255.255.0
Default Gateway > 192.168.50.1
DNS Server      > 192.168.50.4

Server WEB > Services > HTTP > index.html (Contains Webpage)
# Change a few elements
Server DNS > Services > DNS > resource records > Name > www.google.com
Server DNS > Services > DNS > resource records > address > 192.168.50.3



Sys Log
=======
# Step 1: Creating Links
en (enable)
conf t (configure terminal)
#int (interface)
#interface fas (fastEthernet)
#interface fastEthernet 6/0
#no shut (shutdown)

#ip add (address) 192.168.30.3 255.0.0.0  #syslog address
#no shut (shutdown) 
#ex 
## Links are now up

# Step 2: Assign IP on syslog server
Syslog > IP configuration > Interface > Static

ip address      > 192.168.30.4 #Syslog Ip
Subnet Mask     > 255.255.255.0
Default Gateway > 192.168.30.1
DNS Server      > 192.168.50.4
# Checking connectivity

ex
ping 192.168.30.3

# Step 3: Configuration of Syslog Server
Router > CLI
config t 
logg (logging)
logging 192.168.30.4
logging trap
logging trap deb (debugging)
logging trap debugging
ex
ping 192.168.30.4

Server Web > Services > Syslog
Service Turn Off > then on


# Shutting down server to check the logs 
conf 
configure t
configure terminal
int
interface
interface fas
interface fastEthernet 0/0
shut
shutdown

Server Web > Services > Syslog
no shut
no shutdown



Configuring RIPv2
=================
# Router > CLI
router rip
version 2
network 192.168.30.0  
network 192.168.50.0 
network 192.168.70.0 
# PORT Where Routers are connected
ip address 192.168.70.1 255.255.255.252

# Router2 > CLI
router rip
version 2
network 192.168.40.0  
network 192.168.70.0  
ip address 192.168.70.4 255.255.255.252

# Router2 > CLI
router rip
version 2
network 192.168.60.0  
network 192.168.70.0  

## Doing it from both sides of the router will do the trick



Configuring VLANs and Trunks
============================
# Connecting all clusters / computers with switches
# main switch > CLI
config t

# Create VLANs
vlan 70
name Admin_PC
exit 

vlan 71
name Area_1
exit 

vlan 72
name Area_2
exit 

ctrl + z # to go to start, switch#
copy running-config startup-config
*press "enter", no need to set a name.
show vlan brief

# Set this up in all the trunks (switches, connected with the main switch to form a vlan)


# Assingning ports to VLANs
## Switch0 > CLI (main / parent switch)
# int range {port range} # switchport mode ?  # Help command # int range {port range}
config t
int range fa0/8-13
switchport mode access
switchport access vlan 71

int range fa0/14-19
switchport mode access
switchport access vlan 72

int fa0/20
switchport mode access
switchport access vlan 70
end

show vlan brief


# Making Trunks # where switches are configured # Default vlan if no label is found in the packets.
config t
int range fa0/4-5
switchport mode trunk
switchport trunk native vlan 70

int fa0/3
switchport mode trunk
switchport trunk native vlan 70 

show int trunk


## Switch1 > CLI (child switch)
en
show vlan brief
config t
#int fa0/1
#switchport mode trunk
#switchport trunk native vlan 90
#end

config t # int range {port range} # switchport mode ?  # Help command  # int range {port range}
int range fa0/8-13
switchport mode access
switchport access vlan 71

int range fa0/14-19
switchport mode access
switchport access vlan 72

int fa0/20
switchport mode access
switchport access vlan 70
end

show vlan brief

conf t
int fa0/20
switchport acess vlan 70
ctrl + z

show vlan brief
show int trunk

## Switch2 > CLI (child switch)
// Same Steps as above //



#### Only if required to remove
Removing VLANS
==============
If you have the following ports
==============
1   > 1,23,24   # Vlan 
192 > 3,4,5,6   # Brief
==============
First, assign the default VLAN 1 to ports 3 though 6 as shown below.

interface range fastEThernet 0/3-6
switchport access vlan 1
exit

Next, delete the vlan itself as shown below.

no vlan 192

It will delete that vlan



Inter VLAN Routing Configuration
=================================
# Create a new router
en  
conf t
int fa0/0 # Where router is configuered with the switch
no shut

conft t
int fa0/0.1
encapsulation dot1q 21
ip address 192.168.30.1 255.255.255.0
no shut

int fa0/0.2
encapsulation dot1q 23
ip address 192.168.50.1 255.255.255.0
no shut
end

ctrl + z
show run
show ip route


ACL Standard (Giving the permission to allow and not allow IP Address)
============
# Steps
## Creating an access list, list of ips that can(not) access a cretain area.
## Implement the access list on the interface (inbound or outbond) == Sending / recieving


# Firstly configuring where the ACL should take place.
## if recieving data from two computers, the router that will be reciveing the message should be configured as the ACL port, outbond/back port from the which the message from the destination will go to block the message.
## If sending data to computers/router, the recieveing message router outbond should be configured for the ACL.

config t                                # 1 = standard ACL && 100 = extended ACL "Value below this line" 
access-list 1 deny host 192.168.60.8    ## access-list 1 deny 192.168.60.0 0.0.0.255 ## alt method # ip address of the computer where 0.0.0.0 = blocking one host || Blocking entire network = 0.0.0.255 && network = 192.168.2.0
access-list 1 premit any                # allowing any other ip to contact
ctrl + z
show run
 
#int vlan 1005
#ip access-group 1 out
 # out bond wire from router connecting to switch
int fa0/0
ip access-group 1 out

############
## Deleting access list if needed to delete, not required in my project
conf t
no access-list 1  # numeber of access list in Standard ACL 
no ip access-group 1 out # router outbound
show run

## Turning off ACL
conf t
int fa0/1 
no ip access-group 99 out
ctrl + z
show run 

####################    
## Extra information
####################
standarad acl (1-99): (applied closest to the destination) # destination = pc/server under different router
denies or premits source ip address 

Extended ACL (100-199): (applied closest to the source)  # source = pc/server under same router
denies or premits source IP address
denies or premits destination IP address
denies or premits port (service)

## During denying or premitting host
more specific statements should be at the top
more geenral statmenets should be at the bottom
if premit any isn't defined, all packets will be blocked naturally through a hidden (implicit work) called access-list 1 deny host any
####################


Site-to-Site IPsec 
==================
# IP Routing
adding routes on the two routers (other than the ISP)
## Internal Router Address
ip route 0.0.0.0 0.0.0.0 192.168.70.2
## External Router Address
ip route 0.0.0.0 0.0.0.0 192.168.70.6
# Once IP routing is done on both, cofigure ISP = internet (connecting both routes)

config t
# Internal Router
ip route 192.168.30.0 255.255.255.252 192.168.70.1 #address of fastEThernet cable 0 && where 192.168.70.4 = address of router 1
ip route 192.168.50.0 255.255.255.252 192.168.70.1 #address of fastEThernet cable 1 && where 192.168.70.4 = address of router 1
# External Router
ip route 192.168.40.0 255.255.255.0 192.168.70.4   #address of fastEThernet cable 1 && where 192.168.70.4 = address of router 2


# Configuring The "two routes" for ISP (Internet)
# Configure ISAKMP Policy to establish the IKE (Internet Key Exchange)
## Setting up the key
config t
crypto isakmp enable
crypto isakmp policy 20
authentication pre-share
encryption 3des
hash md5
group 1
lifetime 5600
exit


# router 1
crypto isakmp key present11 address 192.168.70.4 # address of the other router where "cisco123" is a key, you can put anything here
# router 2
crypto isakmp key present11 address 192.168.70.1



# Create Accses list
## Router 1
access-list 100 permit ip 192.168.30.0 0.0.0.255 192.168.40.0 0.0.0.255
access-list 100 permit ip 192.168.50.0 0.0.0.255 192.168.40.0 0.0.0.255
## Router 2
access-list 100 permit ip 192.168.40.0 0.0.0.255 192.168.30.0 0.0.0.255 
access-list 100 permit ip 192.168.40.0 0.0.0.255 192.168.50.0 0.0.0.255 


# Defining ISPEC Transform Set
## Types of encryption
## Router 1
config t
#IPS--ExternalRouter = anything ya wanna type
crypto ipsec transform-set int_network__ext_network esp-3des esp-md5-hmac 
## Router 2
config t
#ExternalRouter--IPS = anything ya wanna type
crypto ipsec transform-set ext_network__int_network esp-3des esp-md5-hmac 


# Create Crypto map for IPsec
# Router 1
config t
crypto map FOR_IPSEC 20 ipsec-isakmp
set peer 192.168.70.4 
set pfs group1
set transform-set int_network__ext_network
match address 100
exit

# Router 2
config t
crypto map FOR_IPSEC 20 ipsec-isakmp
set peer 192.168.70.1 
set pfs group1
set transform-set ext_network__int_network
match address 100
exit


# Applying Crypto Map
## apply the crypto map to the outgoing interface of the vpn device
### Router 1
int f0/0
crypto map FOR_IPSEC
exit
# crypto map IPS--ExternalRouter

int fa0/1
crypto map FOR_IPSEC
exit

### Router 2
int fa0/0
crypto map FOR_IPSEC

   
# Testing and Verify VPN
exit (start when dev en)
show crypto ipsec sa
show crypto isakmp policy
show crypto map


IOS IPS (Intrusion Prevention System)
=======

# Enabling IOS IPS
show version
## Syslog Router 
# Creating Directory
(no conf t)
mkdir log_dir
conf t
# Making it the default directory for IPS location logs
ip ips config location log_dir
ip ips ? 
# creating and naming the rule "iosips"
ip ips name iosips 
# Retiring all signature categories and unretiring the IOS IPS basic categories
ip ips signature-category 

category ?
category all
retire true
exit
category ios_ips basic 
retire false 
exit
exit
confirm


interface fa0/0 {port numeber} #Outbound or backport of syslog router of
ip ips ?
ip ips iosips out  # using the name from code 6 (starting IOSIPS)
exit

logging host 192.168.30.4
service timestamps log datetime msec


# Modifying the signature 
config t
ip ips signature-definition
? 
signature 2004 0
? 
status ?
status 
retired false 
enabled true
exit 

{config-sigdf-sig}#engine
engine
?
event-action ? 
event-action produce-alert 
event-action deny-packet-inline
exit 
exit 
exit 

do show ip ips all 

# One network configured for syslog should be able to ping, but not the other network that got pinged.
## Syslog will now contain some information upon pinging hosts of the syslog network