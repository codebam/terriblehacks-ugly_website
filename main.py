#!/usr/bin/env python3

import sys
from lxml import html, etree
from urllib.request import urlopen


def open_website(url):
    try:
        raw_html = urlopen(url).read().decode('utf-8')
    except:
        sys.exit("couldn't download website, try another")
    return raw_html


def parse_website(myfile):
    try:
        # soup = BeautifulSoup(myfile)
        # soup BeautifulSoup(myfile, "lxml")
        lxml_tree = html.fromstring(myfile)
    except:
        sys.exit("couldn't open file")
    # print(myfile)
    return lxml_tree


def modify_html(lxml_tree):
    images = ['http://www.w3.org/WAI/wcag1AAA.png', 'http://www.vintagecomputing.com/wp-content/images/webads/01_SNAPPLE.GIF', 'http://www.vintagecomputing.com/wp-content/images/webads/02_homepage1.gif', 'http://www.vintagecomputing.com/wp-content/images/webads/01_M0QMHHHQ.GIF', 'http://www.vintagecomputing.com/wp-content/images/webads/12_M0QMHID7.GIF', 'http://www.vintagecomputing.com/wp-content/images/webads/23_marchmadness99.gif', 'http://www.vintagecomputing.com/wp-content/images/webads/11_M0RIQ87N.GIF']
    footer = etree.Element('footer')
    lxml_tree.find('.//body').append(footer)
    footer_location = lxml_tree.find('.//footer')
    for image in images:
        img = etree.Element('img')
        img.set('src', image)
        footer_location.append(img)
    for html_tag in lxml_tree.xpath('//html'):
        html_tag.attrib['style'] = 'background-color: blue'
    return lxml_tree


def grab_images(lxml_tree):
    img_list = []
    for img in lxml_tree.xpath('//img/@src'):
        if (img[0:5]) not in ['http:', 'https:']:
            img = "http:" + img
        img_list.append(img)
        # print("img_list: " + str(img_list))
    return img_list


def delete_new_elements(lxml_tree):
    for style in lxml_tree.xpath("//style"):
        style.getparent().remove(style)
    for script in lxml_tree.xpath("//script"):
        script.getparent().remove(script)
    for link in lxml_tree.xpath("//link"):
        link.getparent().remove(link)
    return lxml_tree


def delete_images(lxml_tree):
    for img in lxml_tree.xpath("//img"):
        img.getparent().remove(img)
    for path in lxml_tree.xpath("//path"):
        path.getparent().remove(path)
    return lxml_tree


def main():
    # meme_websites = ['https://imgflip.com/memetemplates']
    # you can add more websites here grab memes from

    # for meme_website in meme_websites:
    #     grab_images(meme_website)
    lxml_tree = parse_website(open_website(sys.argv[1]))

    # lxml_tree.body.append(html.Element("footer"))
    lxml_tree = delete_images(lxml_tree)
    lxml_tree = delete_new_elements(lxml_tree)
    lxml_tree = modify_html(lxml_tree)
    # add_buttons(lxml_tree)

    with open('index.html', 'wb') as f:
        f.write(html.tostring(lxml_tree, pretty_print=True, method="html"))


#   print(grab_images(parse_website(open_website("http://www.memes.com"))))
#   print(open_website(parse_website(grab_images("https://imgflip.com/memetemplates"))))
#   I'm being rate limited, have to fix it


if __name__ == "__main__":
        main()
