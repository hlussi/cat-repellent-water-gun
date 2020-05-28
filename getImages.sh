#!/bin/bash

ssh pi@pi3.local 'cd /home/pi/cat-repellent-water-gun/images; tar cvfz /tmp/images.tar.gz .'
mkdir images
scp pi@pi3.local:/tmp/images.tar.gz images
cd images
tar xvfz images.tar.gz
\rm images.tar.gz
