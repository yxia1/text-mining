from mediawiki import MediaWiki
from imdb import Cinemagoer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


def imdb(movie_title):
    """This function takes a movie title (str) returns its first review"""
    ia = Cinemagoer()
    movie = ia.search_movie(movie_title)[0]
    movie_id = movie.movieID

    movie_reviews =  ia.get_movie_reviews(movie_id)
    return(movie_reviews['data']['reviews'][0]['content'])

#NLTK
def sentiment_analysis(text):
    """The function will take a str and return its polarity score"""
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score

def distribution(text):
    """The function takes a text and return word distribution exclusing stop words"""
    stop_words=set(stopwords.words("english"))
    tokenized_word=word_tokenize(text)
    filtered_sent = []
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sent.append(w)
    fdist = FreqDist(filtered_sent)
    return fdist

def main():
    wikipedia = MediaWiki()
    batman = wikipedia.page("The Batman (2022)")
    batman_content = str(batman.content)
    joker = wikipedia.page("Joker (2019)")
    joker_content = str(joker.content)
    batman_review = imdb("The Batman (2022)")
    # print(batman_review)
    joker_review = imdb('Joker (2019)')
    # print(joker_review)

    #sentiment_analysis
    print(sentiment_analysis(batman_content))
    print(sentiment_analysis(joker_content))
    print(sentiment_analysis(batman_review))
    print(sentiment_analysis(joker_review))

    #distribution using nltk
    batman_wiki_worddistr=distribution(batman_content)
    print(batman_wiki_worddistr.most_common(10))
    batman_wiki_worddistr.plot(30,cumulative=False)
    joker_wiki_worddistr=distribution(joker_content)
    print(joker_wiki_worddistr.most_common(10))
    joker_wiki_worddistr.plot(30,cumulative=False)
    plt.show()

# reference: https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk




if __name__ == "__main__":
    main()