#!/bin/bash
#Set up environment for accessing and processing SnowEx Data at the NSIDC DAAC

#install python pip
sudo apt-get install python3-pip

#Install virtual environment
pip install virtualenv

#Check versiion
virtualenv --version

#make virtual environment
virtualenv venv

#activate environment
source venv/bin/activate

#intall geopandas 
pip install geopandas

#install requests
pip install requests