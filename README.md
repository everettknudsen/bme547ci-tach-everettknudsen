# bme547ci-tach-everettknudsen

The is_tachycardic function passes in a string as an input, then rruns that string through a series of manipulations which remove trailing and leading spaces and punctuation, then make it all the same case before checking to see if there is a result. Each of these operations is broken into a function to ensure modular code.

The first function is remove_punctuation. This function replaces anything that is considered punctuation with a blank space (not a whitespace). Therefore, all trailing and leading punctuation can be removed.

The next function is to remove spaces. It works by using the string.strip() command to strip off trailing and leading spaces.

Next is a function to make the string all lowercase by using the string.lower() command.

Finally is a function which returns the Boolean result. Before comparison, the string is turned into a set of characters. This will show how many unique characters are in the string. For instance, in the word 'dad' there would be a 'd' and an 'a'. The number of characters in the set is then compared to the characters in the set for tachycardia. This allows for tolerance in the case that there is a missing letter or a number in the word. Finally, the Boolean result is returned.

A NOTE FOR THE GRADER: I have a few more commits than I had intended because I went through a few more iterations of the code than I originally thought I was going to. Initially, I didn't attempt the extra credit portion of the assignment and had a simple comparison. However, I decided to change this part and do the extra credit. Also, I initially had some trouble getting the Travis CI set up becuase I had pytest-cov in my .travis.yml file. I was able to get that resolved after lecture on Wednesday. 
