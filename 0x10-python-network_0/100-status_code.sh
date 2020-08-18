#!/bin/bash
curl -sI "$1" | grep HTTP | cut -d ' ' -f2
