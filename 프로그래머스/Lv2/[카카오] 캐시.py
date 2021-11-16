def solution(cacheSize, cities):
    time = 0

    if cacheSize == 0:
        time = len(cities) * 5
        return time

    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:  # cache hit
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1
        else:  # cache miss
            if len(cache) == cacheSize:  # cacheSize=0일때 에러발생하므로 앞에서 처리
                cache.pop(0)
            cache.append(city)
            time += 5

    return time