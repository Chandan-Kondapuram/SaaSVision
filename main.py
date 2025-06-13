from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark.version)




# spark-submit \
#   --jars jars/spark-sql-kafka-0-10_2.12-3.5.0.jar,jars/kafka-clients-3.5.1.jar,jars/spark-token-provider-kafka-0-10_2.12-3.5.0.jar,jars/commons-pool2-2.11.1.jar \
#   spark_kafka_consumer.py