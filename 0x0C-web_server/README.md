# 0x0C. Web server

## TASKS

### 0. Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

Requirements:
<ul>
<li>Accepts 4 parameters
<ul><li>1. The path to the file to be transferred</li>
<li>2. The IP of the server we want to transfer the file to</li>
<li>3. The username scp connects with</li>
<li>4. The path to the SSH private key that scp uses</li>
</li>
<li>Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed</li>
<li>scp must transfer the file to the user home directory ~/</li>
<li>Strict host key checking must be disabled when using scp</li>
</ul>

Example:
<pre><code>
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
<code></pre>

In this example, I:
<ul>
<li>remotely execute the ls ~/ command via ssh to see what ~/ contains</li>
<li>create a file named some_page.html</li>
<li>execute my 0-transfer_file script</li>
<li>remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred</li>
</ul>

That is one way of publishing your website pages to your server.
