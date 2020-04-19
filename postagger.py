import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.tag import pos_tag, pos_tag_sents
import re


fnames1 = ["W2_AI_MOdule_5.txt",
           "W2_AI_MOdule_6.txt",
           "W3_AI_MOdule_7.txt",
           "W3_AI_MOdule_8.txt",
           "W4_AI_MOdule_9.txt",
           "W4_AI_MOdule_10.txt",
           "W4_AI_MOdule_11-Eng-Transcription.txt",
           "W5_AI_MOdule_12-Eng-Transcription.txt",
           "W5_AI_MOdule_13-Eng-Transcription.txt",
           "W5_AI_MOdule_14-Eng-Transcription.txt",
           "W5_AI_MOdule_15-Eng-Transcription.txt",
           ]

fnames2 = ["FMFS_Module_1_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_2_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_4_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_5_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_6_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_7_Verified_Post_Verbatim_TScript.txt",
           "FMFS_Module_8_Verified_Post_Verbatim_TScript.txt",
           ]

fnames3 = ["News_1.txt"]

text = ""
inFile = open(fnames3[0], 'r')
text += inFile.read()

text = text.replace('’', "'")
text = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', text)

sents = sent_tokenize(text)
# print(sents)
for i, s in enumerate(sents):
    sents[i] = word_tokenize(s)

taggedsents = pos_tag_sents(sents)
# print(taggedsents)
for s in taggedsents:
    # print(s)
    for w, t in s:
        print(w, ":", t)
