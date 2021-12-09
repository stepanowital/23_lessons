class Town:
    def __init__(self, name, region):
        self.name = name
        self.region = region


towns = [Town("балашиха", "мо"), Town("химки", "мо"), Town("тула", "тульская область")]


def build_dict(towns):
    res = {}
    for t in towns:
        res[t.name] = t.region
    return res


build_dict(towns)
