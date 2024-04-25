#!/bin/bash
# get the size  of the body response
curl -so /dev/null $1 -w '%{size_download}\n'
