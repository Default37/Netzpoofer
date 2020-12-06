from struct import pack
from scapy.all import rdpcap
from scapy.all import *

def main():
    print(' _____     ___     _____   _____   _____   ______  _______  ______  _____  ')
    print('(_____)  _(___)_  (_____) (_____) (_____) (______)(__ _ __)(______)(_____)   ')
    print('(_)__(_)(_)   (_)(_)___(_)(_)__(_)(_)__(_)(_)__      (_)   (_)__   (_)__(_)')
    print('(_____) (_)    _ (_______)(_____) (_____) (____)     (_)   (____)  (_____) ')
    print('(_)     (_)___(_)(_)   (_)(_)     ( ) ( ) (_)____    (_)   (_)____ ( ) ( ) ')
    print('(_)       (___)  (_)   (_)(_)     (_)  (_)(______)   (_)   (______)(_)  (_)') 

    pcap_filename = input('Pcap Filename: ')
    print(pcap_filename)
    packet_list = rdpcap(pcap_filename)   

    print('[*] There is %i packets.' %len(packet_list))
    print('Packet Content: ')
    print(packet_list)

    while True:
        print('1 - Especific Packet Content')
        print('2 - All Packet Content')
        print('3 - All TCP Packets')
        print('4 - All UDP Packets')
        print('5 - Quit')
        menu = int(input('Selection: '))
        if(menu == 1):
            espec_packet(packet_list)
            print('1 - Check more packets')
            print('2 - Quit')
            espec_menu = int(input('Selection: '))
            if(espec_menu == 2):
                break
        elif(menu == 2):
            full_packet(packet_list)
        elif(menu == 3):
            tcp_packet(packet_list)
        elif(menu == 4):
            udp_packet(packet_list)
        elif(menu == 5):
            break
    
def espec_packet(packet_list):
    print('Type the number of the packet to analyse')
    packet_number = int(input('Packet Number: '))
    packet_list[packet_number].show()

def full_packet(packet_list):
    for i in range(len(packet_list)):
        packet_list[i].show()

def tcp_packet(packet_list):
    for i in range(len(packet_list)):
        if packet_list[i].haslayer(TCP):
            if packet_list[i].dport == 58436:
                packet_list[i].show()

def udp_packet(packet_list):
    for i in range(len(packet_list)):
        if packet_list[i].haslayer(UDP):
            packet_list[i].show()

main()