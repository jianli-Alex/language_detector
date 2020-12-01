#! /usr/bin/env python
# -*-coding: utf-8 -*-

import re
import requests
import html
from runtime import cal_time
from cate import extract_cate
from lxml import etree


@cal_time
def extract_sub_cate(url, lang_cate, cate_list):
    # re pattern
    pattern = re.compile('(?<=href=)\"(.*)\"(?=\s)')
    # headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # save sub_cate and href
    href_list = []

    # create new url with cate_list
    for cate in cate_list:
        # requests
        new_url = url + "/" + cate
        resp = requests.get(new_url, headers=headers)
        resp.encoding = "utf-8"

        # DOM tree
        tree = etree.HTML(resp.text)
        sub_cate = tree.xpath('//ul[@id="triple"]/li')

        for c in sub_cate:
            # change to binary string, and decode from utf-8 to unicode
            link = etree.tostring(c).decode("utf-8")
            # extract href
            link = pattern.findall(link)[0]
            # change normal encoding from html encoding by html lib
            link = html.unescape(link)
            href_list.append(link)

    # drop_duplicates
    href_list = list(set(href_list))
    href_list = list(filter(lambda x: lang_cate in x, href_list))
    return href_list


if __name__ == "__main__":
    url = "http://odp.org/World/Chinese_Simplified"
    lang_cate = url[(url.rfind("/")+1):]
    cate_list = extract_cate(url)
    href_list = extract_sub_cate(url, lang_cate, cate_list)
    print(href_list)
    print(len(href_list))
