#!/usr/bin/env bash

# export WORKLOAD=0 && ./test.sh

if [[ -z "${WORKLOAD}" ]]; then
  echo "Please set WORKLOAD env variable!"
  exit 1
fi

count=0
echo "Press [CTRL+C] to stop or unset WORKLOAD env variable."
while :
do
  echo "Ping w/ ${WORKLOAD}"
  python ping_workload.py "${WORKLOAD}"
	sleep 15
	((count=count+1))
	echo "Passed $count*0.25 min..."
done
