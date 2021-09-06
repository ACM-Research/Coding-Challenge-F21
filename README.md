# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!



## Rohans updates

Sentiment Analysis falls under "Classification", a machine learning method that uses data to determine the category, type, or class of an item or row of data. 

The goal here is to extract words from each sentence, form n-grams and classify the category of those sentences based on those n-grams.

I used Microsofts Azure Text Analytics Service to do the sentiment analysis of the paragraphs in the input text file.

The Text Analytics API is a cloud-based service that provides Natural Language Processing (NLP) features for text mining and text analysis,including sentiment analysis.

here is a reference to the document I followed - 
https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-sentiment-analysis?tabs=version-3-1#view-the-results

tried this console after creating the resource - 
https://eastus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-0/operations/Sentiment/console


followed this coding reference - https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_analyze_sentiment.py

I ran the code and got the sentiment classification for each of the three paragraphs

using the code here (sentiment-analysis) , produced the putput for each of the paragraphs at a paragraph level and at a sentence level using this API.

The output for each of the paragraphs as well as the overall response is included here as json files.

My observations on the outcome and my interpretation :

For context, this excerpt is from the famous novel "Fahrenheit 451" which I had the pleasure of reading in Middle School. Compared to the piece of code ,which has limited knowledge of the overall book, I have the overall context of the book and understand the deeper meaning the book conveys. Nevertheless this makes it easier for me to make sure that the code is outputting the correct information 

The first paragraph was an argument between Captain Beatty and Guy Montag over the importance of books as both of them quote books. However, the argument wasn't civil, the argument was passionate as each side used words like "dreary" and "chaos" to emphasize their points. The program seems to agree with the sentiment as well as it detected words like "dreary" and "chaos" to output that the paragraph was negative. 

The second paragraph followed suit with the first paragraph. However, this time it escalated to a full on fight between Captain Beatty and Guy Montag as they both insult each one another using words like "murder". The program has also caught this as the output came as negative as it has read those words like "murder" to figure out that the paragraph is negative. 

The third paragraph was different compared to the first and second paragraph. As a reader, reading the third paragraph gave me mixed feelings as there were many words that had negative connotations and positive connotations mixed together. The program seems to agree as it also tried calculating the polarity of the negativeness and the positiveness of the and got equal polarity. As a result of this equality the program also outputted mixed as well. 
