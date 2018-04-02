import requests
import csv
from pprint import pprint
from bs4 import BeautifulSoup

USER_AGENT = {'User_Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def snatcher(search_term, results_number, lang):
    """Get HTML data"""
    clean_search_term = search_term.replace(' ','+')
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(
        clean_search_term,
        results_number,
        lang
    )

    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    return response.text

def parser(html):
    """Parse HTML data"""
    soup = BeautifulSoup(html, 'html.parser')
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class':'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class':'r'})        
        description = result.find('span', attrs={'class','st'})

        if link and title:            
            link = 'google.com'+link['href']            
            unclean_title = title.get_text()
            title = unclean_title.replace(', ', ' ')

            if description:                
                unclean_description = description.get_text()
                description = unclean_description.replace(", ","").replace("\n", '')
                print(description)
            if link != '#':
                    found_results.append({
                        'Rank': rank, 
                        'Link': link,
                        'Title': title, 
                        'Description': description
                        })
                    rank+=1
                    
    
    return found_results
        
def dumper(results):
    with open('searchresults.csv','w') as outfile:
        fieldnames = ['Rank', 'Link', 'Title', 'Description']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


html = snatcher('linux', 10, 'en')
results = parser(html)
dumper(results)