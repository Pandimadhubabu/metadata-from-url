from bs4 import BeautifulSoup
import urllib.request
import os

def get_title(url):
    try:
        url_for_analyse = urllib.request.urlopen(url)
        mybytes = url_for_analyse.read()
        html_from_url = mybytes.decode("utf8")
        url_for_analyse.close()
        soup = BeautifulSoup(html_from_url, 'html.parser')
        url_title = soup.title.string
        #print(url_title)
        results_title.write('\n' + "\"" + url_title + "\"")
    except:
        #print("-")
        results_title.write('\n' + "\"-\"")

def get_description(url):
    try:
        url_for_analyse = urllib.request.urlopen(url)
        mybytes = url_for_analyse.read()
        html_from_url = mybytes.decode("utf8")
        url_for_analyse.close()
        soup = BeautifulSoup(html_from_url, 'html.parser')

        # First get the meta description tag
        description = soup.find('meta', attrs={'name': 'og:description'}) or soup.find('meta', attrs={
            'property': 'description'}) or soup.find('meta', attrs={'name': 'description'})

        # If description meta tag was found, then get the content attribute and save it to db entry
        if description:
            # entry.description = description.get('content')
            url_description = description.get('content')
            #print(url_description)
            results_description.write('\n' + "\"" + url_description + "\"")
        else:
           #print('-')
           results_description.write('\n' + "\"-\"")
    except:
        #print("-")
        results_description.write('\n' + "\"-\"")

#clear previous results
def clean_old_files():
    try:
        os.remove("title.txt")
        print('Old file Title.txt removed')
    except:
        print('File Title.txt not found')
    try:
        os.remove("description.txt")
        print('Old file description.txt removed')
    except:
        print('File description.txt not found')

# create file for results
clean_old_files()
results_title = open('title.txt', 'x')
results_description = open('description.txt', 'x')

# working with list of urls
file = open("domains.csv", "r")
num_lines = sum(1 for line in open('domains.csv'))

current_line = 1
for line in file:
    if __name__ == '__main__':
        print("line " + str(current_line) + " from " + str(num_lines) + " lines")
        current_line += 1
        if "http" in line:
            get_title(line)
            get_description(line)
        else:
            line = "https://" + line
            get_title(line)
            get_description(line)

file.close()
results_title.close()
results_description.close()

print("Done!")
