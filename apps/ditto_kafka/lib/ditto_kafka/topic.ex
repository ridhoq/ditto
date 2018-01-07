defmodule DittoKafka.Topic do
  @moduledoc """
  Documentation for DittoKafka.Topic
  """

  def get_topic() do
    kafka_create_topics = Application.get_env(:ditto_kafka, :kafka_create_topics)
    topic_name = String.split(kafka_create_topics, ":") |> hd
    {:ok, topic_name}
  end

  def get_partition_count() do
    kafka_create_topics = Application.get_env(:ditto_kafka, :kafka_create_topics)
    partition_count = String.split(kafka_create_topics, ":")[1] |> Integer.parse
    {:ok, partition_count}
  end

end
