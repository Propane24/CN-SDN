# SDN-Based Firewall using Mininet and Ryu

## 1. Problem Statement

The objective of this project is to design and implement a Software Defined Networking (SDN) based firewall using Mininet and a Ryu controller. The firewall controls network traffic between hosts using rule-based filtering.

The controller must:
- Handle packet_in events  
- Apply match + action flow rules  
- Block or allow traffic based on predefined conditions  

---

## 2. Objective

- Implement controller-switch interaction using OpenFlow  
- Design and install flow rules dynamically  
- Demonstrate firewall behavior (allowed vs blocked traffic)  
- Observe network behavior using Mininet tools  

---

## 3. Tools & Technologies Used

- Mininet (Network Emulator)  
- Ryu Controller (SDN Controller)  
- Open vSwitch  
- Python  

---

## 4. Network Topology

A simple topology is used:

h1 ---|  
h2 ---|--- s1 (switch)  
h3 ---|  

- 1 switch (s1)  
- 3 hosts (h1, h2, h3)  

IP Addresses:
- h1 → 10.0.0.1  
- h2 → 10.0.0.2  
- h3 → 10.0.0.3  

---

## 5. Setup Instructions

### Step 1: Install Dependencies

sudo apt update  
sudo apt install mininet openvswitch-switch python3-pip -y  
pip3 install ryu  

### Step 2: Clone Repository

git clone <your-repo-link>  
cd sdn-firewall-mininet  

---

## 6. Execution Steps

### Terminal 1: Start Ryu Controller

ryu-manager firewall.py  

### Terminal 2: Run Mininet

sudo mn --topo single,3 --controller remote  

---

## 7. Firewall Logic

The controller implements rule-based filtering:

### Block Rule
Traffic from 10.0.0.1 (h1) to 10.0.0.3 (h3) is dropped  

### Allow Rule
All other traffic is allowed  

### Implementation Details
- Packet inspection using IPv4 headers  
- Matching based on source and destination IP  
- Drop rule implemented by ignoring packet (no action)  
- Allowed traffic is forwarded (flooded)  

---

## 8. Test Scenarios

### Test Case 1: Allowed Traffic

h1 ping h2  

Expected Result:
- Ping successful  
- 0% packet loss  

### Test Case 2: Blocked Traffic

h1 ping h3  

Expected Result:
- Ping fails  
- Packets dropped  

### Test Case 3: Reverse Traffic

h3 ping h1  

Expected Result:
- May succeed (depending on rule direction)  

---

## 9. Validation & Verification

### Connectivity Test

pingall  

Expected:
- h1 ↔ h2 → success  
- h1 ↔ h3 → failure  

### Flow Table Inspection

sudo ovs-ofctl dump-flows s1  

Observe:
- Installed flow rules  
- Match conditions  
- Actions  

### Controller Logs

BLOCKED: 10.0.0.1 -> 10.0.0.3  

---

## 10. Performance Observation

### Latency Test

h1 ping h2  

Measure:
- Round trip time (RTT)  

### Throughput Test (Optional)

iperf  

---

## 11. Cleanup

sudo mn -c  

---

## 12. Features Implemented

- Controller-based firewall  
- IP-based filtering  
- Packet inspection  
- Flow rule installation  
- Logging of blocked traffic  
- Test scenario validation  

---

## 13. Expected Output

- Successful communication between allowed hosts  
- Blocked communication for restricted pairs  
- Controller logs showing blocked packets  
- Flow rules visible in switch  

---

## 14. Conclusion

This project demonstrates how SDN enables centralized control of network traffic using a controller. By implementing a firewall at the controller level, dynamic and flexible traffic filtering is achieved using OpenFlow rules.  

---

## 15. References

- https://mininet.org/overview/  
- https://mininet.org/walkthrough/  
- https://github.com/mininet/mininet  
- Ryu Documentation  

---

## 16. Author

Name: Pravith Mohandas 
Course: Computer Networks  
Project: SDN Based Firewall 
