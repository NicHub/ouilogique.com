#!/usr/bin/env python
# -*- coding: utf-8 -*-


import http.client
import os
import sys

FILES = ["pi-hole-whitelist.txt", "pi-hole-adlists.txt"]


def main():
    """ ___ """

    for _f in FILES:
        with open(_f, "r") as url_file:
            for line in url_file:
                print()
                cur_url = line.strip()

                conn = http.client.HTTPSConnection(cur_url, timeout=2)
                try:
                    conn.request("GET", "/")
                    r1 = conn.getresponse()
                    print(r1.status)
                    if not r1.status == 200:
                        print(f"NOK {cur_url}")
                    # else:
                    #     print("Web site exists")

                # except (http.client.InvalidURL, http.client.CannotSendRequest,
                #     http.client.CannotSendHeader) as excep:
                #     excep_msg = f"Error in {cur_url}"
                #     print(excep_msg)


                except Exception as e:
                    print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
