from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import User
from schema import (
    CharacterSchema, AbilitySchema, ExpertiseSchema, JobSkillSchema, 
    SpeciesPassiveSchema, ItemSchema, WeaponSchema, CharacterListSchema, 
    LibrarySchema, BackpackSchema, UserSchema
)
from typing import List
from api.reports import (
    add_character, add_ability, add_expertise, add_job_skill, add_species_passive,
    add_item, add_weapon, view_characters, view_libraries, view_backpacks,
    view_items, view_abilities, bulk_remove_items, add_player_character,
    view_player_character, view_player_backpack, view_player_library, 
    get_ability_details, get_job_skill_details, get_species_passive_details, 
    get_expertise_details, get_item_details, get_weapon_details, 
    level_up_character, adjust_character_stats, add_item_to_backpack, 
    remove_item_from_backpack, add_weapon_to_backpack, remove_weapon_from_backpack
)
from fastapi.security import OAuth2PasswordRequestForm
from api.auth import *

"""
Table of Contents:
1. GM Endpoints
    1.1. Add Character (POST /gm/add-character/)
    1.2. Add Ability (POST /gm/add-ability/)
    1.3. Add Expertise (POST /gm/add-expertise/)
    1.4. Add Job Skill (POST /gm/add-job-skill/)
    1.5. Add Species Passive (POST /gm/add-species-passive/)
    1.6. Add Item (POST /gm/add-item/)
    1.7. Add Weapon (POST /gm/add-weapon/)
    1.8. View All Characters (GET /gm/view-characters/)
    1.9. View All Libraries (GET /gm/view-libraries/)
    1.10. View All Backpacks (GET /gm/view-backpacks/)
    1.11. View Item Inventory (GET /gm/view-items/)
    1.12. View All Abilities (GET /gm/view-abilities/)
    1.13. Bulk Remove Items (DELETE /gm/remove-items/)

2. Player and GM Endpoints
    2.1. Add Player Character (POST /player/add-character/)
    2.2. View Player Character (GET /player/view-character/)
    2.3. View Player Backpack (GET /player/view-backpack/)
    2.4. View Player Library (GET /player/view-library/)
    2.5. Get Ability Details (GET /player/get-ability/)
    2.6. Get Job Skill Details (GET /player/get-job-skill/)
    2.7. Get Species Passive Details (GET /player/get-species-passive/)
    2.8. Get Expertise Details (GET /player/get-expertise/)
    2.9. Get Item Details (GET /player/get-item/)
    2.10. Get Weapon Details (GET /player/get-weapon/)
    2.11. Level Up Character (POST /player/level-up/)
    2.12. Adjust Character Stats (POST /player/adjust-stats/)
    2.13. Add Item to Backpack (POST /player/add-item/)
    2.14. Remove Item from Backpack (DELETE /player/remove-item/)
    2.15. Add Weapon to Backpack (POST /player/add-weapon/)
    2.16. Remove Weapon from Backpack (DELETE /player/remove-weapon/)
"""

app = FastAPI()

# GM Endpoints

