"""
        TCP Padding covert channel leveraging Minecraft-keep-alive TCP

Description: Python script to launch a covert channel using minecraft keep alive
                packet mechanism to apply steganography to the covert channel

@author: Rashed Alnuman
"""

#from scapy.all import IP, TCP, Raw, send
from scapy.all import *


def string_to_binary(msg):
    """
    Converts a string message into binary format.

    params:
    ------
    msg : String, message to be decoded to binary

    returns:
    -------
    binary : String, binary representation of the message
    """
    
    binary = ""
    
    for char in msg:
        
        binary += bin(ord(char))[2:].zfill(8)  # Convert character to binary and pad with zeros
        
    return binary





def covert_channel(destination_ip, msg):
    """
    Implements the covert channel by encoding the secret message in binary
    representation into tcp padding where 1 and 0 are indicated through
    odd or even number of x00 padding units.

    params:
    ------
    destination_ip : String, destination internet protocol address of reciever

    msg : String, binary representation of the secret message
    """
    
    if len(padding) > 32:
        raise ValueError("Padding length exceeds 32 bytes.")
    packet = IP(dst=destination_ip) / TCP(dport=destination_port, flags="A", seq=sequence_number) / Raw(load=padding)
    send(packet)


def test():

    # Create IP packet
    ip_pkt = IP(src="192.168.0.1", dst="192.168.0.2")

    # Create TCP packet with padding
    tcp_pkt = TCP(sport=12345, dport=80, flags="PA",
                  seq=1234567890, ack=9876543210,
                  window=8192, options=[(("NOP", None),), (("NOP", None),)],
                  dataofs=10, urgptr=0)

    # Calculate padding length
    header_length = len(tcp_pkt) // 4  # TCP header length in 32-bit words
    padding_length = (header_length * 4) - len(tcp_pkt)  # Padding length in bytes

    # Limit padding length to maximum allowed value (15 bytes)
    padding_length = min(padding_length, 15)

    # Create padding bytes
    padding_bytes = b"\x00" * padding_length

    # Inject padding after TCP options
    tcp_pkt.options += [("Padding", padding_bytes)]

    # Combine IP and TCP packets
    packet = ip_pkt / tcp_pkt

    # Show packet details
    packet.show()

    # Send the packet
    #send(packet)


test()







"""
def send_packet(destination_ip, destination_port, sequence_number, padding):
    
    



covert_message = "test"

reciever_ip = "192.168.0.100"  # cover reciever ip
destination_port = 25565  # covert reciever port
sequence_number = 123456  # sequence number, to be changed
padding = b"\x00\x00\x00"  # initial padding for testing

send_keep_alive_packet(destination_ip, destination_port, sequence_number, padding)



Initial encoding scheme:

odd number padding indicates 1 and even number indicates 0
"""



  
