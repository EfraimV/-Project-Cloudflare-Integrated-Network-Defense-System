📡 Detection Logic Workflow
Cloudflare detects attack → writes to log

Python script parses logs every 5min for:

High threat scores (>30)

Known bot signatures

Automated response:

Cloudflare: Blocks at DNS/WAF layer

On-prem: Updates ACLs via Ansible

Cloud: Revokes AWS/Azure security groups
