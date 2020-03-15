from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.56.108:9092')
producer.send('test', b'some_message_bytes')
producer.flush()