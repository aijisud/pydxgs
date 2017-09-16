#!/bin/sh
basedir="$HOME/github/repositories/pydxgs"

logfile="$HOME/workspace/log/tickmonitor.log"

cd $basedir
python $basedir/tickmonitor.py > $logfile

#end
