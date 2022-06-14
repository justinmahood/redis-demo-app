[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](stacks-button-redirect-ean27jt5ha-uc.a.run.app)

# cloud-run-vpc-redis

Example of connecting a Cloud Run service to Redis via a VPC connector

Redis is used to keep track of the last load of the site and stores the last viewer's browser name and version. When a new person loads the page they see their own browser name and version, plus the info from the last person to load the site.

## Setup

You'll need:

1. GCP Memorystore running redis
1. A Serverless VPC Connector to connect your Cloud Run service to Redis
1. REDISTHOST environment variable setup for your Cloud Run service to reference your Memorystore Redis

| Environment Variable | Example value |
| -------------------- | ------------- |
| REDISHOST           | 10.10.10.10   |

![Image](https://raw.githubusercontent.com/code128/cloud-run-vpc-redis/master/splash.png)
