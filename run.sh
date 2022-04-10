#!/bin/bash
./imdbsurfer.sh > imdbsurfer.log 2>&1 &
tail -f imdbsurfer.log
