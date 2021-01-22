import os
def nodedict():
    resdict={}
    with open("node.txt") as f:
        ll=[[],[],[],[],[],[]]
        for i in f:
            ss=i.split(' ')
            level=len(ss[0])
            datas=ss[1].split('\n')[0]
            ll[level-1].append(datas)
            if level == 1:
                continue
            else:
                resdict[datas]=ll[level-2][len(ll[level-2])-1]



    return resdict

print(nodedict())