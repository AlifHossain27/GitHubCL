#! /usr/bin/env python3
import os
import requests
import webbrowser
from simple_term_menu import TerminalMenu

class GitHubCL():
    def __init__(self):
        self.GITHUB_TOKEN = ""
        self.API_URL = "https://api.github.com"
        self.HEADER = {
            "Authorization": "token " + self.GITHUB_TOKEN,
            "Accept": "application/vnd.github+json"
        }
        self.REPO_PATH = "/home/alan/Professional/Programming/Projects/"
        self.GITHUB_USER = "AlifHossain27"

    def _createRepo(self):
        repoName = str(input("Enter the Repository name: "))
        repoDescription = str(input("Enter the Repository description: "))
        repoIsPrivate = str(input("Do you want to keep the Repository private(y/n): ")).lower()
        
        if repoIsPrivate == "y":
            payload= '{"name": "' + repoName + '", "description": "' + repoDescription + '", "private": true }'
        if repoIsPrivate == "n":
            payload= '{"name": "' + repoName + '", "description": "' + repoDescription + '", "private": false }'
        else:
            print("There might be some typo or problem with the input values !!!")
            breakpoint
        
        try:
            r = requests.post(self.API_URL + "/user/repos", data=payload, headers=self.HEADER)
            r.raise_for_status()
            os.chdir(self.REPO_PATH)
            os.system(f"git clone https://github.com/AlifHossain27/{repoName}.git")
            os.chdir(self.REPO_PATH + repoName)
            os.system("code .")
            os.system("clear")
            print(f"{repoName} has been created successfully")
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)


        
    def _deleteRepo(self):
        repoName = str(input("Enter repository name: "))
        try:
            r = requests.delete(f"{self.API_URL}/repos/{self.GITHUB_USER}/{repoName}", headers=self.HEADER)
            r.raise_for_status()
            os.chdir(self.REPO_PATH)
            os.system(f"rm -r {repoName}")
            print(f"{repoName} has been deleted")
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

    def _listRepos(self):
        pass

    def _searchUserRepos(self):
        pass

    def _mainScreen(self):
        mainOptions = ["Create a new repository", "Delete a repository", "List repositories", "Search User", "Quit"]
        mainLoopQuit = False

        mainMenu = TerminalMenu(mainOptions, title = "========GITHUBCL========")

        while not mainLoopQuit:
            mainOptionsIndex = mainMenu.show()
            mainOptionsChoice = mainOptions[mainOptionsIndex]

            if mainOptionsChoice == "Quit":
                mainLoopQuit = True
            if mainOptionsChoice == "Create a new repository":
                try:
                    self._createRepo()
                except:
                    print("Something went wrong please try again with valid inputs")
                continue
            if mainOptionsChoice == "Delete a repository":
                self._deleteRepo()
            if mainOptionsChoice == "List repositories":
                self._listRepos()
            if mainOptionsChoice == "Search User":
                self._searchUserRepos()
            


if __name__ == '__main__':
    GitHubCL()._mainScreen()