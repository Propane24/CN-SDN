# CN-SDN

SDN-Based Firewall using Mininet and Ryu

Problem Statement
The objective of this project is to design and implement a Software Defined Networking (SDN) based firewall using Mininet and a Ryu controller. The firewall controls network traffic between hosts using rule-based filtering. The controller handles packet_in events, applies match + action rules, and decides whether to allow or block traffic.
Objective
Implement controller-switch interaction using OpenFlow
Design and install flow rules dynamically
Demonstrate firewall behavior (allowed vs blocked traffic)
Observe network behavior using Mininet
Tools & Technologies Used
Mininet (Network Emulator)
Ryu Controller (SDN Controller)
Open vSwitch
Python
Network Topology

h1 ---|
h2 ---|--- s1 (switch)
h3 ---|

1 switch (s1)
3 hosts (h1, h2, h3)

IP Addresses:

h1 → 10.0.0.1
h2 → 10.0.0.2
h3 → 10.0.0.3
Setup Instructions

Step 1: Install Dependencies
Run the following commands in Ubuntu terminal:
sudo apt update
sudo apt install mininet openvswitch-switch python3-pip -y
pip3 install ryu

Step 2: Clone Repository
git clone <your-repo-link>
cd sdn-firewall-mininet

Execution Steps

Terminal 1: Start Ryu Controller
ryu-manager firewall.py

Terminal 2: Run Mininet
sudo mn --topo single,3 --controller remote

Firewall Logic

The controller implements rule-based filtering.

Blocked Rule:
Traffic from 10.0.0.1 (h1) to 10.0.0.3 (h3) is blocked.

Allowed Rule:
All other traffic is allowed.

Implementation details:

Packet inspection using IPv4 headers
Matching based on source and destination IP
Drop rule implemented by ignoring packet
Allowed traffic is forwarded normally
Test Scenarios

Test Case 1: Allowed Traffic
Command: h1 ping h2
Expected Result: Successful ping with 0% packet loss

Test Case 2: Blocked Traffic
Command: h1 ping h3
Expected Result: Ping fails (packets dropped)

Test Case 3: Reverse Traffic
Command: h3 ping h1
Expected Result: May succeed depending on rule direction

Validation & Verification

Connectivity Test
Command: pingall
Expected:

h1 ↔ h2 → success
h1 ↔ h3 → failure

Flow Table Inspection
Command: sudo ovs-ofctl dump-flows s1
Observe installed flow rules and actions

Controller Logs
The controller prints logs such as:
BLOCKED: 10.0.0.1 -> 10.0.0.3
This confirms firewall behavior

Performance Observation

Latency Test
Command: h1 ping h2
Measure round-trip time

Throughput Test (optional)
Command: iperf
Used to measure bandwidth between hosts

Cleanup

Before rerunning Mininet:
sudo mn -c

Features Implemented
Controller-based firewall
IP-based filtering
Packet inspection
Flow rule installation
Logging of blocked traffic
Test scenario validation
Expected Output
Successful communication between allowed hosts
Blocked communication between restricted hosts
Controller logs showing blocked packets
Flow rules visible in switch
Conclusion

This project demonstrates how SDN enables centralized control of network traffic using a controller. By implementing a firewall at the controller level, flexible and dynamic traffic filtering is achieved using OpenFlow rules.

References
https://mininet.org/overview/
https://mininet.org/walkthrough/
https://github.com/mininet/mininet
Ryu Documentation
Author

Name: Your Name
Course: Computer Networks
Project: SDN Firewall using Mininet
