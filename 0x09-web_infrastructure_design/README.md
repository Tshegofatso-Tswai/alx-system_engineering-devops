# Introduction
In this project, we are tasked with designing a simple web infrastructure, a distributed web infrastructure, a sercure and monitored web infrastructure, and a scale up web infrastructure.

# Simple Web Stack

## Design Overview

1. **Server:**
   - A single server with the IP address 8.8.8.8.

2. **Domain Name:**
   - The domain name is configured as foobar.com.
   - A www record is set up to point to the server's IP.

3. **Web Stack Components:**
   - Web Server (Nginx): Handles HTTP requests, serves static content.
   - Application Server: Manages dynamic content and interacts with the web server.
   - Database (MySQL): Stores and retrieves data for the website.

## Explanation of Components

- **Server:**
  - A physical or virtual machine responsible for hosting the web infrastructure.

- **Domain Name:**
  - A human-readable alias for the server's IP address.

- **DNS Record (www.foobar.com):**
  - www is a subdomain, and it is configured with a DNS record (e.g., an A record) pointing to the server's IP.

- **Web Server (Nginx):**
  - Receives and responds to HTTP requests, serving static content.

- **Application Server:**
  - Manages dynamic content, processing server-side logic, and interacting with the web server.

- **Database (MySQL):**
  - Stores and retrieves data for the website.

## Issues with the Infrastructure

1. **Single Point of Failure (SPOF):**
   - If any component fails, the entire system is affected.

2. **Downtime during Maintenance:**
   - Deploying new code requires restarting the web server, causing downtime.

3. **Scalability Issues:**
   - The infrastructure may struggle to handle a high volume of incoming traffic.

## Screenshot

![Web Stack Screenshot](https://i.imgur.com/OHtE25Y.png)


# Distributed Web Infrastructure
A three-server web infrastructure for hosting www.foobar.com with improved scalability and redundancy.

## Design
- 2 Servers
- 1 Web Server (Nginx)
- 1 Application Server
- 1 Load-Balancer (HAproxy)
- 1 Application Files (Code Base)
- 1 Database (MySQL)

## Explanation
- **Additional Elements:** Added for improved redundancy, load balancing, and scalability.
- **Load Balancer:** Distributes incoming traffic among multiple servers, enhancing performance.
- **Distribution Algorithm:** Load balancer configured with a specific algorithm to determine server selection.
- **Active-Active vs. Active-Passive:** Describes the setup where both servers actively handle requests or one serves as a backup.
- **Primary-Replica Cluster:** Database setup with a master-slave configuration for data redundancy.

## Issues
- **SPOF:** Potential Single Points of Failure exist.
- **Security Issues:** Lack of firewall and HTTPS.
- **No Monitoring:** Absence of a monitoring system for performance tracking.

## Screenshot
![Distributed Web Infrastructure Screenshot](https://i.imgur.com/LXYy5Km.png)


# Secured and Monitored Web Infrastructure
A secured and monitored three-server web infrastructure for hosting www.foobar.com with enhanced security measures.

## Design
- 3 Firewalls
- 1 SSL Certificate (HTTPS)
- 3 Monitoring Clients
- 1 Web Server (Nginx)
- 1 Application Server
- 1 Database (MySQL)

## Explanation
- **Additional Elements:** Added for security (firewalls), encryption (SSL), and monitoring.
- **Firewalls:** Enhance security by controlling incoming and outgoing traffic.
- **HTTPS:** Ensures encrypted communication between users and the website.
- **Monitoring:** Utilized for tracking system performance and collecting data.

## Issues
- **SSL Termination:** Explains the issues related to terminating SSL at the load balancer level.
- **Single MySQL Server:** Potential issue with a single server capable of accepting writes.
- **Uniform Server Components:** Potential problems with identical components on all servers.

## Screenshot
![Secured and Monitored Web Infrastructure Screenshot](https://i.imgur.com/tAYCrue.png)


# Scale Up
An advanced setup to scale up the web infrastructure, differentiating components and utilizing load balancing.

## Design
- 1 Server
- 1 Load-Balancer Cluster (HAproxy)
- Components Split Across Servers (Web Server, Application Server, Database)

## Explanation
- **Additional Elements:** Added to achieve component separation and scalability.
- **Load-Balancer Cluster:** Improves redundancy and load distribution.
- **Component Separation:** Each component (web server, app server, database) has its dedicated server.

## Screenshot
![Scale Up Screenshot](https://i.imgur.com/VcZRhuO.png)

