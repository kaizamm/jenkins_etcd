#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from __future__ import print_function
__author__ = 'chenglanguo'
import etcd
import sys
import time
import os
import re
reload (sys)
etcdCli=etcd.Client(host=sys.argv[1],port=2379)
#etcdCli=etcd.Client(host='172.30.33.31',port=2379)
def push(local_dir, top_path='/', with_local_path=False):
    try:
        for root, dirs, files in os.walk(local_dir):
            if '.' not in dirs and '.' not in root:
                for name in files:
                    file = os.path.join(root, name)
                    f = open(file)
                    content = f.read()
                    f.close()
                    if not with_local_path:
                        etcd_path = '/' + top_path.strip('/') + '/' + file[re.match(local_dir, file).end():].strip(
                            '/')
                    else:
                        etcd_path = '/' + top_path.strip('/') + '/' + file.strip('/')
                    print(etcd_path)
                    etcdCli.write(etcd_path, content)
    except Exception as e:
        etcd.EtcdException(e)
push(sys.argv[2],top_path=sys.argv[3])
#push('AppCfg',top_path='quarkfinance.com/instances')
