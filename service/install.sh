#!/bin/bash

# copy & chmod
cp service/xinfodesk.service /etc/systemd/system/xinfodesk.service
chmod 644 /etc/systemd/system/xinfodesk.service

# reload systemd
systemctl daemon-reload

# enable auto-start
systemctl enable SERVICENAME

# run
systemctl start xinfodesk
systemctl status xinfodesk