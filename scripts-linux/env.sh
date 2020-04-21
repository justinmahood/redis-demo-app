# to get your current Project ID
# gcloud config list project
#
# This script uses the Google Cloud Shell for the Project ID
export PROJECT_ID=`gcloud config get-value project`

export REGION=us-central1
export SERVICE_NAME=redis-connect-example
export IMAGE_NAME=redis-connect-example

