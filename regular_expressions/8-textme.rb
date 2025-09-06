#!/usr/bin/env ruby

line = ARGV[0]

# Extract sender, receiver, and flags using regex
match = line.match(/from:([^\]]+).*to:([^\]]+).*flags:([^\]]+)/)

if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
end
