from aws_cdk import core
from aws_cdk import aws_s3 as s3


class Turma4CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        s3.Bucket(self, 'bucket-belisco-cdk-turma4', bucket_name='bucket-belisco-cdk-turma4')
