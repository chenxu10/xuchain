require 'sinatra'
require 'colorize'
require 'active_support/time'
require_relative 'client'
require_relative 'helpers'

def update_state_interval()
    every(2.seconds) do
        puts "My favourite movie is #{@favorite_movie}."
        update_state(PORT => [@favorite_movie, @version_number])
        @favorite_movie = MOVIES.sample
        @version_number += 1
        puts "Screw #{@favorite_movie}"
    end
end

if __FILE__ == $PROGRAM_NAME
    PORT, PEER_PORT = ARGV.first(2)
    MOVIES = File.readlines("movies.txt").map(&:chomp)
    STATE = ThreadSafe::Hash.new
    @favorite_movie = MOVIES.sample
    @version_number = 0


    update_state_interval()
end