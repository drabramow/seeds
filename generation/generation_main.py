import sys
sys.path.append('/Users/daniel/Desktop/seeds')

from ConditionProvider import get_random_conditions
from GenerationDriver import *

MODEL_PATH = 'stylegan2/network-snapshot-006746.pkl'

def main():
    driver = GenerationDriver()
    _G, _D, Gs = driver.load_model(MODEL_PATH)
    
if __name__ == "__main__":
    main()