import random as rand
import numpy as np

NUM_ARTISTS = 129
NUM_GENRES = 11
NUM_STYLES = 27

def get_random_conditions():
  num_images = np.abs(np.random.normal(loc=1, scale=1.5))
  if num_images <= 1:
    num_images = 1
  else:
    num_images = int(np.ceil(num_images))

  return [{"artist": rand.randint(0, NUM_ARTISTS-1),
          "genre": rand.randint(NUM_ARTISTS, NUM_ARTISTS-1 + NUM_GENRES-1),
          "style": rand.randint(NUM_GENRES, NUM_ARTISTS + NUM_GENRES + NUM_STYLES-1)},
          [np.random.randint(2**32 - 1) for _ in range(num_images)]]