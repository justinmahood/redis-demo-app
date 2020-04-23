# cloud-run-vpc-redis

Example of connecting a Cloud Run service to Redis via a VPC connector

Redis is used to keep track of the last load of the site and stores the last viewer's browser name and version. When a new person loads the page they see their own browser name and version, plus the info from the last person to load the site.

![Image](https://raw.githubusercontent.com/code128/cloud-run-vpc-redis/master/splash.png)
