# AWS Data Lakes Templates

Solution templates for AWS Data Lakes exercises covering ingestion, governance, transformations, and table formats.

## Templates

| # | Template | Description |
|---|----------|-------------|
| 01 | [structured](Template-01-structured/) | Structured data ingestion to S3 |
| 02 | [unstructured](Template-02-unstructured/) | Unstructured data ingestion to S3 |
| 03 | [organization](Template-03-organization/) | Bronze layer data organization |
| 04 | [athena-performance](Template-04-athena-performance/) | Athena query performance optimization |
| 05 | [cdc-dms](Template-05-cdc-dms/) | Change Data Capture with DMS |
| 06 | [glue-catalog](Template-06-glue-catalog/) | AWS Glue Data Catalog management |
| 07 | [silver-transformation](Template-07-silver-transformation/) | Silver layer Spark transformations |
| 08 | [gold-aggregation](Template-08-gold-aggregation/) | Gold layer business aggregations |
| 09 | [spark-optimization](Template-09-spark-optimization/) | Spark job optimization techniques |
| 10 | [iceberg-setup](Template-10-iceberg-setup/) | Apache Iceberg table setup |
| 11 | [acid-merge](Template-11-acid-merge/) | ACID merge operations with Iceberg |
| 12 | [time-travel](Template-12-time-travel/) | Iceberg time travel queries |

## Prerequisites

- AWS account with appropriate permissions
- Python 3.9+
- PySpark (for Spark templates)
- boto3

## Usage

Each template folder contains:
- Solution Python script(s)
- README with exercise context and instructions
- Sample data (where applicable)
