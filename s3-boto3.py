import boto3
s3 = boto3.client("s3")

buck = s3.create_bucket(
    Bucket = <bucket-name>,
    CreateBucketConfiguration={
          'LocationConstraint': <region-name>
    },
    ObjectOwnership='BucketOwnerPreferred'
)
dele = s3.delete_public_access_block(
    Bucket = <bucket-name>
)
f = s3.upload_file(<file-name>, <bucket-name>, <key-name>)
make_pub = s3.put_object_acl(
    ACL = 'public-read',
    Bucket = <bucket-name>,
    Key = <key-name>
)