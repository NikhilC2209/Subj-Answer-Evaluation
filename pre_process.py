import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

ques = "List out the linguistic properties of Multi-word expressions"

exp_ans = {
	"num_bullets": 5,
	"bullet_head": ["Lexical Idiomaticity", "Syntactic Idiomaticity", "Semantic Idiomaticity", "Pragmatic Idiomaticity", "Statistical Idiomaticity"],
	"bullet_text": ["Lexical idiomaticity occurs when one or more components of an MWE are not part of the conventional English lexicon", "Syntactic idiomaticity occurs when the syntax of the MWE is not derived directly from that of its components", "Semantic idiomaticity is the property of the meaning of a MWE not being explicitly derivable from its parts", "Pragmatic idiomaticity is the condition of a MWE being associated with a fixed set of situations or a particular context", "Statistical idiomaticity occurs when a particular combination of words occurs with markedly high frequency, relative to the component words or alternative phrasings of the same expression"]
}

def ans_dict(text):
	bullet_list = get_bullets(text)

def get_bullets(text):
	text_list = text.split("\n")
	text_list = [re.sub('[>\r]', '',i) for i in text_list if i[0]==">"]
	text_list = [i.strip() for i in text_list]
	return text_list

# def cosine_sim():
