import understand,sys
from subprocess import call
from insert import insert_metrics

def projectMetric(db,sha,d_time,host='localhost', port=8086):
  db_name = db
  db = understand.open(db_name)
  row = {}
  row['sha'] = sha
  # row['datetime'] = str(d_time)
  metrics = db.metric(db.metrics())
  for k,v in sorted(metrics.items()):
    row[k] = v
  insert_metrics(row,db_name,d_time)