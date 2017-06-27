#!/usr/bin/env python2.7
import requests
import json
import sys

def getRegistryTagList():
    registry="http://172.30.33.31:5000"
    res=requests.get(registry+"/v2/")
    assert res.status_code == 200

    res=requests.get(registry+"/v2/_catalog?n=1000")
    assert res.status_code == 200

    repositories = res.json().get("repositories",[])

    for repository in repositories:
        res = requests.get(registry + "/v2/{}/tags/list".format(repository))
        tags = res.json().get("tags",None)
        if tags:
            for tag in tags:
                image = format(repository)
                tag = format(tag)
                if len(sys.argv) <2:
                    print (image+":"+tag)
                else:
                    AppTargetName=sys.argv[1]
                    if image.endswith(AppTargetName):
                        print (image+":"+tag)
if __name__ == "__main__":
    getRegistryTagList()
