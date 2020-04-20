import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.tag import pos_tag, pos_tag_sents
import operator

fnames1 = {"data/W2_AI_MOdule_5.txt",
           "data/W2_AI_MOdule_6.txt",
           "data/W3_AI_MOdule_7.txt",
           "data/W3_AI_MOdule_8.txt",
           "data/W4_AI_MOdule_9.txt",
           "data/W4_AI_MOdule_10.txt",
           "data/W4_AI_MOdule_11-Eng-Transcription.txt",
           "data/W5_AI_MOdule_12-Eng-Transcription.txt",
           "data/W5_AI_MOdule_13-Eng-Transcription.txt",
           "data/W5_AI_MOdule_14-Eng-Transcription.txt",
           "data/W5_AI_MOdule_15-Eng-Transcription.txt",
           }

fnames2 = {"data/FMFS_Module_1_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_2_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_4_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_5_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_6_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_7_Verified_Post_Verbatim_TScript.txt",
           "data/FMFS_Module_8_Verified_Post_Verbatim_TScript.txt",
           }
text = ""
for fname in fnames2:
    inFile = open(fname, 'r')
    text += inFile.read()

text = text.replace('’', "'")

verbs = {}
sents = sent_tokenize(text)
# print(sents)
for i, s in enumerate(sents):
    sents[i] = word_tokenize(s)

taggedsents = pos_tag_sents(sents)
# print(taggedsents)
for s in taggedsents:
    # print(s)
    for w, t in s:
        if t in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            # print(w)
            if (verbs.get(w.lower()) is not None):
                verbs[w.lower()] += 1
            else:
                verbs[w.lower()] = 1

sorted_verbs = sorted(verbs.items(), key=operator.itemgetter(1))
sorted_verbs.reverse()

i = 0
for v, c in sorted_verbs:
    # if i >= 40:
    #     break
    # else:
    #     i += 1
    print(v)
    # print(v, " : ", c)
