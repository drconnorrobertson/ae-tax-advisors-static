#!/bin/bash
API_KEY="d1abe8dd1952d605902db4522d2536d3"
HOST="aetaxadvisors.com"
URL="$1"
if [ -z "$URL" ]; then echo "Usage: $0 <url>"; exit 1; fi
curl -s -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d "{\"host\":\"$HOST\",\"key\":\"$API_KEY\",\"keyLocation\":\"https://$HOST/$API_KEY.txt\",\"urlList\":[\"$URL\"]}"
echo "Submitted $URL to IndexNow"
