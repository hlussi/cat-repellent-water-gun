#!/bin/bash

set -euo pipefail

PI=192.168.1.160
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
IMAGE_DIR=$DIR/../images

echo "copying images to $IMAGE_DIR"

ssh pi@$PI 'cd /home/pi/cat-repellent-water-gun/images; tar cvfz /tmp/images.tar.gz .'
mkdir -p $IMAGE_DIR
scp pi@192.168.1.160:/tmp/images.tar.gz $IMAGE_DIR
cd $IMAGE_DIR
tar xvfz images.tar.gz
\rm images.tar.gz

