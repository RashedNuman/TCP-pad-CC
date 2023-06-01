"""
        TCP Padding covert channel leveraging Minecraft-keep-alive TCP

Description: Python script to launch a covert channel using minecraft keep alive
                packet mechanism to apply steganography to the covert channel

@author: Rashed Alnuman
"""

from scapy.all import IP, TCP, Raw, send


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
    pass



def send_packet(destination_ip, destination_port, sequence_number, padding):
    
    if len(padding) > 32:
        raise ValueError("Padding length exceeds 32 bytes.")
    packet = IP(dst=destination_ip) / TCP(dport=destination_port, flags="A", seq=sequence_number) / Raw(load=padding)
    send(packet)



covert_message = "test"

reciever_ip = "192.168.0.100"  # cover reciever ip
destination_port = 25565  # covert reciever port
sequence_number = 123456  # sequence number, to be changed
padding = b"\x00\x00\x00"  # initial padding for testing

send_keep_alive_packet(destination_ip, destination_port, sequence_number, padding)


"""
Initial encoding scheme:

odd number padding indicates 1 and even number indicates 0
"""



  
