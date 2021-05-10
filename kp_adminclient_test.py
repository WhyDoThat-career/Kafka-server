from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic = NewTopic(
    name='flask_all_logs',
    num_partitions=1,
    replication_factor=1 
)
admin_client.create_topics([topic])