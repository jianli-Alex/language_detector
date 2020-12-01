#! /usr/bin/env python
# -*-coding: utf-8 -*-

import time
import requests
from lxml import etree
from runtime import cal_time
from cate import extract_cate
from sub_cate import extract_sub_cate


@cal_time
def extract_content(url_list, sleep_time):
    # create new url
    base_url = "http://odp.org"
    new_url_list = list(map(lambda x: base_url+x, url_list))

    # headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # init
    content_list = []

    # requests
    for url in new_url_list:
        try:
            # requests
            resp = requests.get(url, headers=headers)
            resp.encoding = "utf-8"
            # DOM tree
            tree = etree.HTML(resp.text)
            contents = tree.xpath('//li[@class="listings"]/p')
            # extract text
            for content in contents:
                content_list.append(content.xpath("string(.)"))
            # time sleep
            time.sleep(sleep_time)
        except Exception as error:
            pass
    return content_list


if __name__ == "__main__":
    url = "http://odp.org/World/Chinese_Simplified"
    lang_cate = url[(url.rfind("/") + 1):]
    cate_list = extract_cate(url)
    href_list = extract_sub_cate(url, lang_cate, cate_list)
    content_list = extract_content(href_list, 0.1)

    # write file
    with open("../data/"+lang_cate+".csv", "w+") as f:
        f.writelines(list(map(lambda x: x + "\n", content_list)))
    print(len(content_list))
    print(content_list[:10])
