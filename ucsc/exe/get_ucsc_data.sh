#!/bin/bash
path=`dirname $0`/..
if [[ -z "$1" ]]
then
  hg="all"
else
  hg="$hg"
fi


if [[ "$hg" == "all" || "$hg" == "canfam2" ]]
then
  /bin/sh $path/canfam2/get_canfam2.sh
fi

if [[ "$hg" == "all" || "$hg" == "canfam3" ]]
then
  /bin/sh $path/canfam3/get_canfam3.sh
fi
