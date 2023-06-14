import spacy

#Movie descriptions
movie_descriptions = """
Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek "The Hidden World", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.
Movie B :After the death of Superman, several new people present themselves as possible successors.
Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.
Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.
Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.
Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.
Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.
Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.
Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.
Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney.
"""

#Implement the function that will find the most similar movie based on the given description
def find_similar_movie(description):
    # Load Spacy's 'en_core_web_md' model
    nlp = spacy.load('en_core_web_md')
    
    #Extract movie titles from the movie_descriptions
    movie_list = [line.split(" :")[0] for line in movie_descriptions.split("\n") if line]
    
    #Convert the target description to a Spacy document
    target_description = nlp(description)
    
    #List to store movie similarities
    similarities = []
    
    #Iterate over each line in movie_descriptions
    for line in movie_descriptions.split("\n"):
        if line:
            #Split the line into title and movie_description
            title, movie_description = line.split(" :")
            #Calculate similarity between movie_description and target_description
            similarity = nlp(movie_description).similarity(target_description)
            #Append title and similarity to similarities list
            similarities.append((title, similarity))
    
    #Sort the similarities list in descending order based on similarity score
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    #Extract the title of the most similar movie
    most_similar_movie = similarities[0][0]
    
    #Return the most similar movie title
    return most_similar_movie


#Using "find_similar_movie" function to find the most similar movie  
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = find_similar_movie(description)
print("Next movie to watch:", most_similar_movie)



