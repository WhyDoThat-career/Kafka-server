from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="52.78.62.228:9092", 
    client_id='test'
)

topic = NewTopic(
    name='test_topic2',
    num_partitions=1,
    replication_factor=1 
)
admin_client.create_topics([topic])