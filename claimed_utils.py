# Utilities used by CLAIMED

import os
import zipfile
from minio import Minio

# compresses 'path' into 'target' zipfile


def zipdir(target, path):
    print("adding "+path+" to "+target)
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))

# uncompresses 'zipfile_name' to 'target' directory


def unzip(target, zipfile_name):
    with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:
        zip_ref.extractall(target)
        
def check_and_get_checkpoint_asset(checkpoint_ip, checkpoint_user, checkpoint_pass, asset_name):
    client = Minio(checkpoint_ip, checkpoint_user, checkpoint_pass, secure=False)

    objects = client.list_objects(checkpoint_bucket)
    for obj in objects:
        if asset_name == obj.object_name:
            client.fget_object(checkpoint_bucket, asset_name, asset_name)
            return True
    return False
