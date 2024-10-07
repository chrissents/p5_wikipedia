# function to return list of lnks
import wikipediaapi
import time

user_agent = "p5_wikipedia (christopherwang727@icloud.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

# function to return list of links
def fetch_links(page):
    link_list = []
    links = page.links

    for title in links.keys():
        link_list.append(title)

    return link_list

def wikipedia_game_solver(start_page, target_page):
    links_links(start_page)

    # make a loop that checks every item and prints out a message if
    # target_page.title is in that list




# start and end pages for our wikipedia game solver
start_page = wiki.page("Holocaust")
target_page = wiki.page("My Little Pony")
wikipedia_game_solver(start_page, target_page)

page = [start_page, target_page]
for target_page in links_list:
    print(target_page)
    
print(fetch_links(start_page))