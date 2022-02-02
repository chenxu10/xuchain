require 'sinatra'
require 'colorize'

BALANCES = {
  'hasseb' => 1_000_000
}

get "/balance" do
  username = params['user']
  puts BALANCES.to_s.yellow
  "#{username} has #{BALANCES[username]} amount of money"
end

# @param name
post "/users" do
  name = params['name']
  BALANCES[name] ||= 0
  puts BALANCES.to_s.yellow
  "OK"
end

# @param from
# @param to
# @param amount
post "/transfers" do
    from, to = params.values_at('from','to').map(&:downcase)
    amount = params['amount'].to_i
    raise unless BALANCES[from] > amount
    BALANCES[from] -= amount
    BALANCES[to] += amount
    puts BALANCES.to_s.yellow
    "OK"
end

class InsufficientFunds < StandardError; end