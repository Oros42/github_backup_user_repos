#!/usr/bin/python
# -*- coding: utf-8 -*-
# author Oros
# date 2015/08/25
# license CC0
#
# This program clone and pull all repositories of one or more user for backup.
# Work with python 2 and 3
#
import os
from json import loads as json_loads
from sys import exit, argv
from time import strftime, gmtime
try:
	import urllib.request as urllib
except ImportError:
	import urllib
if os.system("which git>/dev/null"):
	exit("\033[31mYou need to setup git\033[0m\nsudo apt-get install git")

# path where repositories are clone
repo_path="{}/repositories/".format(os.path.dirname(os.path.realpath(__file__)))

if not argv[1:]:
	exit("\033[31mNeed username in argument !\033[0m Like :\npython {n} username [username2 username3 ...]".format(n=argv[0]))
else:
	for user in argv[1:]:
		url="https://api.github.com/users/{}/repos".format(user)
		github_page = urllib.urlopen(url)
		if github_page:
			github_json = json_loads(github_page.read(1000000).decode('utf-8'))
			if github_json:
				i=1
				nb_repo=len(github_json)
				print("{} repositories from {}:".format(nb_repo,user))
				for item in github_json:
					if os.path.exists("{}{}".format(repo_path,item["full_name"])):
						file_time=strftime("%Y-%m-%dT%H:%M:%SZ",gmtime(os.path.getmtime("{}{}".format(repo_path,item["full_name"]))))
						if item["updated_at"] > file_time or item["pushed_at"] > file_time:
							print("repo {}/{}\t: update {} in {}{}".format(i, nb_repo,item["clone_url"], repo_path, item["full_name"]))
							os.system("git --git-dir={}{}/.git pull".format(repo_path, item["full_name"]))
						else:
							print("repo {}/{}\t: no update for {}{}".format(i, nb_repo, repo_path ,item["full_name"]))
					else:
						print("repo {}/{}\t: clone {} in {}{}".format(i, nb_repo,item["clone_url"], repo_path, item["full_name"]))
						os.system("git clone {} {}{}".format(item["clone_url"], repo_path, item["full_name"]))
					i+=1
			else:
				exit("\033[31m{} is not a json file :-/\033[0m".format(url))
		else:
			exit("\033[31mError when try to open {}\033[0m".format(url))
