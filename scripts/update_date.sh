#!/bin/sh

# Note:
# run this script with administrative priviledges
# make sure that you are connected to the internet

date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
