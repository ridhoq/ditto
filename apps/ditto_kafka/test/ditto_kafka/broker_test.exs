defmodule BrokerTest do
  use ExUnit.Case

  alias DittoKafka.Broker, as: Broker

  test "gets kafka broker from zookeeper" do
    {:ok, brokers} = Broker.get_brokers()

    assert length(brokers) == 1
    
    broker = hd(brokers)
    assert tuple_size(broker) == 2

    kafka_host = System.get_env("KAFKA_ADVERTISED_HOST_NAME")
    {kafka_port, _} = System.get_env("KAFKA_ADVERTISED_PORT") |> Integer.parse
    assert elem(broker, 0) == kafka_host
    assert elem(broker, 1) == kafka_port
  end
end