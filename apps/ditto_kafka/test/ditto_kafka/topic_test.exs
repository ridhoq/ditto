defmodule TopicTest do
  use ExUnit.Case

  alias DittoKafka.Topic, as: Topic

  test "gets kafka topic name" do
    {:ok, topic_name} = Topic.get_topic()
    assert System.get_env("KAFKA_CREATE_TOPICS") =~ topic_name
  end
end