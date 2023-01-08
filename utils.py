import sqlite3


def get_all(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        result = []
        print()

        for item in conn.execute(query).fetchall():
            print(item)
            s = dict(item)

            result.append(s)

        return result


def get_one(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute(query).fetchone()

        if res is None:
            return None
        else:
            return dict(res)


def search_by_cast(name1: str = 'Rose McIver', name2: str = 'Ben Lamb'):
    query = f"""
    SELECT * from netflix
    WHERE  "cast" like '%{name1}%' and "cast" like '%{name2}%';
    """

    cast = []
    result = get_all(query)
    for key, values in result.items():
        if values > 2:
            cast.append(key)

    return cast







def get_by_type_genre(type_movie, release_year_movie, listed_in_movie):
    """

    :param type_movie:
    :param release_year_movie:
    :param listed_in_movie:
    :return:
    """
    with sqlite3.connect('netflix.db') as con:
        result = []
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        query = f"""
        SELECT title, description
        from netflix
        WHERE "type" = '{type_movie}'
        AND netflix.release_year = {release_year_movie}
        AND listed_in LIKE  '%{listed_in_movie}%'
        """
        cur.execute(query)
        query_result = cur.fetchall()
        for data in query_result:
            movie = {
                "title": data["title"],
                "description": data["description"],
            }
            result.append(movie)
            return result
