from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'index.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	word2count = {}
	for word in wordlist:
		if word in word2count.keys():
			word2count[word] += 1
		else:
			word2count[word] = 1
	sortedwords = sorted(word2count.items(),key = operator.itemgetter(1),reverse = True)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})
