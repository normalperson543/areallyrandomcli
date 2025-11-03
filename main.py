import requests
from bs4 import BeautifulSoup

def getForumHome():
    request = requests.get("https://scratch.mit.edu/discuss")
    req_text = request.text
    soup = BeautifulSoup(req_text)
    #print(soup)
    categories = []
    # Let's get the forums first.
    idx1 = soup.select_one("#idx1") #get the container with the categories
    for category in idx1.select(".box"):
        category_name = category.select_one(".box-head h4").text
        category_dict = {
            "category_name": category_name,
            "forums": []
        }
        forum_tbody = category.select(".box-content table tbody")
        for forum_tr in forum_tbody:
            forum_name = forum_tr.select_one("tr .tcl .intd .tclcon h3")
            forum_id = forum_tr.select_one("tr .tcl .intd .tclcon h3 a").get("href").split("/discuss/")[1].split("/")[0]
            forum_desc = forum_tr.select_one("tr .tcl .intd .tclcon").text
            topic_count = forum_tr.select_one("tr .tc2").text
            post_count = forum_tr.select_one("tr .tc3").text
            forum_dict = {
                "title": forum_name,
                "id": int(forum_id),
                "description": forum_desc,
                "topic_count": int(topic_count),
                "post_count": int(post_count),
            }
            category_dict["forums"].append(forum_dict)
        categories.append(category_dict)
    print(categories)





print("Scratch Forum CLI-ent")
print("for the Midnight challenge")

getForumHome()
