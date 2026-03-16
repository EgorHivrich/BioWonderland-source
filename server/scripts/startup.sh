#!/bin/sh

SERVICE_SCRIPT_PATH="/etc/systemd/system"

if [ -f "$SERVICE_SCRIPT_PATH/startup.service" ]; then
    cp recruiter-bot/startup.service $SERVICE_SCRIPT_PATH
fi

systemctl daemon-reload
systemctl enable startup.service

systemctl start startup.service