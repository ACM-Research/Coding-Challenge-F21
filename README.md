## Approach
When thinking of how to approach this problem, my first thought was to find a list of both positive and negative words in order to check the words in the input file against them. After some digging, I found two very helpful text files that could easily be imported, GitHub links linked below. The ideas for the rest of the program were to take the total counts of the positive and negative words, respectively, and to assign a score based on which type of word was more frequent and the total length of the text. I decided to calculate a score for each paragraph due to how different they were in the input file. I also had the scores be between a value of -10 and 10 by using a function to squash the possible values to within that range. I then outputted the scores for each paragraph and took their averages to show a total sentiment score for the whole text.

## Explanation
The program first imports the words from each of the dictionary files and places them into their own respective lists. Then it iterates through each of the words in input.txt, removing any punctuations attached the word and checking it against the two word lists. A count is added to either p_count or n_count if it matches a positive or negative word. w_count is also incremented for each word. After each line, there is a check to see if the line is empty, which indicates a new paragraph. If so, the three counts are appended to a paragraphs list, and are then reset for the next paragraph. Once all the counts are summed, a score is then calculated for each paragraph by subtracting the positive count by the negative count and dividing that value by the word count of the paragraph. This new score value is put through a tanh function and multiplied by ten to put it in a range of -10 and 10. The new scores, in this case being -2.58 for the first paragraph and 7.69 for the second paragraph, are then outputted. These values are pretty close to what I expected them to be, since the first paragraph contained quite a few strong emotional words yet still had some positive ones, so it felt more neutral in nature, while the second paragraph contained many positive descriptions of the man and overall had a calming tone. The paragraph scores are then averaged to make a sentiment score for the whole file, which in this case is 2.56.

## Sources
Positive and negative word lists taken from:
https://gist.github.com/mkulakowski2/4289437 and
https://gist.github.com/mkulakowski2/4289441

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
      Proceedings of the ACM SIGKDD International Conference on Knowledge 
      Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
      Washington, USA, 
Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
      and Comparing Opinions on the Web." Proceedings of the 14th 
      International World Wide Web conference (WWW-2005), May 10-14, 
      2005, Chiba, Japan.

