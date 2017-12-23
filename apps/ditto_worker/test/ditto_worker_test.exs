defmodule DittoWorkerTest do
  use ExUnit.Case
  doctest DittoWorker

  test "greets the world" do
    assert DittoWorker.hello() == :world
  end
end
