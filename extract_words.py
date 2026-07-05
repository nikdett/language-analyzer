from collections import defaultdict

words_by_category = defaultdict(set)

with open("hurtlex.tsv", "r") as f:
    next(f) # skip category hearders
    for line in f: 
        parts = line.strip().split("\t")
        if len(parts) >= 4:
            category = parts[1]
            lemma = parts[3]
            if " " not in lemma and len(lemma) > 2:
                words_by_category[category].add(lemma.lower()) # return in lower case

# sort words into each category 
usVSthem = sorted(
    words_by_category["re"] | # radical/ethnic slurs
    words_by_category["is"] | # group
    words_by_category["rci"]  # uncivilized/barbaric
)

threat = sorted(
    words_by_category["cds"] | # violent
    words_by_category["svp"]   # sin
)

angry = sorted(
    words_by_category["dmc"] | # debasement
    words_by_category["asm"] | # sexual insults 
    words_by_category["asf"]   # insults
)

negative = sorted(
    words_by_category["ddp"] |  # mental/physical put-downs
    words_by_category["ddf"] |  # disability slurs
    words_by_category["om"]     # body insults
)

emotional = sorted(
    words_by_category["pa"] |   # nationalist/patriotic
    words_by_category["qas"]    # submission/othering
)

with open("hurtlex_wordlists.js", "w") as out:
    out.write(f'const hvUsVsThemWords = {usVSthem};\n')
    out.write(f'const hvThreatWords = {threat};\n')
    out.write(f'const hvAngryWords = {angry};\n')
    out.write(f'const hvNegativeWords = {negative};\n')
    out.write(f'const hvEmotionalWords = {emotional};\n')

print("done!")