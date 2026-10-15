import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from q_race_lib import VALUE
assert VALUE == 1, f"BROKEN COMBINATION: q_race_lib.VALUE={VALUE}, expected 1"
print("race check ok")
