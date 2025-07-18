from fastapi import FastAPI, Request
from Ai_writer.writer import spin_text
from Ai_writer.reviewer import review_text
from human_loop.edit_interface import present_for_editing
from chroma_search.version_store import store_version, semantic_search
from rl.reward_model import compute_reward
from rl.trainer import update_policy

app = FastAPI()

@app.post("/process_chapter/")
async def process(request: Request):
    data = await request.json()
    raw_text = data["text"]
    spun = spin_text(raw_text)
    reviewed = review_text(spun)
    human_approved = present_for_editing(reviewed)
    
    if human_approved:
        store_version(human_approved, version_tag="v1")
        reward = compute_reward(raw_text, spun, human_feedback="accept")
        update_policy(reward)
        return {"status": "Success", "final_text": human_approved}
    else:
        return {"status": "Rejected by human"}
