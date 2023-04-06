# 0x10. HTTPS SSL

## Tasks

### 0. World wide web
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

<ul>
<li>Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain lb-01 to your domain, point it to your lb-01 IP</li>
<li>Add the subdomain web-01 to your domain, point it to your web-01 IP</li>
<li>Add the subdomain web-02 to your domain, point it to your web-02 IP</li>
<li>Your Bash script must accept 2 arguments:
<ul><li>1. domain:<ul><li>type: string</li><li>what: domain name to audit</li><li>mandatory: yes</li></ul></li>
<li>2. subdomain:<ul><li>type: string</li><li>what: specific subdomain to audit</li><li>mandatory: no</li></ul></li></ul></li>
<li>Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</li>
<li>When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order</li>
<li>When passing domain and subdomain parameters, display information for the specified subdomain</li>
<li>Ignore shellcheck case SC2086</li>
<li>Must use: <ul><li>awk</li><li>at least one Bash function</li></ul></li>
<li>You do not need to handle edge cases such as: <ul><li>Empty parameters</li><li>Nonexistent domain names</li><li>Nonexistent subdomains</li></ul></li>
</ul>

Example:

<pre><code>
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
</code></pre>


### 1. HAproxy SSL termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

<ul>
<li>HAproxy must be listening on port TCP 443</li>
<li>HAproxy must be accepting SSL traffic</li>
<li>HAproxy must serve encrypted traffic that will return the / of your web server</li>
<li>When querying the root of your domain name, the page returned must contain Holberton School</li>
<li>Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)</li>
</ul>

The file 1-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.

Example:

<pre><code>
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
</code></pre>


