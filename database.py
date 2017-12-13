import psycopg2
import psycopg2.extras

def connect():
    psycopg2.extras.register_uuid()
    return psycopg2.connect(user='learnadmin', password = 'Hi5Michael', database='SnapshotDev', host='snapshotdev.cpeg0owf2zfo.us-west-2.rds.amazonaws.com')