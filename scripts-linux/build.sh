## Set your these environment variables first 
export PROJECT_ID=`gcloud config get-value project`
export REGION=us-central1
export SERVICE_NAME=cr-intg-redis-test
export IMAGE_NAME=cr-intg-redis-test

gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME

gcloud run deploy $SERVICE_NAME \
--region $REGION \
--image gcr.io/$PROJECT_ID/$IMAGE_NAME \
--allow-unauthenticated