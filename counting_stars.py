import requests
import json

# url = ('https://api.github.com/users/emaadmanzoor/repos?per_page=1000')
# url2 = ('https://api.github.com/users/emaadmanzoor/repos?page=2&per_page=1000')

max = 100
x = 0
all_repos = []
while max == 100:
    x += 1
    test_url = ('https://api.github.com/users/emaadmanzoor/repos?' + 'page=' + str(x) + '&per_page=1000')
    #print(test_url)
    r = requests.get(test_url)
    repos = r.json()
    all_repos += repos
    max = len(repos)

test_stars = 0
for i in range(0,len(all_repos)):
    stars = all_repos[i]['stargazers_count']
    test_stars += stars

print(f'Total amount of stars is: {test_stars}')


# r = requests.get(url)
# r2 = requests.get(url2)
#
# # print(r.status_code)
# # print(r.raise_for_status())
#
# repos = r.json()
# repos2 = r2.json()

#Testing Code
# print(type(repos), len(repos))
# print(type(repos2), len(repos2))
# print(repos[1])

# for i in repos:
#     print(i['name'], i['stargazers_count'])
#
# for i in repos2:
#     print(i['name'], i['stargazers_count'])


# total_stars = 0
# for i in range(0,len(repos)):
#     stars = repos[i]['stargazers_count']
#     total_stars += stars
#     #print(total_stars)
#
# for i in range(0,len(repos2)):
#     stars = repos2[i]['stargazers_count']
#     total_stars += stars
#
# print(f'Total amount of stars is: {total_stars}')
