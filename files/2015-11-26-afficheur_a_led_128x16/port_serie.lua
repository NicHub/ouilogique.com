#!/usr/bin/env lua

fd=require("rs232")

B9600=13        --  9600 bauds
V24_8BIT=3        -- 8 bits
NO_PARITY=0        -- no parity

-- Open the serial port
-- /dev/ttyS0,V24_STANDARD
-------------------------------------
print("open port /dev/ttyS0")
result=fd.V24OpenPort("/dev/ttyS0",0,0)
print(result)

-- Define serial parameters
---------------------------------------------
print("9600 bauds, 8 bits , no parity")
result=fd.V24SetParameters(B9600,V24_8BIT,NO_PARITY)
print(result)

-- Timeout 5 seconds
------------------------
print("Receive Timeout is 5 seconds")
result=fd.V24SetTimeouts(50)
print(result)

-- Wait a character on the serial port
----------------------------------------------
print("Waiting.......")
result=fd.V24Getc()
print(result)

-- Send 'A'
-------------------------
print("sending 'A'")
result=fd.V24Putc(65)
print(result)

-- Send the string "hello"
-----------------------------
print("sending string 'hello'")
result=fd.V24Write("hello\n\r")
print(result)

-- Close the serial port
--------------------
print("Close serial port")
result=fd.V24ClosePort()
print(result)