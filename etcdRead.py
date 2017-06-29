#!/usr/bin/env python
import etcd
import sys
import time
import os
import re
reload (sys)
def getValue(host,port,location):
    etcdCli=etcd.Client(host=host,port=port)
    context=etcdCli.read(location).value
    return context

envValue=getValue(host=sys.argv[1],port=int(sys.argv[2]),location=sys.argv[3])
print(envValue)
