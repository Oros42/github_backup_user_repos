#!/usr/bin/python
# -*- coding: utf-8 -*-
# author Oros
# date 2015/07/12
# license CC0
#
# This program clone and pull all repositories of one or more user for backup.
# Work with python 2 and 3
#
import os
from json import loads as json_loads
from sys import exit, argv
from time import strftime, localtime
try:
	import urllib.request as urllib
except ImportError:
	import urllib
if os.system("which git>/dev/null"):
	exit("\033[31mYou need to setup git\033[0m\nsudo apt-get install git")

# path where repositories are clone
repo_path="./repositories/"

if not argv[1:]:
	exit("\033[31mNeed username in argument !\033[0m Like :\npython {n} username [username2 username3 ...]".format(n=argv[0]))
else:
	for user in argv[1:]:
		url="https://api.github.com/search/repositories?q=user%3A{}&type=Repositories".format(user)
		github_page = urllib.urlopen(url)
		if github_page:
			github_json = json_loads(github_page.read(1000000).decode('utf-8'))
			if github_json:
				if github_json["incomplete_results"]:
					print("\033[31m/!\TODO\033[0m : incomplete_results not finish to code")
				print("{} repositories from {}:".format(github_json["total_count"],user))
				i=1
				for item in github_json["items"]:
					if os.path.exists("{}{}".format(repo_path,item["full_name"])):
						if item["updated_at"] > strftime("%Y-%m-%dT%H:%M:%SZ",localtime(os.path.getmtime("{}{}".format(repo_path,item["full_name"])))):
							print("repo {}/{}\t: update {} in {}{}".format(i, github_json["total_count"],item["clone_url"], repo_path, item["full_name"]))
							os.system("git --git-dir={}{}/.git pull".format(repo_path, item["full_name"]))
						else:
							print("repo {}/{}\t: no update for {}".format(i, github_json["total_count"],item["full_name"]))
					else:
						print("repo {}/{}\t: clone {} in {}{}".format(i, github_json["total_count"],item["clone_url"], repo_path, item["full_name"]))
						os.system("git clone {} {}{}".format(item["clone_url"], repo_path, item["full_name"]))
					i+=1
			else:
				exit("\033[31m{} is not a json file :-/\033[0m".format(url))
		else:
			exit("\033[31mError when try to open {}\033[0m".format(url))
