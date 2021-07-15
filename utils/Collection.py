from typing import List, Dict

class Collection:
  def __init__(self, seeds: List[int], collection_dict: Dict[str, int]):
    self.seeds = seeds
    self.collection_dict = collection_dict
  
  def get_collection_ids(self) -> Dict[int, int]:
    return {i[0]: i[1] for i in (list(range(len(self.seeds))), self.seeds)}

  def size(self) -> int:
    return len(self.seeds)