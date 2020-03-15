# Simple app for produce and consume

## Run Apache Kafka and develop a simple application that produce and consume a message with python

For run the Apache Kafka you should follow the instruction:

* Download Apache Kafka
* Go to your /{kafka_path}/bin
* Run the zookeper

***
    ./zookeeper-server-start.sh ../config/zookeeper.properties
***

* Run the kafka server

***
    ./kafka-server-start.sh ../config/server.properties
***

* Create topics: following command create a topic with 1 replica and 1 partition which name is test

***
    ./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
***

* You can check all your topics and ensure your topic has been created

***
    ./kafka-topics.sh --list --zookeeper localhost:2181
***

* It should be show "test"
* If everything right so your apache kafka is up
* You can produce message with following command

***
    ./kafka-console-producer.sh --broker-list localhost:9092 --topic test
***

* You can consume messages from beginning with following command

***
    ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
***
