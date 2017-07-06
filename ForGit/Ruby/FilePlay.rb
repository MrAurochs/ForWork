# a computer program to take a file, extract all the code and write it in two new files, 
# I'm actually quite proud of this program even though it seems fairly simple because it represents a "jump" in my 
# coding skills from just doing things within the box of the interpreter to modifying actual files
#I could have done this regular expressions....if I was feeling masochistic.

file_x = ARGV.first
txt = File.open(file_x, "r") 


prompt = "> " 

puts "Here's your file: #{file_x}"

y_name = file_x.to_s + "_code.rb"
z_name = file_x.to_s + "_comments.rb"

file_y = File.new(y_name, "w")
file_z = File.new(z_name, "w")

puts file_y
puts file_z

block_comment_flag = false

txt.each do |line|
	tmp = ""
	cmt = ""
	#the purpose of this is to separate each line into code and comment parts 
	#obviously, most lines are all comment or all code, but sometimes not and that's the tricky part
	if block_comment_flag
		cmt_flag = true
	else
		cmt_flag = false 
	end
    	
	line.each_byte do |byte|
		if cmt_flag
			cmt += byte.chr
		elsif byte.chr == "#"
			cmt_flag = true
			cmt += byte.chr
		else
			tmp += byte.chr
		end 
	end 
	#now check if we have a begin or an end minding that the end will be in a commented section
	#now you have to check to see whether it's the beginning or end of a block comment
	if tmp[0..6] == "=begin "
		block_comment_flag = true
		cmt += tmp
		tmp = "" 
		
	elsif cmt[0..4] == "=end " 
	#this is ugly, and I think you can do this with recursion..but you would have to set it up correctly
	#with a checkline function that does everything..but I'm intellectually lazy right now so I won't do it
		block_comment_flag = false
		tmp = cmt[5..-1].to_s
		cmt = "=end "
		tmp_2 = ""
		flag = false
		
		tmp.each_byte do |x|
			if flag
				cmt += x.chr
			elsif x.chr == "#"
				cmt += x.chr
				flag = true
			else 
				tmp_2 += x.chr
			end
		end
		tmp = tmp_2
	end	

	#write the code part to file_y and write the comment part to file_z 
	file_y.write(tmp)
	file_z.write(cmt) 
#finally the loop ends	
end

puts "||||||||you should have two new fils now with names beginning with the name of the file one contains the comments, the other contains the code|||||||"


