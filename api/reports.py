from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import User, Character, CharacterList, Library, Ability, Expertise, JobSkill, SpeciesPassive, Backpack, Item, Weapon
from schema import UserRegisterSchema
from api import auth

router = APIRouter()

# GM: Add Character
@router.post("/gm/add-character/")
def add_character(
    char_name: str,
    char_class: str,
    char_species: str,
    char_job: str,
    char_level: int,
    char_health: int,
    char_acumen: int,
    char_strength: int,
    char_knowledge: int,
    char_wit: int,
    char_arcana: int,
    char_acrobatics: int,
    char_luck: int,
    db: Session = Depends(get_db)
):
    new_character = Character(
        char_name=char_name,
        char_class=char_class,
        char_species=char_species,
        char_job=char_job,
        char_level=char_level,
        char_health=char_health,
        char_acumen=char_acumen,
        char_strength=char_strength,
        char_knowledge=char_knowledge,
        char_wit=char_wit,
        char_arcana=char_arcana,
        char_acrobatics=char_acrobatics,
        char_luck=char_luck,
        library_id=None,  # To be set after Library creation
        backpack_id=None  # To be set after Backpack creation
    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    
    # Create corresponding Library and Backpack
    new_library = Library(character=new_character)
    db.add(new_library)
    db.commit()
    db.refresh(new_library)

    new_backpack = Backpack(character=new_character)
    db.add(new_backpack)
    db.commit()
    db.refresh(new_backpack)
    
    # Update character with library and backpack IDs
    new_character.library_id = new_library.library_id
    new_character.backpack_id = new_backpack.backpack_id
    db.commit()

    return {"message": "Character added successfully", "character_id": new_character.char_id}

# GM: Add Ability
@router.post("/gm/add-ability/")
def add_ability(
    ability_name: str,
    ability_description: str,
    ability_cost: str,
    ability_requirements: str,
    ability_roll: str,
    db: Session = Depends(get_db)
):
    new_ability = Ability(
        ability_name=ability_name,
        ability_description=ability_description,
        ability_cost=ability_cost,
        ability_requirements=ability_requirements,
        ability_roll=ability_roll
    )
    db.add(new_ability)
    db.commit()
    db.refresh(new_ability)
    return {"message": "Ability added successfully", "ability_id": new_ability.ability_id}

# GM: Add Expertise
@router.post("/gm/add-expertise/")
def add_expertise(
    expertise_name: str,
    expertise_description: str,
    expertise_roll: str,
    db: Session = Depends(get_db)
):
    new_expertise = Expertise(
        expertise_name=expertise_name,
        expertise_description=expertise_description,
        expertise_roll=expertise_roll
    )
    db.add(new_expertise)
    db.commit()
    db.refresh(new_expertise)
    return {"message": "Expertise added successfully", "expertise_id": new_expertise.expertise_id}

# GM: Add Job Skill
@router.post("/gm/add-job-skill/")
def add_job_skill(
    job_skill_name: str,
    job_skill_description: str,
    job_skill_requirements: str,
    job_skill_roll: str,
    db: Session = Depends(get_db)
):
    new_job_skill = JobSkill(
        job_skill_name=job_skill_name,
        job_skill_description=job_skill_description,
        job_skill_requirements=job_skill_requirements,
        job_skill_roll=job_skill_roll
    )
    db.add(new_job_skill)
    db.commit()
    db.refresh(new_job_skill)
    return {"message": "Job skill added successfully", "job_skill_id": new_job_skill.job_skill_id}

# GM: Add Species Passive
@router.post("/gm/add-species-passive/")
def add_species_passive(
    species_passive_species: str,
    species_passive_name: str,
    species_passive_description: str,
    species_passive_roll: str = None,
    db: Session = Depends(get_db)
):
    new_species_passive = SpeciesPassive(
        species_passive_species=species_passive_species,
        species_passive_name=species_passive_name,
        species_passive_description=species_passive_description,
        species_passive_roll=species_passive_roll
    )
    db.add(new_species_passive)
    db.commit()
    db.refresh(new_species_passive)
    return {"message": "Species passive added successfully", "species_passive_id": new_species_passive.species_passive_id}

# GM: Add Item
@router.post("/gm/add-item/")
def add_item(
    item_name: str,
    item_description: str,
    item_roll: str,
    item_cost_rating: int,
    db: Session = Depends(get_db)
):
    new_item = Item(
        item_name=item_name,
        item_description=item_description,
        item_roll=item_roll,
        item_cost_rating=item_cost_rating
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item added successfully", "item_id": new_item.item_id}

# GM: Add Weapon
@router.post("/gm/add-weapon/")
def add_weapon(
    weapon_name: str,
    weapon_description: str,
    weapon_roll: str,
    weapon_ability_name: str = None,
    weapon_ability_description: str = None,
    weapon_ability_roll: str = None,
    db: Session = Depends(get_db)
):
    new_weapon = Weapon(
        weapon_name=weapon_name,
        weapon_description=weapon_description,
        weapon_roll=weapon_roll,
        weapon_ability_name=weapon_ability_name,
        weapon_ability_description=weapon_ability_description,
        weapon_ability_roll=weapon_ability_roll
    )
    db.add(new_weapon)
    db.commit()
    db.refresh(new_weapon)
    return {"message": "Weapon added successfully", "weapon_id": new_weapon.weapon_id}

# GM: View All Characters
@router.get("/gm/view-characters/")
def view_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()
    return characters

# GM: View All Libraries
@router.get("/gm/view-libraries/")
def view_libraries(db: Session = Depends(get_db)):
    libraries = db.query(Library).all()
    return libraries

# GM: View All Backpacks
@router.get("/gm/view-backpacks/")
def view_backpacks(db: Session = Depends(get_db)):
    backpacks = db.query(Backpack).all()
    return backpacks

# GM: View Item Inventory
@router.get("/gm/view-items/")
def view_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

# GM: View All Abilities
@router.get("/gm/view-abilities/")
def view_abilities(db: Session = Depends(get_db)):
    abilities = db.query(Ability).all()
    return abilities

# GM: Bulk Remove Items
@router.delete("/gm/remove-items/")
def bulk_remove_items(item_name: str = None, item_cost_rating: int = None, db: Session = Depends(get_db)):
    query = db.query(Item)
    if item_name:
        query = query.filter(Item.item_name == item_name)
    if item_cost_rating:
        query = query.filter(Item.item_cost_rating == item_cost_rating)
    
    removed_count = query.delete()
    db.commit()
    return {"message": f"{removed_count} items removed successfully"}

# PLAYER AND GM: Add Player Character
@router.post("/player/add-character/")
def add_player_character(
    user_id: int,
    char_name: str,
    char_class: str,
    char_species: str,
    char_job: str,
    char_level: int,
    char_health: int,
    char_acumen: int,
    char_strength: int,
    char_knowledge: int,
    char_wit: int,
    char_arcana: int,
    char_acrobatics: int,
    char_luck: int,
    db: Session = Depends(get_db)
):
    new_character = Character(
        char_name=char_name,
        char_class=char_class,
        char_species=char_species,
        char_job=char_job,
        char_level=char_level,
        char_health=char_health,
        char_acumen=char_acumen,
        char_strength=char_strength,
        char_knowledge=char_knowledge,
        char_wit=char_wit,
        char_arcana=char_arcana,
        char_acrobatics=char_acrobatics,
        char_luck=char_luck,
        library_id=None,
        backpack_id=None
    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)

    new_library = Library(character=new_character)
    db.add(new_library)
    db.commit()
    db.refresh(new_library)

    new_backpack = Backpack(character=new_character)
    db.add(new_backpack)
    db.commit()
    db.refresh(new_backpack)

    new_character.library_id = new_library.library_id
    new_character.backpack_id = new_backpack.backpack_id
    db.commit()

    char_list_entry = CharacterList(user_id=user_id, char_id=new_character.char_id, char_index=1)  # You may adjust char_index logic
    db.add(char_list_entry)
    db.commit()

    return {"message": "Player character added successfully", "character_id": new_character.char_id}

# PLAYER: View Player Character
@router.get("/player/view-character/")
def view_player_character(user_id: int, db: Session = Depends(get_db)):
    character_list = db.query(CharacterList).filter(CharacterList.user_id == user_id).all()
    if not character_list:
        raise HTTPException(status_code=404, detail="No characters found for this player.")
    return character_list

# PLAYER: View Player Backpack
@router.get("/player/view-backpack/")
def view_player_backpack(char_id: int, db: Session = Depends(get_db)):
    backpack = db.query(Backpack).filter(Backpack.character_id == char_id).first()
    if not backpack:
        raise HTTPException(status_code=404, detail="Backpack not found.")
    return backpack

# PLAYER: View Player Library
@router.get("/player/view-library/")
def view_player_library(char_id: int, db: Session = Depends(get_db)):
    library = db.query(Library).filter(Library.character_id == char_id).first()
    if not library:
        raise HTTPException(status_code=404, detail="Library not found.")
    return library

# PLAYER: Get Ability Details
@router.get("/player/get-ability/")
def get_ability_details(ability_id: int, db: Session = Depends(get_db)):
    ability = db.query(Ability).filter(Ability.ability_id == ability_id).first()
    if not ability:
        raise HTTPException(status_code=404, detail="Ability not found.")
    return ability

# PLAYER: Get Job Skill Details
@router.get("/player/get-job-skill/")
def get_job_skill_details(job_skill_id: int, db: Session = Depends(get_db)):
    job_skill = db.query(JobSkill).filter(JobSkill.job_skill_id == job_skill_id).first()
    if not job_skill:
        raise HTTPException(status_code=404, detail="Job skill not found.")
    return job_skill

# PLAYER: Get Species Passive Details
@router.get("/player/get-species-passive/")
def get_species_passive_details(species_passive_id: int, db: Session = Depends(get_db)):
    species_passive = db.query(SpeciesPassive).filter(SpeciesPassive.species_passive_id == species_passive_id).first()
    if not species_passive:
        raise HTTPException(status_code=404, detail="Species passive not found.")
    return species_passive

# PLAYER: Get Expertise Details
@router.get("/player/get-expertise/")
def get_expertise_details(expertise_id: int, db: Session = Depends(get_db)):
    expertise = db.query(Expertise).filter(Expertise.expertise_id == expertise_id).first()
    if not expertise:
        raise HTTPException(status_code=404, detail="Expertise not found.")
    return expertise

# PLAYER: Get Item Details
@router.get("/player/get-item/")
def get_item_details(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    return item

# PLAYER: Get Weapon Details
@router.get("/player/get-weapon/")
def get_weapon_details(weapon_id: int, db: Session = Depends(get_db)):
    weapon = db.query(Weapon).filter(Weapon.weapon_id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found.")
    return weapon

# PLAYER: Level Up Character
@router.post("/player/level-up/")
def level_up_character(char_id: int, new_level: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.char_id == char_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found.")
    
    # You may add logic to check if the character meets criteria for leveling up
    character.char_level = new_level
    db.commit()
    return {"message": "Character leveled up successfully", "new_level": new_level}

# PLAYER: Adjust Character Stats
@router.post("/player/adjust-stats/")
def adjust_character_stats(
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
    character = db.query(Character).filter(Character.char_id == char_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found.")
    
    if char_health is not None:
        character.char_health = char_health
    if char_acumen is not None:
        character.char_acumen = char_acumen
    if char_strength is not None:
        character.char_strength = char_strength
    if char_knowledge is not None:
        character.char_knowledge = char_knowledge
    if char_wit is not None:
        character.char_wit = char_wit
    if char_arcana is not None:
        character.char_arcana = char_arcana
    if char_acrobatics is not None:
        character.char_acrobatics = char_acrobatics
    if char_luck is not None:
        character.char_luck = char_luck
    
    db.commit()
    return {"message": "Character stats adjusted successfully"}

# PLAYER: Add Item to Backpack
@router.post("/player/add-item/")
def add_item_to_backpack(char_id: int, item_id: int, db: Session = Depends(get_db)):
    backpack = db.query(Backpack).filter(Backpack.character_id == char_id).first()
    if not backpack:
        raise HTTPException(status_code=404, detail="Backpack not found.")
    
    # Logic to add the item to the backpack (this may require adjusting your models or adding a join table)
    backpack.item_id = item_id
    db.commit()
    return {"message": "Item added to backpack successfully"}

# PLAYER: Remove Item from Backpack
@router.delete("/player/remove-item/")
def remove_item_from_backpack(char_id: int, item_id: int, db: Session = Depends(get_db)):
    backpack = db.query(Backpack).filter(Backpack.character_id == char_id, Backpack.item_id == item_id).first()
    if not backpack:
        raise HTTPException(status_code=404, detail="Item not found in backpack.")
    
    # Logic to remove the item from the backpack
    backpack.item_id = None
    db.commit()
    return {"message": "Item removed from backpack successfully"}

# PLAYER: Add Weapon to Backpack
@router.post("/player/add-weapon/")
def add_weapon_to_backpack(char_id: int, weapon_id: int, db: Session = Depends(get_db)):
    backpack = db.query(Backpack).filter(Backpack.character_id == char_id).first()
    if not backpack:
        raise HTTPException(status_code=404, detail="Backpack not found.")
    
    # Logic to add the weapon to the backpack (this may require adjusting your models or adding a join table)
    backpack.weapon_id = weapon_id
    db.commit()
    return {"message": "Weapon added to backpack successfully"}

# PLAYER: Remove Weapon from Backpack
@router.delete("/player/remove-weapon/")
def remove_weapon_from_backpack(char_id: int, weapon_id: int, db: Session = Depends(get_db)):
    backpack = db.query(Backpack).filter(Backpack.character_id == char_id, Backpack.weapon_id == weapon_id).first()
    if not backpack:
        raise HTTPException(status_code=404, detail="Weapon not found in backpack.")
    
    # Logic to remove the weapon from the backpack
    backpack.weapon_id = None
    db.commit()
    return {"message": "Weapon removed from backpack successfully"}


from auth import get_password_hash, create_access_token

@router.post("/register/")
def register_user(user_data: UserRegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_name == user_data.user_name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(user_name=user_data.user_name, user_type=user_data.user_type, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.user_id}