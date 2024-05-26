import sys
import xmltodict
import re
from loguru import logger

clean_regex_1 = re.compile("<.*?>")
clean_regex_2 = re.compile("<!.*?>")
clean_regex_3 = re.compile("<div.*?>")


def read_wordpress_xml(filename):
    with open(filename, encoding="utf8") as f:
        xml_data = f.read()
    xml_dict = xmltodict.parse(xml_data)
    return xml_dict


def _add_to_file(filename, data):
    with open(filename, "a", encoding="utf8") as f:
        f.write(data)


def new_file(filename):
    # Open file in write mode so that it's cleared from old data
    with open(filename, "w", encoding="utf8"):
        pass


def clean_text(text) -> str:
    """removes html and wordpress tags, i.e anything between < >"""
    tmp = re.sub(clean_regex_1, "", text)
    tmp = re.sub(clean_regex_2, "", tmp)
    tmp = re.sub(clean_regex_3, "", tmp)
    tmp = tmp.replace("None", " ").replace("&nbsp", " ")
    return tmp


def process_data(xml_dict: dict, output_filename: str) -> None:
    items = xml_dict.get("rss").get("channel").get("item")
    pages = []
    other = []
    for item in items:
        attatchemnt_url = item.get("wp:attachment_url", " ")
        if attatchemnt_url.endswith("jpg") or attatchemnt_url.endswith("png"):
            pass
        guid_text = item.get("guid").get("#text")
        ending = guid_text.split(".")[-1]
        if ending in ["jpeg", "mp4", "png", "jpg"]:
            pass
        elif "page_id" in ending:
            pages.append(item)
        else:
            other.append(item)

    for page in pages:
        title = page.get("title")
        content = page.get("content:encoded")
        content = clean_text(content)
        excerpt = page.get("excerpt:encoded")
        _add_to_file(output_filename, data=f"{title}\n{excerpt}\n{content}\n")
        logger.info(f"Added {title} to {output_filename}")

    for post in other:
        post_type = post.get("wp:post_type")
        if post_type == "wp_global_styles":
            continue
        if post_type not in ["post", "page"]:
            continue
        title = post.get("title")
        if not title:
            continue
        title = title.replace("/", " ")
        content = post.get("content:encoded", " ")
        if content is None:
            content = " "
        content = clean_text(content)
        excerpt = post.get("excerpt:encoded", " ")
        _add_to_file(output_filename, data=f"{title}\n{excerpt}\n{content}\n")
        logger.info(f"Added {title} to {output_filename}")


def main():
    logger.info("start")
    wordpress_export_file = sys.argv[1]
    if not wordpress_export_file:
        raise ValueError("No wordpress export file specified")
    output_file = sys.argv[2]
    raw_data = read_wordpress_xml(wordpress_export_file)
    process_data(raw_data, output_file)
    logger.info(f"Finished, data saved to {output_file}")


if __name__ == "__main__":
    main()
