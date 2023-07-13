
f = open("newfile.txt", "w")
i = 0
for i in range(20000):
    f.write("""
        docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
                inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
                ether 02:42:6d:c9:82:46  txqueuelen 0  (Ethernet)
                RX packets 0  bytes 0 (0.0 B)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 0  bytes 0 (0.0 B)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
                inet6 fe80::30d4:bdd3:b7d0:3a3e  prefixlen 64  scopeid 0x20<link>
                ether 08:00:27:c7:e5:37  txqueuelen 1000  (Ethernet)
                RX packets 21390  bytes 24617735 (24.6 MB)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 7691  bytes 1033944 (1.0 MB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
                inet 127.0.0.1  netmask 255.0.0.0
                inet6 ::1  prefixlen 128  scopeid 0x10<host>
                loop  txqueuelen 1000  (Local Loopback)
                RX packets 2565  bytes 1164016 (1.1 MB)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 2565  bytes 1164016 (1.1 MB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        """)
    

