from typing import List
from dataclasses import dataclass


@dataclass
class Player:
    """The player is the main object. They have a name, a"""
    name: str
    skills: List[dict]
    tasks: dict
    quests: dict
    gold: int
    rewards: dict


@dataclass
class Quest:
    """Quests are the backbone of activity. They have
    easy, medium, hard difficulty, the skill they are associated with,
    and a reward dict"""
    title: str
    skill: dict
    reward: dict
    difficulty: str


class Skill:
    """Skills are things that the player can do.
    They can be hobbies, tasks, or habits to build.
    A skill has a name, a level, and total exp."""

    def __init__(self, name, exp, level) -> None:
        self.name = name
        self.exp = exp
        self.level = level

    def gain_exp(self, exp_gained) -> int:
        """This adds any experience gained to the total XP.
        Each level will be a flat number of experience points, to build better habits."""
        self.exp = self.exp + exp_gained
        if self.exp > 100:
            self.level = self.level + 1
            self.exp = self.exp - 100
        return self.exp


if __name__ - - "__main__":
    print("classes.py log")
