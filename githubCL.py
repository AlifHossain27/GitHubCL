#! /usr/bin/env python3
import os
import requests
from simple_term_menu import TerminalMenu

class GitHubCL():
    def __init__(self):
        self.GITHUB_TOKEN = "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"
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
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)


        
    def _deleteRepo(self):
        pass

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
                    print("Something went wrong try again with correct info")
                    continue
                continue
            if mainOptionsChoice == "Delete a repository":
                self._deleteRepo()
            if mainOptionsChoice == "List repositories":
                self._listRepos()
            if mainOptionsChoice == "Search User":
                self._searchUserRepos()
            


if __name__ == '__main__':
    GitHubCL()._mainScreen()