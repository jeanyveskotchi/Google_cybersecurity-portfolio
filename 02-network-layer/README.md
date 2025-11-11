# Network Layer Communication — DNS/ICMP Troubleshooting

**Scenario**
You are a cybersecurity analyst working at a company that specializes in providing IT services for clients. Several customers of clients reported that they were not able to access the client company website www.yummyrecipesforme.com, and saw the error “destination port unreachable” after waiting for the page to load. 
You are tasked with analyzing the situation and determining which network protocol was affected during this incident. To start, you attempt to visit the website and you also receive the error “destination port unreachable.” To troubleshoot the issue, you load your network analyzer tool, tcpdump, and attempt to load the webpage again. To load the webpage, your browser sends a query to a DNS server via the UDP protocol to retrieve the IP address for the website's domain name; this is part of the DNS protocol. Your browser then uses this IP address as the destination IP for sending an HTTPS request to the web server to display the webpage .The analyzer shows that when you send UDP packets to the DNS server, you receive ICMP packets containing the error message: “udp port 53 unreachable.” 

![tcpdump](sc/)


**Observation (tcpdump):** ICMP errors reporting **UDP port 53 unreachable** while querying DNS.

**Assessment:**
- DNS over UDP/53 being blocked or service unavailable → name resolution fails → HTTPS never starts.
- Likely causes: **Firewall rule blocking UDP/53**, DNS service outage, or network ACL misconfig.

**Actions:**
- Verify DNS reachability to resolver(s) (UDP+TCP 53).
- Check firewall/ACL changes and DNS server health.
- Add fallback resolvers and monitoring/alerting on NXDOMAIN/SERVFAIL spikes.

**Takeaway:** Fix name resolution first; higher-layer failures cascade from DNS. 
