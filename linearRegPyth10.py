import os
import pyspark
from pyspark.sql import SparkSession
from dotenv import load_dotenv
load_dotenv()
key_filepath = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

spark = SparkSession.builder \
    .master("local[3]") \
    .appName("Airbnb Listings") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile",key_filepath  ) \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .getOrCreate()

# Read data from GCS
df = spark.read.parquet("gs://airbnb-listings-421017-bucket/airbnb_listings.parquet")
df.show(5)
# Parse DataFrame into (X, y) pairs
def parse_point(row):
    print(row)
    features = [float(row[column]) for column in row.asDict().keys()[:-1]]
    return (features, float(row[-1]))

# Apply parse_point function to each row and select relevant columns
parsed_data = df.rdd.map(parse_point)
print(parsed_data.collect())
