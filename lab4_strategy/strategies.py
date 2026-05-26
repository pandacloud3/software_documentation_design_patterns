import json
from abc import ABC, abstractmethod

class IExportStrategy(ABC):
    @abstractmethod
    def export(self, data: list):
        pass

class ConsoleExportStrategy(IExportStrategy):
    def export(self, data: list):
        print("\n--- ЕКСПОРТ У КОНСОЛЬ ---")
        for row in data:
            print(row)
        print("-------------------------\n")

class RedisExportStrategy(IExportStrategy):
    def __init__(self, host, port):
        import redis
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def export(self, data: list):
        import time
        print(f"\n--- ЕКСПОРТ У REDIS ({len(data)} записів) ---")
        for i, row in enumerate(data):
            timestamp = int(time.time() * 1000)
            unique_key = f"inspection:{timestamp}_{i}"
            
            self.client.set(unique_key, json.dumps(row))
            
        print("Успішно записано в Redis!\n")

class KafkaExportStrategy(IExportStrategy):
    def __init__(self, bootstrap_servers, topic):
        from kafka import KafkaProducer
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def export(self, data: list):
        print(f"\n--- ЕКСПОРТ У KAFKA ({len(data)} записів) ---")
        for row in data:
            self.producer.send(self.topic, value=row)
        self.producer.flush()
        print("Успішно відправлено в Kafka!\n")