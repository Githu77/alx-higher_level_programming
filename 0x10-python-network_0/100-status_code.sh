#!/bin/bash
#picks URL, sends request to it,and shows size of response
curl -s -o /dev/null -w "%{http_code}" "$1"
