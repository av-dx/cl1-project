from nltk import pos_tag as pt
import re
import nltk.tokenize as tk


# fsm_m1 = open("FMFS_Module_1_Verified_Post_Verbatim_TScript.txt", "r")
# text = fsm_m1.read()
# module_test = 1


# print("%-20s %-8s %s\n" %("Token", "Tag", "Corrected Tag"))

# for sent in tagged_data:
#     for word in sent:
#         print("%-20s %-8s %s" %(word[0], word[1], word[1]))


# fsm_m1.close()


with open('FMFS_Module_1_Verified_Post_Verbatim_TScript.txt', mode='r') as f:
	for i in range(3):            # for ignoring the forst three lines (details about the module)
		f.readline()

	module_text = f.read()
	module_text = re.sub(r'([A-Za-z])/([a-zA-Z])', r'\1 / \2', module_text)
	module_text = re.sub(r'([a-z])\.([A-Z])', r'\1\. \2', module_text)
	sentences = tk.sent_tokenize(module_text)

	tagged_data = []

	for sent in sentences:
		tagged_data.append(pt(tk.word_tokenize(sent)))
	# print(tagged_data)
	for sent in tagged_data:
		for token in sent:
			print("%-25s %-4s" %(token[0], token[1]))	