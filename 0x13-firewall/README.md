# 0x13. Firewall

## Tasks

### 0. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:
<ul>
<li>The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)</li>
<li>Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
<ul><li>22 (SSH)</li>
<li>443 (HTTPS SSL)</li>
<li>80 (HTTP)</li>
</ul></li>
<li>Share the ufw commands that you used in your answer file</li>
</ul>

### 1. Port forwarding
Firewalls can not only filter requests, they can also forward them.

Requirements:
<ul>
<li>Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.</li>
<li>Your answer file should be a copy of the ufw configuration file that you modified to make this happen</li>
</ul>

Terminal in web-01:

<pre><code>
`
root@03-web-01:~# netstat -lpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2473/nginx
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      2473/nginx
tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd
udp        0      0 0.0.0.0:68              0.0.0.0:*                           594/dhclient
udp        0      0 0.0.0.0:54432           0.0.0.0:*                           594/dhclient
udp6       0      0 :::32563                :::*                                594/dhclient
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     SEQPACKET  LISTENING     7175     433/systemd-udevd   /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     6505     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8048     741/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     8419     987/acpid           /var/run/acpid.socket
root@03-web-01:~#
root@03-web-01:~# grep listen /etc/nginx/sites-enabled/default
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#   listen 8000;
#   listen somename:8080;
#   listen 443;
root@03-web-01:~#`
</code></pre>

