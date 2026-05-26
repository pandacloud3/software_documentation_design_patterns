import csv
import json
from strategies import ConsoleExportStrategy, RedisExportStrategy, KafkaExportStrategy

def read_csv(file_path):
    """Окремий код для вичитки даних"""
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def get_strategy():
    """Читає config.json і повертає правильний клас стратегії"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    target = config.get("export_target", "console").lower()
    
    if target == "redis":
        return RedisExportStrategy(config["redis_host"], config["redis_port"])
    elif target == "kafka":
        return KafkaExportStrategy(config["kafka_server"], config["kafka_topic"])
    else:
        return ConsoleExportStrategy()

if __name__ == "__main__":
    dataset = read_csv('fire_inspections.csv')
    strategy = get_strategy()
    
    if dataset:
        strategy.export(dataset)