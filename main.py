from scapy.all import send, IP, UDP
import time
from config import *

def wakeup(ip: str, xbox_live_device_id: str):
    pbase = IP(dst=ip)/UDP(sport=50519,dport=5050)
    devid_bytes = xbox_live_device_id.upper().encode("ascii", "ignore")
    devid_length = len(devid_bytes).to_bytes(1, byteorder="big")
    payload = b"\x00" + devid_length + devid_bytes + b"\x00"
    payload_length = len(payload).to_bytes(1, byteorder="big")
    pheader = b"\xdd\x02\x00" + payload_length + b"\x00\x00" 
    return pbase/(pheader + payload)

def ping(ip: str, xbox_live_device_id: str):
    pbase = IP(dst=ip)/UDP(sport=50519,dport=5050)
    payload = b"\xdd\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x02"
    return pbase/payload

if __name__ == "__main__":
    for i in range(5):
        send(wakeup(ip, xbox_live_device_id))
        time.sleep(1)
