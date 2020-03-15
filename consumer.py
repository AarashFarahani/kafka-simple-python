from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers='192.168.56.108:9092')
for msg in consumer:
    print (msg.value)