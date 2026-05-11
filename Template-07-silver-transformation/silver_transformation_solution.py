"""
Exercise 2 Solution: Silver Layer Transformation
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, date_trunc, from_unixtime
import time
import os

spark = SparkSession.builder \
    .appName("SilverTransformation") \
    .config("spark.sql.adaptive.enabled", "true") \
    .remote("sc://localhost:15002") \
    .config("spark.sql.legacy.parquet.nanosAsLong", "true") \
    .getOrCreate()

print("=== SILVER LAYER: DATA CLEANING AND ENRICHMENT ===\n")

bronze_orders = spark.read.parquet("/workspace/Lesson3-Exercise1-silver-transformation/solution/data/orders.parquet")
bronze_clicks = spark.read.json("/workspace/Lesson3-Exercise1-silver-transformation/solution/data/clickstream.json")

start_time = time.time()

# Clean orders
silver_orders = bronze_orders.filter(
    col("order_value").isNotNull() & 
    col("user_id").isNotNull() &
    (col("order_value") > 0)
).withColumn("order_date", col("order_date").cast("date"))

# Flatten clickstream
silver_events = bronze_clicks.select(
    col("user_id"),
    col("event_type").alias("action"),
    col("page_url").alias("page")
).filter(col("user_id").isNotNull())

# Join
silver = silver_orders.join(silver_events, "user_id", "left_outer") \
                     .dropDuplicates(["order_id"])

process_time = time.time() - start_time

print(f"Silver Orders Count: {silver_orders.count()}")
print(f"Silver Events Count: {silver_events.count()}")
print(f"Silver Joined Count: {silver.count()}")
print(f"Processing Time: {process_time:.3f}s")

print("\nSample Silver Data:")
silver.select("order_id", "user_id", "product_id", "order_value", "action", "order_date").show(5)

import tempfile

output_path = tempfile.mkdtemp()

# Write to temp directory
silver.write.mode("overwrite").partitionBy("order_date").parquet(output_path)

# Read back to verify
verification = spark.read.parquet(output_path)

print(f"\nSilver data written to {output_path}")
print(f"Verification - rows written: {verification.count()}")

spark.stop()
