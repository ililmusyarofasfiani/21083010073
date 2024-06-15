#CLEANSING DAN STANDARISASI DATA

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim, lower, datediff, lit, when
import pandas as pd

def main():
    # Membuat Spark Session
    spark = SparkSession.builder \
        .appName("Cleaning and Standardizing Data") \
        .config("spark.jars", "/home/arviano/Downloads/postgresql-42.2.24.jar") \
        .getOrCreate()

    # Detail koneksi PostgreSQL
    jdbc_url = "jdbc:postgresql://localhost:5432/rentalok"
    properties = {
        "user": "postgres",
        "password": "1234",
        "driver": "org.postgresql.Driver"
    }

    # Membaca tabel transaksi dari PostgreSQL ke DataFrame Spark
    df_transaksi = spark.read.jdbc(url=jdbc_url, table="transaksi", properties=properties)

    # Cleaning dan Standarisasi Data
    df_cleaned = df_transaksi \
        .dropna(subset=["sewa_id", "mobil_id", "pelanggan_id", "pembayaran_id", "tanggal_sewa", "tanggal_kembali"]) \
        .dropDuplicates() \
        .withColumn("model", upper(trim(col("model")))) \
        .withColumn("nama", upper(trim(col("nama")))) \
        .withColumn("metode_pembayaran", trim(lower(col("metode_pembayaran"))))

    # Tambahkan Kolom jumlah_hari
    df_cleaned = df_cleaned.withColumn(
        "jumlah_hari",
        datediff(col("tanggal_kembali"), col("tanggal_sewa"))
    )

    # Tambahkan Kolom keterangan
    df_cleaned = df_cleaned.withColumn(
        "keterangan",
        when(col("jumlah_hari") > 365, "Denda berlaku karena lebih dari satu tahun").otherwise("Tidak ada denda")
    )
# Mengonversi DataFrame Spark ke DataFrame Pandas dan menyimpan ke file Excel
    pandas_df = df_cleaned.toPandas()
    pandas_df.to_excel("/home/arviano/spark_warehouse/rentalok_data_cleaned.xlsx", index=False)

    # Pastikan sesi Spark dihentikan setelah penggunaan
    spark.stop()

if __name__ == "_main__":
    main()