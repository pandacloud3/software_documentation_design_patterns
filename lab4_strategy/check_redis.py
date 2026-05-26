import redis

client = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("Ключі в базі:", client.keys())
first_record = client.get("inspection:0")
print("\nДані під ключем 'inspection:0':")
print(first_record)