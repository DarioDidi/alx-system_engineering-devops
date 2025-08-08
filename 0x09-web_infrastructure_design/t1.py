from graphviz import Digraph

# Single Server Infrastructure
single = Digraph("single_server", filename="single_server.gv")
single.attr(rankdir="LR", bgcolor="white")
single.attr(
    "node", shape="rectangle", style="rounded,filled", color="lightgrey"
)

# User
single.node(
    "User", "User\n(requests www.foobar.com)", shape="ellipse", color="skyblue"
)

# DNS
single.node(
    "DNS",
    "DNS Server\n(foobar.com)\nwww record → 8.8.8.8",
    width="2",
    height="1.5",
)

# Server components
with single.subgraph(name="cluster_server") as s:
    s.attr(label="Server (8.8.8.8)", color="black")
    s.node("Web", "Web Server\n(Nginx)", width="2", height="1.2")
    s.node("App", "Application Server", width="2", height="1.2")
    s.node("Code", "Application Files\n(Code Base)", width="2", height="1.2")
    s.node("DB", "Database\n(MySQL)", width="2", height="1.2")

    # Connections within server
    s.edge("Web", "App")
    s.edge("App", "Code")
    s.edge("App", "DB")

# External connections
single.edge("User", "DNS")
single.edge("DNS", "Web", label="HTTP/HTTPS request")

single.render(format="png", cleanup=True)
single
