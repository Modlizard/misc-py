import random

VALUES = ["∞", "Α", "α", "Β", "β", "Γ", "γ", "Δ", "δ", "Ε", "ε", "Ζ", "ζ", "Η", "η", "Θ", "θ", "Ι", "ι", "Κ", "κ", "Λ", "λ", "Μ", "μ", "Ν", "ν", "Ξ", "ξ", "Ο", "ο", "Π", "π", "Ρ", "ρ", "Σ", "σ", "Τ", "τ", "Υ", "υ", "Φ", "φ", "Χ", "χ", "Ψ", "ψ", "Ω", "ω"]
MATH = ["+", "-", "±", "/", "⋅", "^"]
MATH2 = ["≪", "≫", "∝", "=", "<", "≤", ">", "≥", "⇒", "⇔"]
WRAPPERS = [["∫", "dx"], ["∫∫", "dxdx"]]
INTERMEDIATES = ["∴", "∵"]
PREFIXES = ["∆"]
SUFFIXES = ["!", "°"]

def genValueGroup():
    prefix = random.choice(PREFIXES) if random.randint(1,10) == 1 else "" # 10% chance of prefix
    suffix = random.choice(SUFFIXES) if random.randint(1,5) == 1 else "" # 20% chance of suffix
    return f"{prefix}{random.choice(VALUES)}{suffix}"


def genMathLine():
    text = ""
    charGroups = random.randint(3,9)
    for x in range(charGroups):
        text += f"{genValueGroup()} "
        if x != charGroups - 1:
            text += f"{random.choice(MATH2)} " if random.randint(1,10) < 4 else f"{random.choice(MATH)} " # 30% chance of math2 vs math
    if random.randint(1,4) == 1: # 25% chance of wrapping function
        group = random.choice(WRAPPERS)
        text = f"{group[0]} {text}{group[1].replace('dx',f'd{random.choice(VALUES)}')}"
    return text

def genMathParagraph():
    if random.randint(1,10) == 1: # 10% chance of shitpost
        return "The proof is trivial and left as an exercise to the reader."

    nextParagraph, text = 3, ""
    while nextParagraph > 1:
        for _ in range(random.randint(4,8)):
            text += f"{genMathLine()}\n"
        text += f"{random.choice(INTERMEDIATES)}\n"
        nextParagraph = random.randint(1,3)
    return f"{text}Q.E.D"

def githubFormat(text):
    return text.replace("\n", "\\\n")
    #return "\n".join(map(lambda x: f"`{x}`", text.split("\n")))

if __name__ == "__main__":
    bullshit = genMathParagraph()
    print(bullshit)
    print(githubFormat(bullshit))

