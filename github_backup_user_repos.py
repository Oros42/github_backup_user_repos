#!/usr/bin/python
# -*- coding: utf-8 -*-
# author Oros
# date 2020-06-07
# license CC0
#
# This program clone and pull all repositories of one or more user for backup.
# Work with python 2 and 3
#
import os
from json import loads as json_loads
from sys import exit, argv
from time import strftime, gmtime
from optparse import OptionParser
try:
    import urllib.request as urllib
except ImportError:
    import urllib
if os.system("which git>/dev/null"):
    exit("\033[31mYou need to setup git\033[0m\nsudo apt-get install git")

def cloneRepo(user, outputDir, force):
    if user == "":
        exit("\033[31mNeed username in argument !\033[0m")
    if outputDir == "":
        outputDir = "./repositories/"

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    os.chdir(outputDir)
    outputDir = os.getcwd() + "/"

    page = 1
    nextPage = True
    nbRepoPerPage = 50
    while nextPage:
        url="https://api.github.com/users/{}/repos?page={}&per_page={}".format(user, page, nbRepoPerPage)
        github_page = urllib.urlopen(url)
        if github_page:
            github_json = json_loads(github_page.read(1000000).decode('utf-8'))
            if github_json:
                i=1
                nb_repo=len(github_json)
                nextPage = nb_repo == nbRepoPerPage
                print("{} repositories from {}:".format(nb_repo,user))
                for item in github_json:
                    if item["full_name"] != "":
                        os.chdir(outputDir)
                        if os.path.exists("{}{}".format(outputDir, item["full_name"])):
                            file_time=strftime("%Y-%m-%dT%H:%M:%SZ",gmtime(os.path.getmtime("{}{}".format(outputDir,item["full_name"]))))
                            if force or item["updated_at"] > file_time or item["pushed_at"] > file_time:
                                print("repo {}/{}\t: update {} in {}{}".format(i, nb_repo,item["clone_url"], outputDir, item["full_name"]))
                                os.system("cd {}{}; git pull".format(outputDir, item["full_name"]))
                            else:
                                print("repo {}/{}\t: no update for {}{}".format(i, nb_repo, outputDir ,item["full_name"]))
                        else:
                            print("repo {}/{}\t: clone {} in {}{}".format(i, nb_repo,item["clone_url"], outputDir, item["full_name"]))
                            os.system("git clone {} {}{}".format(item["clone_url"], outputDir, item["full_name"]))
                    i+=1
            else:
                exit("\033[31m{} is not a json file :-/\033[0m".format(url))
        else:
            exit("\033[31mError when try to open {}\033[0m".format(url))
        page += 1


if __name__ == "__main__":
    parser = OptionParser(usage="%prog: [options]")
    parser.add_option("-u", "--user", dest="username", type="string", default="", help="Username (From https://github.com/<Username>)")
    parser.add_option("-o", "--output", dest="output", type="string", default="./repositories/", help="Path to the output directory")
    parser.add_option("-f", "--force", dest="force", action="store_true", help="Force git pull")
    (options, args) = parser.parse_args()
    user = options.username
    outputDir = options.output
    force = options.force
    cloneRepo(user, outputDir, force)
