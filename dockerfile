# Use the base image
FROM jupyter/pyspark-notebook:latest



# Map volume to /home/jovyan/work inside the container
VOLUME [:"/home/jovyan/work"]

