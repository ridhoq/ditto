defmodule DittoKafka.ProducerAgent do
  @moduledoc """
  Documentation for DittoKafka.ProducerAgent
  Responsible for maintaining round robin paritioning state
  """

  use Agent
  alias DittoKafka.Topic, as: Topic

  @doc"""
  Start the agent with a current_partition of 0 and partition_count from DittoKafka.Topic
  """
  def start_link(_opts) do
    {:ok, partitions} = Topic.get_partitions(Application.get_env(:ditto_kafka, :kafka_create_topics))
    Agent.start_link(fn -> %{current_partition: 0, partitions: partitions} end)
  end

  @doc"""
  Get the current partition from the agent
  """
  def get_current_partition(agent) do
    Agent.get(agent, &Map.get(&1, :current_partition))
  end
end
