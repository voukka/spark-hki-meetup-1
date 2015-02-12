__author__ = 'Vladimir Grigor <vladimir.grigor@kiosked.com>'

from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext(appName="HelloWorldPySpark",)
    print "\nHello World! \n\tYours,  %s." % sc.appName
