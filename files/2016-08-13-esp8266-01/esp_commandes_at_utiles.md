
ESP8266 — Commandes AT utiles
=============================

Les commandes de ce fichier sont tirées des pages :

<https://alselectro.wordpress.com/2015/05/05/wifi-module-esp8266-1-getting-started-with-at-commands/>

<https://alselectro.wordpress.com/2015/05/13/wifi-module-esp8266-2-tcp-client-server-mode/>

---

# Get status ⇒ retourne OK ou ERROR
AT

# Return the current firmware version.
AT+GMR

> AT version:0.40.0.0(Aug  8 2015 14:45:58)
> SDK version:1.3.0
> Ai-Thinker Technology Co.,Ltd.
> Build:1.3.0.2 Sep 11 2015 11:48:04
> OK

# Baud rate ⇒ fonctionne pas
AT+CIOBAUD?

# returns the Mode of operation of the module.
AT+CWMODE?

# List access points in range.
AT+CWLAP

# Connect to your home/office access point
AT+CWJAP="yourSSID","yourWifiPassword"
AT+CWJAP="×××","×××"

> WIFI CONNECTED
> WIFI GOT IP
>
> OK

# Disconnect
AT+CWQAP

# Current IP
AT+CIFSR

> +CIFSR:STAIP,"192.168.1.132"
> +CIFSR:STAMAC,"18:fe:34:d4:8e:d5"
>
> OK

#  ESP on STation mode
AT+CWMODE?
AT+CWMODE=1

# start a web server with ESP module
AT+CIPMUX=1

# start the server at HTTP port 80
AT+CIPSERVER=1,80

# close server
AT+CIPSERVER=0
AT+RST

> OK
> 1,CLOSED

# Current IP
AT+CIFSR

> +CIFSR:STAIP,"192.168.1.132"
> +CIFSR:STAMAC,"18:fe:34:d4:8e:d5"
>
> OK
0,CONNECT

> +IPD,0,439:GET / HTTP/1.1
> Host: 192.168.1.132
> Connection: keep-alive
> Cache-Control: max-age=0
> Upgrade-Insecure-Requests: 1
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
> Accept-Encoding: gzip, deflate, sdch
> Accept-Language: fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4,de;q=0.2


AT+CIPSEND=0,31
<h1>Hello World</h1><p>cool</p>
AT+CIPCLOSE=0


telnet 192.168.1.132:80
