defmodule KafkaUtilTest do
  use ExUnit.Case

  alias DittoUtil.KafkaUtil, as: KU

  test "gets kafka broker from zookeeper" do
    zookeeper_host = System.get_env("KAFKA_ZOOKEEPER_CONNECT")
    IO.puts("#{zookeeper_host}")
    {:ok, brokers} = KU.get_kafka_brokers(zookeeper_host)

    assert length(brokers) == 1
    
    broker = hd(brokers)
    assert tuple_size(broker) == 2

    kafka_host = System.get_env("KAFKA_ADVERTISED_HOST_NAME")
    {kafka_port, _} = System.get_env("KAFKA_ADVERTISED_PORT") |> Integer.parse
    assert elem(broker, 0) == kafka_host
    assert elem(broker, 1) == kafka_port
  end
end