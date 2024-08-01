import requests

API_BASE_URL = "https://rdb.altlinux.org/api/"

def fetch_binary_packages(branch):
    """
    Получает список бинарных пакетов для заданного branch.
    """
    url = f"{API_BASE_URL}/export/branch_binary_packages/{branch}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['packages']
    else:
        raise Exception(f"Failed to fetch packages for branch {branch}. Status code: {response.status_code}")

def compare_package_lists(packages1, packages2):
    """
    Сравнивает два списка пакетов и возвращает JSON с результатами сравнения.
    """
    set1 = {(pkg['name'], f"{pkg['version']}-{pkg['release']}") for pkg in packages1}
    set2 = {(pkg['name'], f"{pkg['version']}-{pkg['release']}") for pkg in packages2}

    in_first_only = [{"name": pkg[0]} for pkg in set1 - set2]
    in_second_only = [{"name": pkg[0]} for pkg in set2 - set1]
    greater_in_first = [{"name": pkg1['name'], "version-release": f"{pkg1['version']}-{pkg1['release']}"} 
                        for pkg1 in packages1 
                        for pkg2 in packages2 
                        if pkg1['name'] == pkg2['name'] and f"{pkg1['version']}-{pkg1['release']}" > f"{pkg2['version']}-{pkg2['release']}"]

    return {
        "in_first_only": in_first_only,
        "in_second_only": in_second_only,
        "greater_in_first": greater_in_first
    }
