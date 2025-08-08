from graphviz import Digraph

# Secured Infrastructure
secure = Digraph("secured", filename="secured.gv")
secure.attr(rankdir="LR", bgcolor="white")
secure.attr(
    "node", shape="rectangle", style="rounded,filled", color="lightgrey"
)

# User
secure.node(
    "User",
    "User\n(requests https://www.foobar.com)",
    shape="ellipse",
    color="skyblue",
)

# DNS
secure.node("DNS", "DNS Server\n(foobar.com)", width="2", height="1.5")

# Firewalls
secure.node("FW1", "Firewall", width="1.5", height="1", color="orange")
secure.node("FW2", "Firewall", width="1.5", height="1", color="orange")
secure.node("FW3", "Firewall", width="1.5", height="1", color="orange")

# Load Balancer with SSL
secure.node(
    "LB",
    "Load Balancer\n(HAProxy with SSL termination)\nHTTPS → HTTP",
    width="3",
    height="1.5",
    color="lightblue",
)

# Web servers with monitoring
with secure.subgraph(name="cluster_web") as web:
    web.attr(label="Web Servers (Nginx)")
    web.node(
        "Web1", "Web Server 1\nMonitoring Agent", width="2.5", height="1.2"
    )
    web.node(
        "Web2", "Web Server 2\nMonitoring Agent", width="2.5", height="1.2"
    )

# App servers with monitoring
with secure.subgraph(name="cluster_app") as app:
    app.attr(label="Application Servers")
    app.node(
        "App1", "App Server 1\nMonitoring Agent", width="2.5", height="1.2"
    )
    app.node(
        "App2", "App Server 2\nMonitoring Agent", width="2.5", height="1.2"
    )

# Database
with secure.subgraph(name="cluster_db") as db:
    db.attr(label="Database Cluster")
    db.node(
        "DBMaster",
        "Primary\n(MySQL)",
        width="2",
        height="1.2",
        color="lightgreen",
    )
    db.node(
        "DBReplica1",
        "Replica 1\n(MySQL)",
        width="2",
        height="1.2",
        color="lightgreen",
    )
    db.node(
        "DBReplica2",
        "Replica 2\n(MySQL)",
        width="2",
        height="1.2",
        color="lightgreen",
    )

# Code
secure.node("Code", "Application Files\n(Shared)", width="2", height="1.2")

# SSL
secure.node(
    "SSL",
    "SSL Certificate\n(www.foobar.com)",
    width="2",
    height="1",
    color="yellow",
)

# Monitoring
secure.node(
    "Monitor",
    "Monitoring Server\n(SumoLogic)",
    shape="cylinder",
    color="purple",
)

# Connections
secure.edge("User", "DNS")
secure.edge("DNS", "FW1")
secure.edge("FW1", "LB")
secure.edge("LB", "FW2")
secure.edge("FW2", "Web1")
secure.edge("FW2", "Web2")
secure.edge("Web1", "FW3")
secure.edge("Web2", "FW3")
secure.edge("FW3", "App1")
secure.edge("FW3", "App2")
secure.edge("App1", "Code")
secure.edge("App2", "Code")
secure.edge("App1", "DBMaster")
secure.edge("App2", "DBMaster")
secure.edge("DBMaster", "DBReplica1", dir="both")
secure.edge("DBMaster", "DBReplica2", dir="both")
secure.edge("SSL", "LB")
secure.edge("Web1", "Monitor")
secure.edge("Web2", "Monitor")
secure.edge("App1", "Monitor")
secure.edge("App2", "Monitor")
secure.edge("DBMaster", "Monitor")
secure.edge("DBReplica1", "Monitor")
secure.edge("DBReplica2", "Monitor")

secure.render(format="png", cleanup=True)
secure
