from typing import List
from dataclasses import dataclass


@dataclass
class Player:
    """The player is the main object.
    They have a name, a bunch of skills, quests, their own gold, and potential rewards."""
    name: str
    skills: List[dict] = None
    gold: int = 0
    rewards: dict = None
    def add_new_skill(self, skill: str) -> List[dict]:
        print("New skill:", skill)
        new_skill = {'name': skill, 'level': 1, 'exp': 0}
        self.skills.append(new_skill)
        return self.skills


@dataclass
class Quest:
    """Quests are the backbone of activity. They have
    easy, medium, hard difficulty, the skill they are associated with,
    and a reward dict"""
    title: str
    skill: str
    reward: dict
    difficulty: str
    repeatable: bool


