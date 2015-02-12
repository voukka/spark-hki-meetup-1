__author__ = 'Vladimir Grigor <vladimir.grigor@kiosked.com>'

"""
One way to anonymize some logs
Run me as
cd this_dir
../../spark/bin/spark-submit --master local[*] --py-files md5py.py,anon_helper.py anonymize_logs.py 'logs_input/*' 'logs_output/'
or
../../spark/bin/spark-submit --master local[*] --py-files anon_helper.py anonymize_logs.py 'logs_input/*'
"""

import sys
import json


from pyspark import SparkContext

from anon_helper import Helper
if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print >> sys.stderr, "Usage: %s <input_file> [output_dir]" % (sys.argv[0])
        exit(-1)

    sc = SparkContext(appName="AnonymizeLogs", )

    input_file = sys.argv[1]

    inputRDD = sc.textFile(input_file)

    helper = Helper()
    anonEventRDD = inputRDD.map(lambda l: helper.anonymize_event(json.loads(l)))

    if len(sys.argv) == 3:
        anonEventRDD.coalesce(anonEventRDD.getNumPartitions() - 1)\
            .map(lambda x: json.dumps(x)).saveAsTextFile(sys.argv[2])
    else:
        for r in anonEventRDD.collect():
            print r

    sc.stop()