str = ARGV
str_arr = []


str.each do |word|
  word_arr =  word.split("")
  word_arr.insert(rand(word.length), " ")
  str_arr << word_arr.join("")
end

p str_arr.join("")