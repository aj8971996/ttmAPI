from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Users Table
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_type = Column(String(15), nullable=False)
    hashed_password = Column(String(60), nullable=False)

    __table_args__ = (
        CheckConstraint("user_type IN ('GM', 'Player')", name='user_type_check'),
    )

    # Relationships
    character_list = relationship('CharacterList', back_populates='user')

# Character List Table
class CharacterList(Base):
    __tablename__ = 'character_list'
    list_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    char_index = Column(Integer, nullable=False)
    char_id = Column(Integer, ForeignKey('characters.char_id'), nullable=False)
    
    # Relationships
    user = relationship('User', back_populates='character_list')
    character = relationship('Character', back_populates='character_list')

# Characters Table
class Character(Base):
    __tablename__ = 'characters'
    char_id = Column(Integer, primary_key=True)
    char_type = Column(String(15), nullable=False)
    char_name = Column(String(150), nullable=False)
    char_description = Column(String(500))
    char_class = Column(String(25), nullable=False)
    char_job = Column(String(25), nullable=False)
    char_species = Column(String(25), nullable=False)
    char_level = Column(Integer, nullable=False)
    char_magic_point_value = Column(Integer, nullable=False)
    char_health_point_value = Column(Integer, nullable=False)
    char_health = Column(Integer, nullable=False)
    char_acumen = Column(Integer, nullable=False)
    char_strength = Column(Integer, nullable=False)
    char_knowledge = Column(Integer, nullable=False)
    char_wit = Column(Integer, nullable=False)
    char_arcana = Column(Integer, nullable=False)
    char_acrobatics = Column(Integer, nullable=False)
    char_luck = Column(Integer, nullable=False)
    library_id = Column(Integer, ForeignKey('libraries.library_id'), nullable=False)
    backpack_id = Column(Integer, ForeignKey('backpacks.backpack_id'), nullable=False)
    
    # Relationships
    character_list = relationship('CharacterList', back_populates='character')
    library = relationship('Library', back_populates='character')
    backpack = relationship('Backpack', back_populates='character')

# Library Table
class Library(Base):
    __tablename__ = 'libraries'
    library_id = Column(Integer, primary_key=True)
    ability_id = Column(Integer, ForeignKey('abilities.ability_id'), nullable=False)
    expertise_id = Column(Integer, ForeignKey('expertises.expertise_id'), nullable=False)
    job_skill_id = Column(Integer, ForeignKey('job_skills.job_skill_id'), nullable=False)
    species_passive_id = Column(Integer, ForeignKey('species_passives.species_passive_id'), nullable=False)
    
    # Relationships
    character = relationship('Character', back_populates='library')
    ability = relationship('Ability', back_populates='library')
    expertise = relationship('Expertise', back_populates='library')
    job_skill = relationship('JobSkill', back_populates='library')
    species_passive = relationship('SpeciesPassive', back_populates='library')

# Abilities Table
class Ability(Base):
    __tablename__ = 'abilities'
    ability_id = Column(Integer, primary_key=True)
    ability_cost = Column(String(500), nullable=False)
    ability_requirements = Column(String(500), nullable=False)
    ability_name = Column(String(150), nullable=False)
    ability_description = Column(String(500), nullable=False)
    ability_roll = Column(String(500), nullable=False)
    
    # Relationships
    library = relationship('Library', back_populates='ability')

# Expertise Table
class Expertise(Base):
    __tablename__ = 'expertises'
    expertise_id = Column(Integer, primary_key=True)
    expertise_name = Column(String(150), nullable=False)
    expertise_description = Column(String(500), nullable=False)
    expertise_roll = Column(String(500), nullable=False)
    
    # Relationships
    library = relationship('Library', back_populates='expertise')

# Job Skills Table
class JobSkill(Base):
    __tablename__ = 'job_skills'
    job_skill_id = Column(Integer, primary_key=True)
    job_skill_name = Column(String(150), nullable=False)
    job_skill_requirements = Column(String(500), nullable=False)
    job_skill_description = Column(String(500), nullable=False)
    job_skill_roll = Column(String(500), nullable=False)
    
    # Relationships
    library = relationship('Library', back_populates='job_skill')

# Species Passives Table
class SpeciesPassive(Base):
    __tablename__ = 'species_passives'
    species_passive_id = Column(Integer, primary_key=True)
    species_passive_species = Column(String(25), nullable=False)
    species_passive_name = Column(String(150), nullable=False)
    species_passive_description = Column(String(500), nullable=False)
    species_passive_roll = Column(String(500))
    
    # Relationships
    library = relationship('Library', back_populates='species_passive')

# Backpack Table
class Backpack(Base):
    __tablename__ = 'backpacks'
    backpack_id = Column(Integer, primary_key=True)
    weapon_id = Column(Integer, ForeignKey('weapons.weapon_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    
    # Relationships
    character = relationship('Character', back_populates='backpack')
    weapon = relationship('Weapon', back_populates='backpack')
    item = relationship('Item', back_populates='backpack')

# Weapons Table
class Weapon(Base):
    __tablename__ = 'weapons'
    weapon_id = Column(Integer, primary_key=True)
    weapon_name = Column(String(150), nullable=False)
    weapon_description = Column(String(500), nullable=False)
    weapon_roll = Column(String(500), nullable=False)
    weapon_ability_name = Column(String(150))
    weapon_ability_description = Column(String(150))
    weapon_ability_roll = Column(String(500))
    
    # Relationships
    backpack = relationship('Backpack', back_populates='weapon')

# Items Table
class Item(Base):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(150), nullable=False)
    item_description = Column(String(500), nullable=False)
    item_roll = Column(String(500), nullable=False)
    item_cost_rating = Column(Integer, nullable=False)
    
    # Relationships
    backpack = relationship('Backpack', back_populates='item')