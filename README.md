# Getting started with Apache Spark

## Setup Spark in local mode
    echo download and extract spark 1.2.1
    cd ..
    wget http://d3kbcqa49mib13.cloudfront.net/spark-1.2.1-bin-hadoop2.4.tgz
    tar xzf spark-1.2.1-bin-hadoop2.4.tgz
    ln -sf ./spark-1.2.1-bin-hadoop2.4 spark
    
    echo make symlink to spark lib for python
    cd hkimeetup1
    ln -s ../spark/python/pyspark ./

## Run Hello World in local
    ../spark/bin/spark-submit hello_world.py

## Run Pi python example in local with 2 "workers"
    ../spark/bin/spark-submit ../spark/examples/src/main/python/pi.py 200 --master local[4]

* Tip: You can see UI for spark while it is running at http://IP:4040/

## Run Spark in interactive Python shell:
    ../spark/bin/pyspark --master local[2]

## Run Spark in interactive iPython shell
    PYSPARK_DRIVER_PYTHON=ipython \
     PYSPARK_DRIVER_PYTHON_OPTS="notebook --pylab inline" \
     ../spark/bin/pyspark --master local[2]    
## Bonus - anonymize_logs project
    cd anonymize_logs
     ../../spark/bin/spark-submit --master local[*] --py-files anon_helper.py anonymize_logs.py 'logs_input/*' logs_output
     
## Appendix
### Links
* http://spark.apache.org/docs/latest/
* http://spark.apache.org/docs/latest/ec2-scripts.html
