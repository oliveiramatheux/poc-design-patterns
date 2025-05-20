from abc import ABC, abstractmethod

import requests


class Github(ABC):
    @abstractmethod
    def get_user_repositories(self, user_name: str):
        pass


class GithubRepository(Github):
    def get_user_repositories(self, user_name: str):
        url = f"https://api.github.com/users/{user_name}/repos"

        response = requests.get(url)

        if response.status_code == 200:
            return [repo['name'] for repo in response.json()]

        return []


class GithubProxy(Github):
    def __init__(self):
        self.cache = {}
        self.github_repository = GithubRepository()

    def get_user_repositories(self, user_name: str):
        if user_name in self.cache:
            print("Entrou no cache")
            return self.cache[user_name]

        value = self.github_repository.get_user_repositories(user_name)

        print("Não entrou no cache")

        self.cache[user_name] = value

        return value


if __name__ == "__main__":
    repo = GithubProxy()

    print("Primeira chamada:")
    response = repo.get_user_repositories('oliveiramatheux')
    print(response)

    print("Segunda chamada:")
    response = repo.get_user_repositories('oliveiramatheux')
    print(response)

    print("Terceira chamada:")
    response = repo.get_user_repositories('oliveiramatheux')
    print(response)

    print("Quarta chamada:")
    response = repo.get_user_repositories('tiago154')
    print(response)

    print("Quinta chamada:")
    response = repo.get_user_repositories('tiago154')
    print(response)
