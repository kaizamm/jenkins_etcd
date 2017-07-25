#!/usr/bin/env python
import requests,sys,os

def healthyCheck():
  if len(sys.argv) < 2: sys.exit("need 1 argument")
  url = sys.argv[1]
  code = requests.get(url).status_code
  if code >= 200 and code < 400:
    print "healthy check ok , status_code:%s" % code
  else:
    print "healthy check not ok, status_code:%s" % code
    sys.exit("healthy check not ok")

if __name__ == "__main__":
  healthyCheck()
