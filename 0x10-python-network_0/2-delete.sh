#!/bin/bash
# sends DELETE request to  first argument(URL) and shows the body of the response
curl -sX DELETE "$1"
