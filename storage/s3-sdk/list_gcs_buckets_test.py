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

import os

import list_gcs_buckets

BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
OBJECT = "random-object"

def test_create_bucket(capsys):
    response = list_gcs_buckets.create_gcs_bucket(BUCKET)
    out, _ = capsys.readouterr()
    assert response is not None

def test_get_bucket(capsys):
    response = list_gcs_buckets.get_gcs_bucket(BUCKET)
    out, _ = capsys.readouterr()
    assert response is not None

def test_list_buckets(capsys):
    response = list_gcs_buckets.list_gcs_buckets()
    out, _ = capsys.readouterr()
    assert response is not None
    assert BUCKET in out

def test_create_object(capsys):
    response = list_gcs_buckets.create_gcs_object(BUCKET, "resources/example.txt", OBJECT)
    out, _ = capsys.readouterr()

def test_list_objects(capsys):
    response = list_gcs_buckets.list_gcs_objects(BUCKET)
    out, _ = capsys.readouterr()
    assert response is not None
    assert OBJECT in out

def test_get_object(capsys):
    response = list_gcs_buckets.get_gcs_object(BUCKET, OBJECT)
    out, _ = capsys.readouterr()
    assert response is not None

def test_download_object(capsys):
    response = list_gcs_buckets.download_gcs_object(BUCKET, OBJECT, "resources/example_down.txt")
    out, _ = capsys.readouterr()
    # test that file downloaded...

def test_delete_object(capsys):
    response = list_gcs_buckets.delete_gcs_object(BUCKET, OBJECT)
    out, _ = capsys.readouterr()
    assert response is not None

def test_delete_bucket(capsys):
    response = list_gcs_buckets.delete_gcs_bucket(BUCKET)
    out, _ = capsys.readouterr()
    assert response is not None
