import psycopg2

def connect():
    return psycopg2.connect(user='learnadmin', password = 'Hi5Michael', database='SnapshotDev', host='snapshotdev.cpeg0owf2zfo.us-west-2.rds.amazonaws.com')