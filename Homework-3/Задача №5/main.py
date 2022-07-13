from heroes import ChuckNorris, Superman, SuperHero
from media import Massmedia
from places import Place, Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news = Massmedia(hero, place)
    make_news = news.create_newspaper
    make_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())
