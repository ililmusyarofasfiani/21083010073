from pyspark.sql import SparkSession
import pandas as pd 

def read_and_write_sales_data():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("write data warehouse") \
        .config("spark.jars", "/home/arviano/Downloads/postgresql-42.2.24.jar," 
                              "/home/arviano/spark-excel_2.12-0.13.7.jar,"
                              "/home/arviano/Downloads/xmlbeans-3.1.0.jar,"
                              "/home/arviano/Downloads/poi-ooxml-5.0.0.jar,"
                              "/home/arviano/Downloads/poi-ooxml-schemas-4.1.2.jar") \
        .config("spark.hadoop.fs.defaultFS", "file:///")\
        .getOrCreate()

     # Path to the excel file
    excel_file_path = "/home/arviano/spark_warehouse/rentalok_data_cleaned.xlsx"

    # Read data from the Excel file
    df = spark.read.format("com.crealytics.spark.excel") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .option("dataAddress", "Sheet1") \
        .load(excel_file_path)

    
    # Detail koneksi PostgreSQL (dwh)
    jdbc_url_olap = "jdbc:postgresql://localhost:5432/db_olap"
    jdbc_properties_olap = {
        "user": "postgres",
        "password": "1234",
        "driver": "org.postgresql.Driver"
    }

    # Menulis data ke tabel di database dwh
    df.write.jdbc(url=jdbc_url_olap, table='dwh', mode='overwrite', properties=jdbc_properties_olap)
    
    # Menghentikan SparkSession
    spark.stop()

if __name__ == "__main__":
    read_and_write_sales_data()