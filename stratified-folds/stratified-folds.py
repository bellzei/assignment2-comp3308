import csv, random
from pathlib import Path

INPUT_FILE   = "normalisation/occupancy.csv"
OUTPUT_FILE  = "occupancy-folds.csv"
K            = 10        # number of folds
SEED         = 42        # reproducibility

# 1. -------- read entire file (no header) --------
with open(INPUT_FILE, newline="") as f:
    rows = [row for row in csv.reader(f)]

# 2. -------- split by class --------
buckets = {}
for row in rows:
    label = row[-1]
    buckets.setdefault(label, []).append(row)

# 3. -------- shuffle each bucket --------
rng = random.Random(SEED)
for lst in buckets.values():
    rng.shuffle(lst)

# 4. -------- compute per‑fold quotas --------
def quotas(total, k):
    base = total // k
    extras = total % k
    return [base + 1 if i < extras else base for i in range(k)]

quota_map = {lbl: quotas(len(lst), K) for lbl, lst in buckets.items()}

# 5. -------- build K folds --------
folds = [[] for _ in range(K)]
for i in range(K):
    for lbl, lst in buckets.items():
        need = quota_map[lbl][i]
        folds[i].extend(lst[:need])
        del lst[:need]
    rng.shuffle(folds[i])            # mix classes inside the fold

# 6. -------- write out in required format --------
with open(OUTPUT_FILE, "w", newline="") as fout:
    writer = csv.writer(fout)
    for idx, fold in enumerate(folds, start=1):
        fout.write(f"fold{idx}\n")
        writer.writerows(fold)       # raw rows, no header
        fout.write("\n")             # single blank line separator

print("✓  Wrote", Path(OUTPUT_FILE).resolve())
