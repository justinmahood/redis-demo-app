# cloud-run-vpc-redis

Example of connecting a Cloud Run service to Redis via a VPC connector

Redis is used to keep track of the last load of the site and stores the last viewer's browser name and version. When a new person loads the page they see their own browser name and version, plus the info from the last person to load the site.

## Setup

You'll need:

1. Running redis instance (I'm using the Redis Certified by Bitnami on a GCP VM)
1. A Serverless VPC Connector
1. A couple of environment variables setup for your Cloud Run service to reference your redis

| Environment Variable | Example value |
| -------------------- | ------------- |
| redis_host           | 10.10.10.10   |
| redis_password       | 123456        |

![Image](https://raw.githubusercontent.com/code128/cloud-run-vpc-redis/master/splash.png)
