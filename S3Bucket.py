import boto3


class S3Bucket:

    BUCKET_NAME = 'snapshot-dev-s3bucket'
    BUCKET_URL = "https://s3-us-west-1.amazonaws.com/" + BUCKET_NAME
    AWS_ID = 'AKIAIMJPSR5H46TZ5NQQ'
    AWS_KEY = 'uLicFNddTs1KuxqHRpo4fi4erIQmRqEVFMywqYQw'

    s3 = boto3.resource('s3', aws_access_key_id=AWS_ID, aws_secret_access_key=AWS_KEY)

    @classmethod
    def add(cls, localPath, fileKey):
        file = cls.s3.Object(cls.BUCKET_NAME, fileKey)
        file.put(ACL='public-read', Body=open(localPath,'rb'))

    @classmethod
    def getUrl(cls, fileKey):
        return cls.BUCKET_URL + "/" + fileKey

    @classmethod
    def delete(cls,fileKey):
        cls.s3.Object(cls.BUCKET_NAME, fileKey).delete()


# Examples:
# S3Bucket.add('../1.png', 'folder2/pic1.png')
# S3Bucket.delete("folder1/pic1.png")
#
# for bucket in s3.buckets.all():
#     for object in bucket.objects.all():
#         mypdf = s3.Object(bucket.name, 'node.pdf')
#         print(mypdf.content_length)

