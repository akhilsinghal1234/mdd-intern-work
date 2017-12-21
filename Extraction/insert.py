# import understand,sys
# import argparse
# import json
# from subprocess import call
from influxdb import InfluxDBClient

def insert_metrics(row,db_name,d_time,host='localhost', port=8086):
    user = ''
    password = ''
    dbname = 'metrics'
    dbuser = ''
    dbuser_password = ''
    json_body = [
        {
            "measurement": db_name[:-4],
            "time": d_time,
            "fields" : row
        }
    ]
    client = InfluxDBClient(host, port, user, password, dbname)
    client.write_points(json_body)