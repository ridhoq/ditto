defmodule DittoKafka.Topic do
  @moduledoc """
  Documentation for DittoKafka.Topic
  Responsible for parsing kafka topics in the following format:
  https://github.com/wurstmeister/kafka-docker#automatically-create-topics
  """

  def get_topic(topic_str) do
    topic = String.split(topic_str, ":") |> hd
    {:ok, topic}
  end

  def get_partitions(topic_str) do
    partitions = String.split(topic_str, ":")
                 |> Enum.at(1)
                 |> String.to_integer
    {:ok, partitions}
  end

end
