# Create a sentence-generator program:
# a. The prepositional phrase is optional. (It can appear with a certain probability.)
# b. A conjunction and a second independent clause are optional: The boy took a drink and the girl played baseball.
# c. An adjective is optional: The girl kicked the red ball with a sore foot.

import random as r


def generate_sentence():
    subjects = ["The boy", "The girl", "The cat", "The dog"]
    verbs = ["kicked", "ate", "threw", "caught"]
    objects = ["the ball", "the bat", "the frisbee", "the shoe"]
    prepositions = ["in", "on", "at", "under"]
    conjunctions = ["and", "but", "or", "nor"]
    adjectives = ["red", "blue", "green", "yellow"]

    sentence = r.choice(subjects) + " " + r.choice(verbs) + " " + r.choice(objects) + " " + \
        r.choice(prepositions) + " " + r.choice(subjects) + \
        " " + r.choice(conjunctions) + " " + r.choice(adjectives)
    print(sentence)


generate_sentence()
