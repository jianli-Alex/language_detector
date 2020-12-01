#! /usr/bin/env python
# -*-coding: utf-8 -*-

"""
function: crawl information in various language in odp website
"""

import requests
from runtime import cal_time
from lxml import etree


# crawl origin website
@cal_time
def extract_cate(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"

    # DOM tree
    tree = etree.HTML(resp.text)
    # extract Subcategories
    sub_cate = tree.xpath('//ul[@id="triple"]/li')
    cate_list = []

    for cate in sub_cate:
        cate_list.append(cate.xpath("string(.)"))
    return cate_list


if __name__ == "__main__":
    url = "http://odp.org/World/Chinese_Simplified"
    cate_list = extract_cate(url)
    print(cate_list)
