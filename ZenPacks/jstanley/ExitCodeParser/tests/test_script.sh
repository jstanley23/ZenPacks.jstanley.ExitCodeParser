#!/bin/bash
echo "test output | datapoint=$(($RANDOM % 20))"
exit $(($RANDOM % 7))
