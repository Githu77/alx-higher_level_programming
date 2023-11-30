#!/bin/bash
#picks URL, sends request to it,and shows size of response
curl -s "$1" | wc -c
