#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from __future__ import print_function

__author__ = 'chenglanguo'
import etcd
import sys
import os
import re
etcdCli=etcd.Client(host=sys.argv[1],port=2379)
f = open(sys.argv[3],'wb')
f.write(etcdCli.get('%s' % sys.argv[2]).value.encode('utf-8'))
f.close()
