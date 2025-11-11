# Network Layer Communication — DNS/ICMP Troubleshooting

**Scenario:** Users receive *Destination port unreachable* when loading `www.yummyrecipesforme.com`.

**Observation (tcpdump):** ICMP errors reporting **UDP port 53 unreachable** while querying DNS.

**Assessment:**
- DNS over UDP/53 being blocked or service unavailable → name resolution fails → HTTPS never starts.
- Likely causes: **Firewall rule blocking UDP/53**, DNS service outage, or network ACL misconfig.

**Actions:**
- Verify DNS reachability to resolver(s) (UDP+TCP 53).
- Check firewall/ACL changes and DNS server health.
- Add fallback resolvers and monitoring/alerting on NXDOMAIN/SERVFAIL spikes.

**Takeaway:** Fix name resolution first; higher-layer failures cascade from DNS. 
