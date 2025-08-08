# Single Server Infrastructure:

- User: Initiates request by entering www.foobar.com
 
- DNS Server: Translates domain to IP (8.8.8.8) using a CNAME record for www
 
- Web Server (Nginx): Handles HTTP requests, serves static content, proxies dynamic requests
 
- Application Server: Executes application logic, processes dynamic content
 
- Database (MySQL): Stores and manages persistent data
 
- Application Files: Contains the website's codebase
    
Diasdvantages:
    
- SPOF: Single point of failure at every component

- Maintenance Downtime: Any update requires taking down the whole system

- No Scalability: Cannot handle increased traffic


# Distributed Infrastructure:

- Load Balancer (HAProxy):
    
    Distributes traffic using Round Robin algorithm

    Active-Active setup (both servers handle traffic simultaneously)

- Web Servers (Nginx):

    Two instances for redundancy and load distribution

- Application Servers:

    Two instances to handle increased processing load

- Database Cluster:

    Primary-Replica setup where Primary handles writes and Replica handles reads

    Replica syncs with Primary via replication

Disadvantages:

- SPOFs: Load balancer and primary database

- Security: No firewalls or HTTPS

- No Monitoring: No visibility into system health

# Secured Infrastructure:

Firewalls:

    FW1: Protects load balancer
    
    FW2: Protects web servers
    
    FW3: Protects application servers

HTTPS:

- SSL certificate encrypts traffic
- Terminated at load balancer (potential security issue)

Monitoring:

- Agents collect metrics (QPS, response times, errors)
 
- Sent to centralized monitoring server
 
- To monitor QPS: track requests per second at web servers

Database:

- Primary with two replicas for read scaling
 
- Still only one write node (potential bottleneck)

Disadvantages:

- SSL Termination: Decrypted traffic between LB and web servers

- Single Write DB: Primary remains a bottleneck

- Identical Components: Limits specialization optimization
