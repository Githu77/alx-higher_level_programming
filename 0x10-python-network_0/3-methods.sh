#!/bin/bash
# picks a URL and displays all HTTP methods accepted by server.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
