defmodule TopicTest do
  use ExUnit.Case

  alias DittoKafka.Topic, as: Topic

  test "gets kafka topic name" do
    expected_topic = "some_juicy_topic"
    topic_str = [expected_topic, 2, 1]
                |> Enum.join(":")

    {:ok, topic} = Topic.get_topic(topic_str)
    assert expected_topic == topic
  end

  test "gets kafka partition count" do
    expected_partitions = 2
    topic_str = ["some_juicy_topic", expected_partitions, 1]
                |> Enum.join(":")

    {:ok, partitions} = Topic.get_partitions(topic_str)
    assert expected_partitions == partitions
  end
end