import boto3


class S3Bucket:

    BUCKET_NAME = 'snapshot-dev-s3bucket'
    BUCKET_URL = "https://s3-us-west-1.amazonaws.com/" + BUCKET_NAME
    AWS_ID = 'AKIAJHIKEBDCJEEA4W6Q'
    AWS_KEY = 'AYQCTb8HeFTxZ1SKYbI3h6mp34CWhPos9kIsS+GV'

    s3 = boto3.resource('s3', aws_access_key_id=AWS_ID, aws_secret_access_key=AWS_KEY)

    @classmethod
    def add(cls, localPath, fileKey):
        file = cls.s3.Object(cls.BUCKET_NAME, fileKey)
        file.put(ACL='public-read', Body=open(localPath,'rb'))

    @classmethod
    def getUrl(cls, fileKey):
        urlKey = fileKey.replace(" ", "+")
        return cls.BUCKET_URL + "/" + urlKey

    @classmethod
    def delete(cls,fileKey):
        cls.s3.Object(cls.BUCKET_NAME, fileKey).delete()


# # Examples:
# S3Bucket.add('../f 1.pdf', 'file 1.pdf')
# S3Bucket.delete("org/InteractionMaterial/20121212/cultural 1.docx")
#
#
# for bucket in S3Bucket.s3.buckets.all():
#     for object in bucket.objects.all():
#         print(object.key)


