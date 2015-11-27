#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
ser = serial.Serial( '/dev/tty.wchusbserial14230', baudrate=9600, timeout=3.0 )
ser.write( b"<ID01><PA>sss<L2> <E>" )
print( ser.name )
ser.close()


# cat -v < /dev/tty.wchusbserial14230
# stty -f /dev/tty.wchusbserial14230 9600 cs8 cread clocal

# stty -f /dev/tty.wchusbserial14230 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
# echo -n "<ID01><PA><L1><F2>KIOSQUE DE MONTCHOISI<L2><F2>JOYEUSES FETES DE FIN D'ANNEE<E>" > /dev/tty.wchusbserial14230


# stty -f /dev/tty.wchusbserial14230 cs8 9600 ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts

# screen /dev/tty.wchusbserial14230 9600


sudo socat -d -d -d -d -lf /tmp/socat pty,link=/dev/tty.wchusbserial14230,raw,echo=0,user=nico,group=staff pty,link=/dev/slave,raw,echo=0,user=nico,group=staff
sudo socat -d -d -d -d -lf /tmp/socat pty,link=/dev/slave,raw,echo=0,user=nico,group=staff pty,link=/dev/tty.wchusbserial14230,raw,echo=0,user=nico,group=staff

<ID01><PA>coucou<L2> <E>