from pydantic import BaseModel
from typing import Optional

# User Schema
class UserSchema(BaseModel):
    user_id: int
    user_name: str
    user_password: str
    user_type: str

    class Config:
        from_attributes = True

# Character List Schema
class CharacterListSchema(BaseModel):
    list_id: int
    user_id: int
    char_index: int
    char_id: int

    class Config:
        from_attributes = True

# Character Schema
class CharacterSchema(BaseModel):
    char_id: int
    char_type: str
    char_name: str
    char_description: Optional[str] = None
    char_class: str
    char_job: str
    char_species: str
    char_level: int
    char_magic_point_value: int
    char_health_point_value: int
    char_health: int
    char_acumen: int
    char_strength: int
    char_knowledge: int
    char_wit: int
    char_arcana: int
    char_acrobatics: int
    char_luck: int
    library_id: int
    backpack_id: int

    class Config:
        from_attributes = True

# Library Schema
class LibrarySchema(BaseModel):
    library_id: int
    ability_id: int
    expertise_id: int
    job_skill_id: int
    species_passive_id: int

    class Config:
        from_attributes = True

# Ability Schema
class AbilitySchema(BaseModel):
    ability_id: int
    ability_cost: str
    ability_requirements: str
    ability_name: str
    ability_description: str
    ability_roll: str

    class Config:
        from_attributes = True

# Expertise Schema
class ExpertiseSchema(BaseModel):
    expertise_id: int
    expertise_name: str
    expertise_description: str
    expertise_roll: str

    class Config:
        from_attributes = True

# Job Skill Schema
class JobSkillSchema(BaseModel):
    job_skill_id: int
    job_skill_name: str
    job_skill_requirements: str
    job_skill_description: str
    job_skill_roll: str

    class Config:
        from_attributes = True

# Species Passive Schema
class SpeciesPassiveSchema(BaseModel):
    species_passive_id: int
    species_passive_species: str
    species_passive_name: str
    species_passive_description: str
    species_passive_roll: Optional[str] = None

    class Config:
        from_attributes = True

# Backpack Schema
class BackpackSchema(BaseModel):
    backpack_id: int
    weapon_id: int
    item_id: int

    class Config: 
        from_attributes = True

# Weapons Schema
class WeaponSchema(BaseModel):
    weapon_id: int
    weapon_name: str
    weapon_description: str
    weapon_roll: str
    weapon_ability_name: Optional[str] = None
    weapon_ability_description: Optional[str] = None
    weapon_ability_roll: Optional[str] = None

    class Config:
        from_attributes = True

# Items Schema
class ItemSchema(BaseModel):
    item_id: int
    item_name: str
    item_description: str
    item_roll: str
    item_cost_rating: int

    class Config:
        from_attributes = True