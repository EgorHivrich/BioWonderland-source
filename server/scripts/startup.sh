#!bin/bash

systemctl daemon-reload
systemctl enable startup.service

systemctl start startup.service