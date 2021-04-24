import os
from abc import abstractmethod

import boto3
from pydantic import BaseModel

DYNAMO_DB_CLIENT = None


def _dynamo_db_client():
    global DYNAMO_DB_CLIENT
    if DYNAMO_DB_CLIENT is None:

        if os.environ.get('IS_OFFLINE') is not None:
            DYNAMO_DB_CLIENT = boto3.client(
                'dynamodb',
                region_name='localhost',
                endpoint_url='http://localhost:8000',
                aws_access_key_id='default',
                aws_secret_access_key='default',
            )
        else:
            DYNAMO_DB_CLIENT = boto3.client('dynamodb')

    return DYNAMO_DB_CLIENT


class DynamoModel(BaseModel):
    @property
    def table_name(self):
        raise NotImplementedError('Must define a table name.')

    @abstractmethod
    def to_dynamo(self):
        raise NotImplementedError('Must implement to_dynamo.')

    @abstractmethod
    def from_dynamo(self):
        raise NotImplementedError('Must implement from_dynamo.')

    def save(self):
        return _dynamo_db_client().put_item(
            TableName=self.table_name,
            Item=self.to_dynamo(),
        )

    def get(self):
        pass
