import pywikibot
import subprocess
import webbrowser
import os
from menu import edit_summary_menu

# Read in the list of ignored terms
ignore_list = []
if os.path.exists("ignore.text"):
    with open("ignore.txt", encoding="utf-8") as ignore:
        ignore_list = [line.strip() for line in ignore.readlines()] 
else:
    with open("ignore.txt", mode="w", encoding="utf-8"):
        """Creates ignore.txt if it does not yet exist"""

site = pywikibot.Site("en", "wiktionary")
# index_page_url = input("Please enter a Wiktionary pagename to specify a word list to utilize: ")
index_page_url = "User:Benwing2/bg-freq-fiction"
index_page = pywikibot.Page(site, index_page_url)

for link in index_page.linkedPages():
    link: pywikibot.Page

    # Avoid all existing links, ignored links, and proper nouns
    if not link.exists() and link.title() not in ignore_list and not link.title()[0].isupper():
        subprocess.run(["code", f"output/{link.title()}.wt"])
    else:
        continue
    try:
        if input(f"Press enter to upload \"{link.title()}\" to Wiktionary, Ctrl+C to ignore the word, \"exit\" to quit. ") in ("quit", "exit"):
            break
        # webbrowser.open_new_tab(f"https://en.wiktionary.org/w/index.php?title={link.title()}&action=edit")
        with open(f"output/{link.title()}.wt") as wikitext:
            link.text = wikitext.read()
        
        link.save(summary=edit_summary_menu(), quiet=True)
        print(f"Page '{link.title()}' saved ({link.full_url()})")

    except KeyboardInterrupt:
        ignore_list.append(link.title())
        print()
        continue

    try:
        input("Press enter for next term. ")
    except KeyboardInterrupt:
        print()
        break

# Update the list of ignored terms
with open("ignore.txt", mode="w", encoding="utf-8") as ignore:
    ignore.write("\n".join(ignore_list))