#Open the text file
import re



def check_match(tests, words):
	pattern = '[)(]'
	test_case = 1
	for test in tests:
		
		count = 0
		for word in words:
			pattern = r'(\w+)+'
			pattern_2 = r'[^(\w+)]\w+'
			x = re.findall(pattern, test)
			#print(x,test,word)
			if len(x) == lenght_L and (word[0] in x[0]) and (word[1] in x[1]) and (word[2] in x[2]):
				count += 1
			elif len(test) == len(word) and (word[0] in test[0]) and (word[1] in test[1]) and (word[2] in test[2]):
				count += 1
			elif len(x) < lenght_L:
				
					
				continue
			
			
		print( "Case #{}: {}".format(test_case,count))
		test_case += 1	
			

words_D = ''
lenght_L = ''
tests_N = ''
def read_file():
	txtFile = open('C:/MVGT-Personal/test.in','r')
	print("Reading the test.in file.....")
	
	count = 0
	words = []
	tests = []
	for line in txtFile:
		pattern = '\d'
		if count==0:
			x = re.findall(pattern, line)
			lenght_L = int(x[0])
			words_D = x[1]
			tests_N = x[2]
		else:
			if count <= int(words_D):
				words.append(line.strip())
			else:
				tests.append(line.strip())
		count += 1

	txtFile.close()

	check_match(tests,words)
	print(words)
	print(tests)

read_file()