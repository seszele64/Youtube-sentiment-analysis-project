# spark_session_manager.py

from pyspark.sql import SparkSession

class SparkSessionManager:
    _spark_session = None

    @classmethod
    def get_spark_session(cls, app_name="YouTube Analysis"):
        if cls._spark_session is None:
            cls._spark_session = SparkSession.builder \
                                .appName(app_name) \
                                .config("spark.executor.memory", "4g") \
                                .config("spark.executor.cores", "4") \
                                .config("spark.dynamicAllocation.enabled", "true") \
                                .config("spark.dynamicAllocation.minExecutors", "1") \
                                .config("spark.dynamicAllocation.maxExecutors", "10") \
                                .getOrCreate()
        return cls._spark_session


