require 'sinatra'
require 'colorize'

BALANCES = {
  'hasseb' => 1_000_000
}

get "/balance" do
  username = params['user']
  "#{username} has #{BALANCES[username]} coins"
end

# @param name
post "/users" do
  name = params['name'].downcase
  BALANCES[name] ||= 0
  "OK"
end

# @param from
# @param to
# @param amount
post "/transfers" do
  from, to = params.values_at('from', 'to').map(&:downcase)
  amount = params['amount'].to_i
  raise InsufficientFunds if BALANCES[from] < amount
  BALANCES[from] -= amount
  BALANCES[to] += amount
  print_state
  "OK"
end

class InsufficientFunds < StandardError; end