#!/bin/sh
docker stop violence-detector-2
docker start violence-detector-2
docker exec -dit -w /root violence-detector-2 bash -c 'cd /home && ./extra.sh'
