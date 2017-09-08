# -*- coding: utf-8 -*-
from urllib import request, parse
import json
import time
import configparser
from functools import reduce
import re

c = configparser.ConfigParser()
c.read("c.conf")

stars_match_id = c.get("match", "stars_id")
challenges_match_id = c.get("match", "challenges_id")

user_agent = c.get("app", "user_agent")
headers = { 'User-Agent' : user_agent }

base_url = c.get("app", "base_url")
auth_token = c.get("app", "auth_token")
now = time.time()

re_empty = re.compile("\s")

def formattime(buying_at):
    #print(time.localtime(time.time()))
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(buying_at))


def format_participants(participant):
    format_data = {}

    format_data["id"] = participant["id"]
    format_data["rank"] = participant["rank"]
    format_data["special"] = participant["special"]

    format_data["votes_count"] = participant["votes_count"]

    format_data["user_id"] = participant["user"]["id"]

    #re.sub
    format_data["user_name"] = re.sub(re_empty, "", participant["user"]["name"])

    format_data["stock_code"] = participant["stock"]["code"]
    format_data["stock_name"] = participant["stock"]["name"]
    format_data["stock_buying_price"] = participant["stock"]["buying_price"]
    format_data["stock_buying_at_str"] = formattime(participant["stock"]["buying_at"])
    format_data["stock_buying_at"] = participant["stock"]["buying_at"]

    temp = participant["stock"]["highest_price"]
    format_data["stock_highest_price"] = 0 if temp == "-" or temp == "明日计入" else temp

    temp = participant["stock"]["best_increase_percentage"]
    format_data["stock_best_increase_percentage"] = 0 if temp == "-" or temp == "明日计入" else temp

    return format_data


def do_request(url):
    #return python dict
    response = request.urlopen(url)
    page = response.read().decode('utf-8')
    return json.loads(page)

    """
    s=requests.Session()
    r = s.get("http://stock.yoomet.com/matches/150", headers = headers, timeout=5)
    j = r.content.decode('utf-8')
    return json.loads(j)
    """

def get_stars_reviews():
    """
    get url
    http://stock.yoomet.com/matches/107/reviews?auth_token=
    """
    querydata = {
        'auth_token':auth_token
    }
    url = base_url + stars_match_id + '/reviews?'
    url_postfix = parse.urlencode(querydata)

    request_result = do_request(url + url_postfix)

    return request_result["reviews"]


def format_brief_reviews(reviews):
    result = ""
    for i in reviews:
        result += "%s %s" % (i['title'], i['content'])
    return result


def raw_reviews():
    raw = []
    raw.append(get_stars_reviews())
    raw.append(get_challenges_reviews())
    return raw


def get_reviews():
    result = ""
    result += format_brief_reviews(get_stars_reviews())
    result += format_brief_reviews(get_challenges_reviews())
    return result


def get_challenges_reviews():
    """
    get url
    http://stock.yoomet.com/matches/106/reviews?auth_token=
    """
    querydata = {
        'auth_token':auth_token
    }
    url = base_url + challenges_match_id + '/reviews?'
    url_postfix = parse.urlencode(querydata)

    request_result = do_request(url + url_postfix)

    return request_result["reviews"]


def get_stars_matches():
    """
    get url
    http://stock.yoomet.com/matches/107/reviews?auth_token=
    """
    querydata = {
        'auth_token':auth_token
    }
    url = base_url + stars_match_id + '/?'
    url_postfix = parse.urlencode(querydata)

    request_result = do_request(url + url_postfix)

    match_full_content = []
    match_content = []
    all_participants = request_result["participants"]
    if "special_participants" in request_result:
        all_participants.extend(request_result["special_participants"])

    #print(all_participants)
    for p in all_participants:
        if 'stock' in p:
            match_content.append(format_participants(p))
            match_full_content.append(p)
    return match_content


def get_challenges_matches():
    """
    get url
    http://stock.yoomet.com/matches/106?page=1&auth_token=
    """

    match_full_content = []
    match_content = []
    page = 0
    total_count = 0

    while True:
        if page == 0:
            querydata = {
                'auth_token':auth_token
            }
        else:
            querydata = {
                'page':page,
                'auth_token':auth_token
            }

        url = base_url + challenges_match_id + '/?'
        url_postfix = parse.urlencode(querydata)
        request_result = do_request(url + url_postfix)

        #request url and format the result
        all_participants = request_result["participants"]
        total_count = request_result["participants_count"]

        for i in range(0, len(all_participants)):
            #print(page,i,total_count)
            match_content.append(format_participants(all_participants[i]))
            match_full_content.append(all_participants[i])

        #no next page
        if total_count < page * 10:
            break

        page = page + 1

    #end of while
    return match_content


def raw_matches():
    raw = get_stars_matches()
    raw.extend(get_challenges_matches())
    return raw


def format_brief_matches(matches):
    result = ""
    for i in matches:
        result += "【%s】在%s以 %.2f 价格买入[%s]%s;\n" % (
                    i['user_name'], i['stock_buying_at'],
                    i['stock_buying_price'], i['stock_code'],
                    i['stock_name']
                    )
    return result


def get_brief_matches():
    result = ""
    result += format_brief_matches(get_stars_matches())
    result += format_brief_matches(get_challenges_matches())
    return result


def __print_matches(matches):
    for i in matches:
        print(i)


def __print_test_line():
    print("......")
    print("......")
    print("......")
    print("......")
    print("......")


def print_brief_matches_to_excel(matches):
    """
    output = "".join(i \
                for i in \
                [ "%s++%s++%s\n" % (str(m["stock_code"]), m["stock_name"], str(m["stock_buying_price"])) for m in matches])
    """

    output = "\n".join(i
                for i in
                    [
                    reduce(lambda x, y : str(x) + "++" + str(y), list(m.values()))
                    for m in matches
                    ]
                )
    print(output)


def print_all_matches_to_excel(matches):
    output = "".join( str(i) + "\n" \
                for i in \
                [ m for m in matches])
    print(output)


def format_statics_result(list_data):
    #TODO

    i = 0
    output = ""
    for r in list_data:
        #ls["stock_buying_count"]) +
        s = "[%s]%s" % (str(r["stock_code"]), str(r["stock_name"]))
        output = output + s + "\n"
    #print(output)
    return output


if __name__ == '__main__':

    """
    TEST OK

    print(get_stars_reviews())
    __print_test_line()
    print(get_challenges_reviews())
    __print_test_line()
    print(get_reviews())
    __print_test_line()

    print(get_stars_matches())
    __print_test_line()
    print(get_challenges_matches())
    __print_test_line()
    print(get_brief_matches())
    __print_test_line()

    exit(0)
    """

    #print_brief_matches_to_excel(get_stars_matches())
    #print_brief_matches_to_excel(get_challenges_matches())

    m = raw_matches()
    print_brief_matches_to_excel(m)



#end
