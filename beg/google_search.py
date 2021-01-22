import webbrowser

required = input("Please enter what you want to search about:")

webbrowser.open('https://www.youtube.com/results?search_query=' + required) #youtube search
webbrowser.open_new_tab('https://www.google.com/search?q='+ required) #google search