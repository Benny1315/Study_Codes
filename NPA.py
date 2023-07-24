# Network Packet Analayzer


import pyshark

# Set up the packet capture session on the Wi-Fi interface
capture = pyshark.LiveCapture(interface='Wi-Fi name',
                             display_filter='Protocol or IP')

# Start capturing packets and process them
for packet in capture.sniff_continuously(packet_count=20):  # Capture 10 packets
    # Access packet information
    source_ip = packet.ip.src
    destination_ip = packet.ip.dst
    protocol = packet.transport_layer
    payload = packet.data.data if hasattr(packet, 'data') else ""

    # Process the packet information
    print(f"Source IP: {source_ip}")
    print(f"Destination IP: {destination_ip}")
    print(f"Protocol: {protocol}")
    print(f"Payload: {payload}")
    print("-----------")
