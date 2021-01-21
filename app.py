
'''from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__,template_folder='template')
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/live-data', methods=["GET", "POST"])
def data():
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
'''


import findspark
import pyspark
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import pandas
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__,template_folder='template')
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

conf = SparkConf().setAppName("traccar").setMaster('local')
sc = SparkContext.getOrCreate(conf=conf)
#spark = SparkSession(sc)
ssc = StreamingContext(sc, 1)
data = KafkaUtils.createDirectStream(ssc, topics=["JavaTopic"], kafkaParams={"metadata.broker.list":"localhost:9092"})
counts=data.map(lambda x: json.loads(x[1])).pprint()





findspark.init(spark_home='C:\spark\spark-2.4.7-bin-hadoop2.7')

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/VisTrac', methods=["GET", "POST"])
def main1():
    return render_template('VisTrac.html')


@app.route('/data', methods=["GET", "POST"])
def data():
   

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True, host='127.0.0.1', port=5000)