#!/usr/bin/env bash

# export WORKLOAD=0 && export INSTANCE=3883352030247723487 && echo "br6g" && ./test.sh
# export WORKLOAD=0 && export INSTANCE=1143374607222644001 && echo "xx0r" && ./test.sh
# export WORKLOAD=0 && export INSTANCE=1190325428765922378 && echo "mhvq" && ./test.sh

if [[ -z "${WORKLOAD}" ]]; then
  echo "Please set WORKLOAD env variable!"
  exit 1
fi

if [[ -z "${INSTANCE}" ]]; then
  echo "Please set INSTANCE env variable!"
  exit 1
fi

count=0
echo "Press [CTRL+C] to stop or unset WORKLOAD env variable."
while :
do
  echo "Ping w/ ${WORKLOAD}"
  python ping_workload.py "${WORKLOAD}" "${INSTANCE}"
	sleep 15
	((count=count+1))
	echo "Passed $count*0.25 min..."
done
