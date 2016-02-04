if ! $?PYTHONPATH then
setenv PYTHONPATH "/home/8/bakshia/.local/lib/python2.7/site-packages"
else
setenv PYTHONPATH "/home/8/bakshia/.local/lib/python2.7/site-packages":$PYTHONPATH
endif
if ! $?NLTK_DATA then
setenv NLTK_DATA "/home/8/bakshia/nltk_data"
else
setenv NLTK_DATA "/home/8/bakshia/nltk_data":$NLTK_DATA
endif
