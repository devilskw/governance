#!/bin/bash
docker-compose up -d
pause
aws --endpoint-url=http://localhost:4566 s3 mb s3://kazuo-bucket
aws --endpoint-url=http://localhost:4566 s3api put-bucket-acl --bucket kazuo-bucket --acl public-read
pause