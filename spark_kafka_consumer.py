from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType, BooleanType, TimestampType

# Define the schema for the incoming JSON messages
schema = StructType() \
    .add("event_id", StringType()) \
    .add("user_id", StringType()) \
    .add("event_type", StringType()) \
    .add("plan", StringType()) \
    .add("region", StringType()) \
    .add("amount", FloatType()) \
    .add("is_trial", BooleanType()) \
    .add("timestamp", StringType())

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaRawEventsToBigQuery") \
    .master("local[*]") \
    .config("spark.sql.streaming.statefulOperator.checkCorrectness.enabled", "false") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/Users/chandankondapuram/Documents/My Projects/kafka-project/gcp-spark-sa.json") \
    .config("spark.jars", ",".join([
        "jars/spark-sql-kafka-0-10_2.12-3.5.0.jar",
        "jars/kafka-clients-3.5.1.jar",
        "jars/spark-token-provider-kafka-0-10_2.12-3.5.0.jar",
        "jars/commons-pool2-2.11.1.jar",
        "jars/spark-bigquery-with-dependencies_2.12-0.35.1.jar",
        "jars/gcs-connector-hadoop3-latest.jar"
    ])) \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Read Kafka stream
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "saas-events") \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", "false") \
    .load()

# Parse the JSON and cast timestamp
df_parsed = df_raw.selectExpr("CAST(value AS STRING) as json_string") \
    .select(from_json(col("json_string"), schema).alias("data")) \
    .select("data.*") \
    .withColumn("timestamp", col("timestamp").cast(TimestampType()))

# Write the full raw parsed data to BigQuery in append mode
df_parsed.writeStream \
    .format("bigquery") \
    .option("table", "realtime-pipeline-457321.saas_data.raw_events") \
    .option("checkpointLocation", "/tmp/raw_events_checkpoint") \
    .option("credentialsFile", "/Users/chandankondapuram/Documents/My Projects/kafka-project/gcp-spark-sa.json") \
    .option("parentProject", "realtime-pipeline-457321") \
    .option("temporaryGcsBucket", "realtime-temp-bucket-457321") \
    .outputMode("append") \
    .start() \
    .awaitTermination()





# spark-submit \
#   --conf spark.driver.bindAddress=127.0.0.1 \
#   --conf spark.driver.host=127.0.0.1 \
#   --jars jars/spark-sql-kafka-0-10_2.12-3.5.0.jar,\
# jars/kafka-clients-3.5.1.jar,\
# jars/spark-token-provider-kafka-0-10_2.12-3.5.0.jar,\
# jars/commons-pool2-2.11.1.jar,\
# jars/spark-bigquery-with-dependencies_2.12-0.35.1.jar,\
# jars/gcs-connector-hadoop3-latest.jar \
#   spark_kafka_consumer.py