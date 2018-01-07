defmodule ProducerAgentTest do
  use ExUnit.Case, async: true

  alias DittoKafka.ProducerAgent, as: ProducerAgent

  setup do
    {:ok, agent} = start_supervised(ProducerAgent)
    %{agent: agent}
  end

  test "gets current partition from the producer", %{agent: agent} do
    assert ProducerAgent.get_current_partition(agent) == 0
  end
end