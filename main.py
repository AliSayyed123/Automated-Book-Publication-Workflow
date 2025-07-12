# main.py
from Scraping.fetcher import fetch_chapter
from Ai_writer.writer import spin_text
from Ai_writer.reviewer import review_text
from human_loop.edit_interface import present_for_editing
from chroma_search.version_store import store_version
from rl.reward_model import compute_reward
from rl.trainer import update_policy

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

def main():
    raw_text = fetch_chapter(URL)
    spun = spin_text(raw_text)
    reviewed = review_text(spun)
    final = present_for_editing(reviewed)
    if final:
        store_version(final, version_tag="v1")
        reward = compute_reward(raw_text, spun, human_feedback="accept")
        update_policy(reward)
        print("[SUCCESS] Chapter finalized and stored.")
    else:
        print("[REJECTED] Human rejected the AI-generated version.")

if __name__ == "__main__":
    main()
