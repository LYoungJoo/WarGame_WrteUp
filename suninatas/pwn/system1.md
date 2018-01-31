```
youngjoo@ubuntu pwn$ strings packet_dump.pcap | grep "pw="
Hid=suninatas&Hpw=suninatasc
Hid=blackkey&Hpw=blackkeyn
Hid=ultrashark&Hpw=sharkpass01~
Hid=ultrashark&Hpw=%3Dsharkpass01
Hid=ultrashark&Hpw=%3DSharkPass01
```

id = ultrashark<br/>
pw = =sharkpass01
