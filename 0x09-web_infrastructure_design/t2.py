from graphviz import Digraph

# Distributed Infrastructure
dist = Digraph("distributed", filename="distributed.gv")
dist.attr(rankdir="LR", bgcolor="white")
dist.attr("node", shape="rectangle", style="rounded,filled", color="lightgrey")

# User
dist.node(
    "User", "User\n(requests www.foobar.com)", shape="ellipse", color="skyblue"
)

# DNS
dist.node("DNS", "DNS Server\n(foobar.com)", width="2", height="1.5")

# Load Balancer
dist.node(
    "LB",
    "Load Balancer\n(HAProxy)\nRound Robin",
    width="2.5",
    height="1.5",
    color="lightblue",
)

# Web servers
with dist.subgraph(name="cluster_web") as web:
    web.attr(label="Web Servers (Nginx)")
    web.node("Web1", "Web Server 1", width="2", height="1.2")
    web.node("Web2", "Web Server 2", width="2", height="1.2")

# App servers
with dist.subgraph(name="cluster_app") as app:
    app.attr(label="Application Servers")
    app.node("App1", "App Server 1", width="2", height="1.2")
    app.node("App2", "App Server 2", width="2", height="1.2")

# Database
with dist.subgraph(name="cluster_db") as db:
    db.attr(label="Database Cluster")
    db.node(
        "DBMaster",
        "Primary\n(MySQL)",
        width="2",
        height="1.2",
        color="lightgreen",
    )
    db.node(
        "DBReplica",
        "Replica\n(MySQL)",
        width="2",
        height="1.2",
        color="lightgreen",
    )

# Code
dist.node("Code", "Application Files\n(Shared)", width="2", height="1.2")

# Connections
dist.edge("User", "DNS")
dist.edge("DNS", "LB")
dist.edge("LB", "Web1")
dist.edge("LB", "Web2")
dist.edge("Web1", "App1")
dist.edge("Web2", "App2")
dist.edge("App1", "Code")
dist.edge("App2", "Code")
dist.edge("App1", "DBMaster")
dist.edge("App2", "DBMaster")
dist.edge("DBMaster", "DBReplica", dir="both", label="Replication")

dist.render(format="png", cleanup=True)
dist
