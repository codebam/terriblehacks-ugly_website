#!/usr/bin/env python3

import sys
from lxml import html
from urllib.request import urlopen
from io import StringIO, BytesIO


def open_website(url):
    try:
        raw_html = urlopen(url).read().decode('utf-8')
    except:
        sys.exit("couldn't download website, try another")
    return raw_html


def parse_website(myfile):
    try:
        lxml_tree = html.fromstring(myfile)
    except:
        sys.exit("couldn't open file")
    # print(myfile)
    return lxml_tree


def add_buttons(lxml_tree):
    # http://www.w3.org/WAI/wcag1AAA.png
    return 0

def add_to_footer(lxml_tree, image):
    lxml_tree.body.footer.append(html.Element("a"))
    return lxml_tree


def grab_images(lxml_tree):
    img_list = []
    for img in lxml_tree.xpath('//img/@src'):
        if (img[0:5]) not in ['http:', 'https:']:
            img = "http:" + img
        img_list.append(img)
        # print("img_list: " + str(img_list))
    return img_list


def main():
    meme_websites = ['https://imgflip.com/memetemplates']
    # you can add more websites here grab memes from

    # for meme_website in meme_websites:
    #     grab_images(meme_website)
    lxml_tree = parse_website(open_website(sys.argv[1]))

    lxml_tree.body.append(html.Element("footer"))
    lxml_tree = add_to_footer(lxml_tree, '')
    # add_buttons(lxml_tree)

    with open('index.html', 'wb') as f:
        f.write(html.tostring(lxml_tree, pretty_print=True, method="html"))


#   print(grab_images(parse_website(open_website("http://www.memes.com"))))
#   print(open_website(parse_website(grab_images("https://imgflip.com/memetemplates"))))
#   I'm being rate limited, have to fix it


if __name__ == "__main__":
        main()
