defmodule DittoUtil.KafkaUtil do
  @moduledoc """
  Documentation for DittoUtil.KafkaUtil
  """

  alias Zookeeper.Client, as: ZK

  @doc """
  Gets registered kafka brokers from zookeeper
  """
  def get_kafka_brokers(zookeeper_host) do
    {:ok, pid} = ZK.start_link(zookeeper_host)
    brokers_path = "/brokers/ids"
    broker_ids = ZK.get_children!(pid, brokers_path)
    brokers = 
        Enum.map(broker_ids, fn(broker_id) -> 
            {:ok, broker_json} = ZK.get(pid, "#{brokers_path}/#{broker_id}")
            broker = elem(broker_json, 0) |> Poison.decode!
            {broker["host"], broker["port"]}
         end)
    :ok = ZK.close(pid)
    {:ok, brokers}
  end
end