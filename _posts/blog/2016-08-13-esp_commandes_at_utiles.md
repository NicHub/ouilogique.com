---
author: Nico
date: 2016-08-13 09:24:00+02:00
image:
    feature: null
lang: fr
layout: page
published: true
redirect_from: []
tags: []
title: ESP8266 — Commandes AT utiles
---

Les commandes présentées télégraphiquement ici sont tirées des pages :

-   <https://alselectro.wordpress.com/2015/05/05/wifi-module-esp8266-1-getting-started-with-at-commands/>
-   <https://alselectro.wordpress.com/2015/05/13/wifi-module-esp8266-2-tcp-client-server-mode/>

---

## Get status

> retourne OK ou ERROR

```bash
AT
```

## Current firmware version

```bash
AT+GMR
```

```bash
> AT version:0.40.0.0(Aug 8 2015 14:45:58)
> SDK version:1.3.0
> Ai-Thinker Technology Co.,Ltd.
> Build:1.3.0.2 Sep 11 2015 11:48:04
> OK
```

## Baud rate

> fonctionne pas

```bash
AT+CIOBAUD?
```

## Mode of operation of the module

```bash
AT+CWMODE?
```

## List access points in range

```bash
AT+CWLAP
```

## Connect to your home/office access point

```bash
AT+CWJAP="yourSSID","yourWifiPassword"
AT+CWJAP="×××","×××"
```

```bash
> WIFI CONNECTED
> WIFI GOT IP
>
> OK
```

## Disconnect

```bash
AT+CWQAP
```

## Current IP

```bash
AT+CIFSR
```

```bash
> +CIFSR:STAIP,"192.168.1.132"
> +CIFSR:STAMAC,"18:fe:34:d4:8e:d5"
>
> OK
```

## ESP on STation mode

```bash
AT+CWMODE?
AT+CWMODE=1
```

## Start a web server with ESP module

```bash
AT+CIPMUX=1
```

## Start the server at HTTP port 80

```bash
AT+CIPSERVER=1,80
```

## Close server

```bash
AT+CIPSERVER=0
AT+RST
```

```bash
> OK
> 1,CLOSED
```

## Current IP

```bash
AT+CIFSR
```

```bash
> +CIFSR:STAIP,"192.168.1.132"
> +CIFSR:STAMAC,"18:fe:34:d4:8e:d5"
>
> OK
> 0,CONNECT

> +IPD,0,439:GET / HTTP/1.1
> Host: 192.168.1.132
> Connection: keep-alive
> Cache-Control: max-age=0
> Upgrade-Insecure-Requests: 1
> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,_/_;q=0.8
> Accept-Encoding: gzip, deflate, sdch
> Accept-Language: fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4,de;q=0.2
```

```bash
AT+CIPSEND=0,31
<h1>Hello World</h1><p>cool</p>
AT+CIPCLOSE=0
```

```bash
telnet 192.168.1.132:80
```
