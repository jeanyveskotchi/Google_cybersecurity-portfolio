# Network Attacks — SYN Flood Analysis

**Symptom:** Website timeouts; packet capture shows abnormal volume of **TCP SYN** from unfamiliar IP.

**Explanation:** Attack exhausts server resources before the handshake completes (SYN backlog overflow).

**Evidence:**
- Repeated **SYN** to target; limited or missing final **ACK** from attacker.
- Downstream errors: **HTTP 504** from gateway; **RST, ACK** when server can't maintain state.

**Remediation:**
- Enable **SYN cookies**.
- **Rate-limit** SYN per source; SYN-proxy on edge.
- Autoscale / anycast frontends; WAF/CDN with L4 protections.
- Monitor backlog/conntrack, alert on spikes.

**Linux quick check:**

```bash
# enable at runtime
sudo sysctl -w net.ipv4.tcp_syncookies=1

# persist
echo 'net.ipv4.tcp_syncookies = 1' | sudo tee -a /etc/sysctl.conf
```
