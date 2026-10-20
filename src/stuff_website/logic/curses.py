import random

TEXT_POOL = [
    "The secret of getting ahead is getting started.",
    "Simplicity is prerequisite for reliability.",
    "First, solve the problem. Then, write the code.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Make it work, make it right, make it fast.",
    "Continuous improvement is better than delayed perfection.",
]


def get_random_curse() -> str:
  """Returns a random string from the pool

  Returns:
      Random curse as text"""

  return random.choice(TEXT_POOL)
