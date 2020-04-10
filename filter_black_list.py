import os
from collections import Counter


def filter_black_list():
    res = []
    for root, dirs, files in os.walk("log"):
        for q in files:
            if "txt" in q:
                c = Counter()
                for line in open("./log/" + q, "r"):
                    if "[S]" in line:
                        begin = line.find("IP ")
                        end = line.rfind(" >")
                        ss = line[begin + 3:end]
                        c[ss] += 1
                    elif "[S.]" in line:
                        begin = line.find("IP ")
                        end = line.rfind(" >")
                        ss = line[begin + 3:end]
                        c[ss] -= 1
                for k in c:
                    if c.get(k) >= 1:
                        res.append(k)
    r = open("./" + "blacklist.list", "r")
    oldRes = r.readlines()
    r.close()
    with open("./" + "blacklist.list", "a") as f:
        for i in res:
            print(i, oldRes)
            if i+"\n" not in oldRes:
                f.writelines(i+"\n")
    f.close()


filter_black_list()
