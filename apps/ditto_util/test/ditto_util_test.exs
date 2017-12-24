defmodule DittoUtilTest do
  use ExUnit.Case
  doctest DittoUtil

  test "greets the world" do
    assert DittoUtil.hello() == :world
  end
end