@app.post("/gm/add-character", response_model=CharacterSchema)
async def add_character_endpoint(char_data: CharacterSchema, db: Session = Depends(get_db)):
    try:
        return add_character(db, **char_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-ability", response_model=AbilitySchema)
async def add_ability_endpoint(ability_data: AbilitySchema, db: Session = Depends(get_db)):
    try:
        return add_ability(db, **ability_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-expertise", response_model=ExpertiseSchema)
async def add_expertise_endpoint(expertise_data: ExpertiseSchema, db: Session = Depends(get_db)):
    try:
        return add_expertise(db, **expertise_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-job-skill", response_model=JobSkillSchema)
async def add_job_skill_endpoint(job_skill_data: JobSkillSchema, db: Session = Depends(get_db)):
    try:
        return add_job_skill(db, **job_skill_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-species-passive", response_model=SpeciesPassiveSchema)
async def add_species_passive_endpoint(species_passive_data: SpeciesPassiveSchema, db: Session = Depends(get_db)):
    try:
        return add_species_passive(db, **species_passive_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-item", response_model=ItemSchema)
async def add_item_endpoint(item_data: ItemSchema, db: Session = Depends(get_db)):
    try:
        return add_item(db, **item_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/gm/add-weapon", response_model=WeaponSchema)
async def add_weapon_endpoint(weapon_data: WeaponSchema, db: Session = Depends(get_db)):
    try:
        return add_weapon(db, **weapon_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gm/view-characters", response_model=List[CharacterSchema])
async def view_characters_endpoint(db: Session = Depends(get_db)):
    try:
        return view_characters(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gm/view-libraries", response_model=List[LibrarySchema])
async def view_libraries_endpoint(db: Session = Depends(get_db)):
    try:
        return view_libraries(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gm/view-backpacks", response_model=List[BackpackSchema])
async def view_backpacks_endpoint(db: Session = Depends(get_db)):
    try:
        return view_backpacks(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gm/view-items", response_model=List[ItemSchema])
async def view_items_endpoint(db: Session = Depends(get_db)):
    try:
        return view_items(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gm/view-abilities", response_model=List[AbilitySchema])
async def view_abilities_endpoint(db: Session = Depends(get_db)):
    try:
        return view_abilities(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/gm/remove-items")
async def bulk_remove_items_endpoint(item_name: str = None, item_cost_rating: int = None, db: Session = Depends(get_db)):
    try:
        return bulk_remove_items(db, item_name=item_name, item_cost_rating=item_cost_rating)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Player and GM Endpoints

@app.post("/player/add-character", response_model=CharacterSchema)
async def add_player_character_endpoint(char_data: CharacterSchema, user_id: int, db: Session = Depends(get_db)):
    try:
        return add_player_character(db, user_id, **char_data.dict())
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/view-character", response_model=List[CharacterListSchema])
async def view_player_character_endpoint(user_id: int, db: Session = Depends(get_db)):
    try:
        return view_player_character(db, user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/view-backpack", response_model=BackpackSchema)
async def view_player_backpack_endpoint(char_id: int, db: Session = Depends(get_db)):
    try:
        return view_player_backpack(db, char_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/view-library", response_model=LibrarySchema)
async def view_player_library_endpoint(char_id: int, db: Session = Depends(get_db)):
    try:
        return view_player_library(db, char_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-ability", response_model=AbilitySchema)
async def get_ability_details_endpoint(ability_id: int, db: Session = Depends(get_db)):
    try:
        return get_ability_details(db, ability_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-job-skill", response_model=JobSkillSchema)
async def get_job_skill_details_endpoint(job_skill_id: int, db: Session = Depends(get_db)):
    try:
        return get_job_skill_details(db, job_skill_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-species-passive", response_model=SpeciesPassiveSchema)
async def get_species_passive_details_endpoint(species_passive_id: int, db: Session = Depends(get_db)):
    try:
        return get_species_passive_details(db, species_passive_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-expertise", response_model=ExpertiseSchema)
async def get_expertise_details_endpoint(expertise_id: int, db: Session = Depends(get_db)):
    try:
        return get_expertise_details(db, expertise_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-item", response_model=ItemSchema)
async def get_item_details_endpoint(item_id: int, db: Session = Depends(get_db)):
    try:
        return get_item_details(db, item_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/player/get-weapon", response_model=WeaponSchema)
async def get_weapon_details_endpoint(weapon_id: int, db: Session = Depends(get_db)):
    try:
        return get_weapon_details(db, weapon_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/player/level-up", response_model=dict)
async def level_up_character_endpoint(char_id: int, new_level: int, db: Session = Depends(get_db)):
    try:
        return level_up_character(db, char_id, new_level)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/player/adjust-stats", response_model=dict)
async def adjust_character_stats_endpoint(
    char_id: int,
    char_health: int = None,
    char_acumen: int = None,
    char_strength: int = None,
    char_knowledge: int = None,
    char_wit: int = None,
    char_arcana: int = None,
    char_acrobatics: int = None,
    char_luck: int = None,
    db: Session = Depends(get_db)
):
    try:
        return adjust_character_stats(
            db, char_id, char_health, char_acumen, char_strength,
            char_knowledge, char_wit, char_arcana, char_acrobatics, char_luck
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/player/add-item", response_model=dict)
async def add_item_to_backpack_endpoint(char_id: int, item_id: int, db: Session = Depends(get_db)):
    try:
        return add_item_to_backpack(db, char_id, item_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/player/remove-item", response_model=dict)
async def remove_item_from_backpack_endpoint(char_id: int, item_id: int, db: Session = Depends(get_db)):
    try:
        return remove_item_from_backpack(db, char_id, item_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/player/add-weapon", response_model=dict)
async def add_weapon_to_backpack_endpoint(char_id: int, weapon_id: int, db: Session = Depends(get_db)):
    try:
        return add_weapon_to_backpack(db, char_id, weapon_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/player/remove-weapon", response_model=dict)
async def remove_weapon_from_backpack_endpoint(char_id: int, weapon_id: int, db: Session = Depends(get_db)):
    try:
        return remove_weapon_from_backpack(db, char_id, weapon_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Register User
@app.post("/register/")
async def register_user(user_name: str, user_type: str, db: Session = Depends(get_db)):
    # Ensure user_type is either "GM" or "Player"
    if user_type not in ["GM", "Player"]:
        raise HTTPException(status_code=400, detail="Invalid user_type. Must be 'GM' or 'Player'.")

    # Check if username already exists
    existing_user = db.query(User).filter(User.user_name == user_name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists.")

    # Create a new user
    new_user = User(
        user_name=user_name,
        user_type=user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.user_id}

@app.post("/register/")
def register_user(user_data: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_name == user_data.user_name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(user_name=user_data.user_name, user_type=user_data.user_type, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.user_id}
