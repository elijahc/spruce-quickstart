import pandas as pd

POKEDEX = pd.read_csv('https://query.data.world/s/w2h7grri3uebxuwy6z53evk7mrqe6v')
# def load_pokedex()
#     px = pd.read_csv('https://query.data.world/s/w2h7grri3uebxuwy6z53evk7mrqe6v')
#     return px

gl = {
    'Brock':[74, 95],
    'Misty':[120,121],
    'Lt Surge':[100,25,26]
}

px = POKEDEX
gl = {k:[dict(px.query('number == {}'.format(i)).iloc[0]) for i in v] for k,v in gl.items()}
gl

gym_leaders_g1 = gl