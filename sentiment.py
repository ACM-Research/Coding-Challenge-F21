import string
import math

def get_word_counts():
    """
    Iterates through each word of inputs.txt for each paragraph and
    checks to see if it exists in either positive_words or negative_words.
    The total amount of positive and negative words are each totaled up.
    """
    p_count = 0
    n_count = 0
    w_count = 0
    paragraphs = []

    with open('input.txt', 'r') as f:
        for line in f:
            if line != '\n':
                words_on_line = line.split()

                for word in words_on_line:
                    word = clean_word(word)
                    if word in positive_words:
                        p_count += 1
                    elif word in negative_words:
                        n_count += 1

                    w_count += 1
            else:
                paragraphs.append((p_count, n_count, w_count))
                p_count = 0
                n_count = 0
                w_count = 0
                continue

        paragraphs.append((p_count, n_count, w_count))

        return paragraphs

def get_scores(paragraphs):
    """
    Takes the summed word counts for each paragraph and converts
    them into a tangible sentiment score
    """
    scores = []

    for i, par in enumerate(paragraphs):
        score = squash(calc_score(par))
        
        scores.append(score)

    return scores

def clean_word(word):
    """
    Removes punctuations and makes words lowercase to match sample words lists
    """
    for char in string.punctuation:
        word = word.replace(char, '').lower()

    return word

def calc_score(par):
    """
    Calculates a score based on amount of positive and negative words
    that is also proportional to amount of total words
    """
    return (par[0] - par[1]) / par[2] * 100

def squash(score):
    """
    Squashes a given value to be within -10 and 10
    """
    adjustment = 7
    return math.tanh(score / adjustment) * 10

def get_avg(num_list):
    return sum(num_list) / len(num_list)


if __name__ == '__main__':
    with open('positive-words.txt', 'r') as f:
        positive_words = [line.strip() for line in f]

    with open('negative-words.txt', 'r') as f:
        negative_words = [line.strip() for line in f]

    paragraphs = get_word_counts()

    scores = get_scores(paragraphs)

    for i, score in enumerate(scores):
        print(f'Paragraph {i+1} has a sentiment score of {round(score, 2)}.')

    print(f'The sentiment score of the entire text is {round(get_avg(scores), 2)}.')