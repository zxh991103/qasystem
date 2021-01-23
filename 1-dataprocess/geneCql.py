from data2dict import nodelist

from data2dict import nodedict

from data2dict import nodeid

from data2dict import nodedesc

from data2dict import nodecode

from data2dict import noderes

nodedescp=nodedesc()

nodecodes=nodecode()

noderesn=noderes()



nodes = nodelist()

noderelation = nodedict()

nodesid = nodeid()



from py2neo import Graph,Node


g = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="971124")


def create__nodes():
    global g
    count = 0
    for i in nodes:
        node = Node(
            nodes[i],
            name=i,
            id=nodesid[i],
            desc=nodedescp[i],
            importres=noderesn[i],
            code=nodecodes[i]
        )
        g.create(node)
        count += 1
        print(count)

create__nodes()

