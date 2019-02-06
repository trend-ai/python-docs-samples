#!/usr/bin/env python

# Copyright 2018 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This sample shows how to list Google Cloud Storage (GCS) buckets
   using the AWS S3 SDK with the GCS interoperable XML API.

GCS Credentials are passed in using the following environment variables:

    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY

Learn how to get GCS interoperable credentials at
https://cloud.google.com/storage/docs/migrating#keys.
"""

import boto3
from botocore.handlers import set_list_objects_encoding_type_url
boto3.set_stream_logger(name='botocore')

# [START storage_s3_sdk_create_bucket]
def create_gcs_bucket(bucket_name):
    """Create a GCS bucket using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.create_bucket(Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'US'})
# [END storage_s3_sdk_create_bucket]
    return response

# [START storage_s3_sdk_get_bucket]
def get_gcs_bucket(bucket_name):
    """Get a GCS bucket using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.get_bucket_acl(Bucket=bucket_name)
# [END storage_s3_sdk_get_bucket]
    return response


# [START storage_s3_sdk_list_buckets]
def list_gcs_buckets():
    """Lists all GCS buckets using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")

    # Call GCS to list current buckets
    response = interop_client.list_buckets()

    # Print bucket names
    print("Buckets:")
    for bucket in response["Buckets"]:
        print(bucket["Name"])
# [END storage_s3_sdk_list_buckets]
    return response

# [START storage_s3_sdk_create_object]
def create_gcs_object(bucket_name, local_file_path, object_name):
    """Lists all GCS buckets using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.upload_file(Filename=local_file_path, Bucket=bucket_name, Key=object_name)
# [END storage_s3_sdk_create_object]
    return response

def list_gcs_objects(bucket_name):
    """Lists all GCS buckets using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")
    interop_client.meta.events.unregister(
    'before-parameter-build.s3.ListObjects',
    set_list_objects_encoding_type_url)
    response = interop_client.list_objects(Bucket=bucket_name)

    # Print bucket names
    print("Objects:")
    for file in response["Contents"]:
        print(file["Key"])
# [END storage_s3_sdk_list_buckets]
    return response

# [START storage_s3_sdk_get_object]
def get_gcs_object(bucket_name, object_name):
    """Get GCS object using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.get_object(Bucket=bucket_name, Key=object_name)
# [END storage_s3_sdk_get_object]
    return response

# [START storage_s3_sdk_download_object]
def download_gcs_object(bucket_name, object_name, local_file_path):
    """Lists all GCS buckets using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.download_file(Filename=local_file_path, Bucket=bucket_name, Key=object_name)
# [END storage_s3_sdk_read_object]
    return response

# [START storage_s3_sdk_delete_object]
def delete_gcs_object(bucket_name, object_name):
    """Delete a GCS object using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.delete_object(Bucket=bucket_name, Key=object_name)
# [END storage_s3_sdk_delete_object]
    return response

# [START storage_s3_sdk_delete_bucket]
def delete_gcs_bucket(bucket_name):
    """Lists all GCS buckets using boto3 SDK"""
    # Change the endpoint_url to use the Google Cloud Storage XML API endpoint.
    interop_client = boto3.client('s3', region_name="auto",
                                  endpoint_url="https://storage.googleapis.com")


    response = interop_client.delete_bucket(Bucket=bucket_name)
# [END storage_s3_sdk_delete_bucket]
    return response

if __name__ == '__main__':
    list_gcs_buckets()
