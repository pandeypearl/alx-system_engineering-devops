# 0x19. Postmortem

## Task
<hr>

### 0. My first postmortem
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:
<ul>
<li>Issue Summary (that is often what executives will read) must contain: 
<ul><li>duration of the outage with start and end times (including timezone)</li>
<li>what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)</li>
<li>what was the root cause</li></ul></li>
<li>Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
<ul><li>when was the issue detected</li>
<li>how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)</li>
<li>actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)</li>
<li>misleading investigation/debugging paths that were taken</li>
<li>which team/individuals was the incident escalated to</li>
<li>how the incident was resolved</li></ul></li>
<li>Root cause and resolution must contain:
<ul><li>explain in detail what was causing the issue</li>
<li>explain in detail how the issue was fixed</li></ul></li>
<li>Corrective and preventative measures must contain:
<ul><li>what are the things that can be improved/fixed (broadly speaking)</li>
<li>a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)</li></ul></li>
<li>Be brief and straight to the point, between 400 to 600 words</li>
</ul>

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
