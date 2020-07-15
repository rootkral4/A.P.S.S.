#Import
import requests
import time
from pyfiglet import Figlet
from google import google
from bs4 import BeautifulSoup
from termcolor import colored

f = Figlet(font='slant')
print(colored(f.renderText("A.P.S.S"), "magenta"))
print(colored("@kral4", "magenta"))
thingtosearch = input(colored("Who Are We Looking For :", "cyan"))
print(colored("Running Too Much Search May Cause Ban From Google\nIf You Got Banned From Google Try To Use VPN", "red"))
#Google Search
try:
	
	print(colored("[?]Searching On Google...", "blue"))
	search_results = google.search("intext:" + thingtosearch, 1)
	for result in search_results:
		print(colored("[-]URL :" + result.link + " | " + result.name, "yellow"))
except:
	pass
	
#Youtube Account
time.sleep(10)
try:
	print(colored("[?]Searching On Youtube...", "blue"))
	youtube_results = google.search("intext:" + thingtosearch + " inurl:youtube.com", 1)
	for youtube in youtube_results:
		print(colored("[-]URL :" + youtube.link + " | " + youtube.name, "yellow"))
except:
	pass
#Facebook Account
time.sleep(10)
try:
	print(colored("[?]Searching On Facebook...", "blue"))
	facebook_results = google.search("intext:" + thingtosearch + " inurl:facebook.com", 1)
	for facebook in facebook_results:
		print(colored("[-]URL :" + facebook.link + " | " + facebook.name, "yellow"))
except:
	pass

#Twitch Account
time.sleep(10)
try:
	print(colored("[?]Searching On Twitch...", "blue"))
	twitch_results = google.search("intext:" + thingtosearch + " inurl:twitch.tv", 1)
	for twitch in twitch_results:
		print(colored("[-]URL :" + twitch.link + " | " + twitch.name, "yellow"))
except:
	pass
		
#Steam Account
time.sleep(2)
print(colored("[?]Searching For Steam Account...", "blue"))
def steam():
	steam = requests.get('https://steamcommunity.com/id/' + thingtosearch)
	soup = BeautifulSoup(steam.text, 'html.parser')
	steamresult = soup.find("div", {"class": "persona_name persona_level"}).text
	if "Level" in steamresult:
		print(colored("[+]Account Found !\n[+]Steam URL :https://steamcommunity.com/id/" + thingtosearch, "green"))	
		print(colored("[?]Getting Information About Target {Steam}", "blue"))
		try:
			steaminfo1 = soup.find("span", {"class": "actual_persona_name"}).text
			print(colored("[-]" + steaminfo1, "yellow"))
		except:
			pass
		try:
			steaminfo2 = soup.find("div", {"class": "profile_summary"}).get_text(strip=True)
			print(colored("[-]" + steaminfo2, "yellow"))
		except:
			pass
		try:
			steaminfo3 = soup.find("div", {"class": "header_real_name"}).get_text(strip=True)
			print(colored("[-]" + steaminfo3, "yellow"))
		except:
			pass
		try:
			steaminfo4 = soup.find("div", {"class": "persona_name persona_level"}).get_text(strip=True)
			print(colored("[-]" + steaminfo4, "yellow"))
		except:
			pass
		try:
			steaminfo5 = soup.find("span", {"class": "profile_count_link_total"}).get_text(strip=True)
			print(colored("[-]Badges " + steaminfo5, "yellow"))
		except:
			pass
		try:
			steaminfo6 = soup.find('a', {'href': 'https://steamcommunity.com/id/' + thingtosearch +'/friends/'}).get_text(strip=True)
			print(colored("[-]" + steaminfo6, "yellow"))
			print(colored("[-]https://steamcommunity.com/id/" + thingtosearch + "/friends/", "yellow"))
		except:
			pass
		try:
			steaminfo7 = soup.find('a', {'href': 'https://steamcommunity.com/id/' + thingtosearch +'/games/?tab=all'}).get_text(strip=True)
			print(colored("[-]" + steaminfo7, "yellow"))
			print(colored('[-]https://steamcommunity.com/id/' + thingtosearch +'/games/?tab=all', "yellow"))
		except:
			pass
		try:
			steaminfo8 = soup.find('a', {'href': 'https://steamcommunity.com/id/' + thingtosearch +'/screenshots/'}).get_text(strip=True)
			print(colored("[-]" + steaminfo8, "yellow"))
			print(colored('[-]https://steamcommunity.com/id/' + thingtosearch +'/screenshots/', "yellow"))
		except:
			pass
		try:
			steaminfo9 = soup.find('a', {'href': 'https://steamcommunity.com/id/' + thingtosearch +'/videos/'}).get_text(strip=True)
			print(colored("[-]" + steaminfo9, "yellow"))
			print(colored('[-]https://steamcommunity.com/id/' + thingtosearch +'/videos/', "yellow"))
		except:
			pass
	else:
		print("Not Found")


try: steam()
except: 
	print(colored("Not Found", "red"))
	pass
	
#Github Account
time.sleep(2)
def github():
	print(colored("[?]Searching For Github Account...", "blue"))
	try:
		print(colored("[?]Searching On Github...", "blue"))
		search_results = google.search("intext:" + thingtosearch + " inurl:github", 1)
		for result in search_results:
			print(colored("[-]URL :" + result.link + " | " + result.name, "yellow"))
	except:
		pass
	github = requests.get('https://github.com/' + thingtosearch)
	githubsoup = BeautifulSoup(github.text, 'html.parser')
	githubresult = githubsoup.find("div", {"class": "js-pinned-items-reorder-container"}).get_text()
	if "Popular" or "Pinned" in githubresult:
		print(colored("[+]Github Account Found !", "green"))
		print(colored("[+]Github URL :https://github.com/" + thingtosearch, "green"))
		print(colored("[?]Getting Information About Target {Github}", "blue"))
		try:
			githubinfo6 = githubsoup.find("div", {"class": "p-note user-profile-bio mb-3 js-user-profile-bio f4"}).get_text()
			print(colored("[-]" + githubinfo6, "yellow"))
		except:
			pass
		try:
			githubinfo1 = githubsoup.find("span", {"class": "p-org"}).get_text()
			print(colored("[-]" + githubinfo1, "yellow"))
		except:
			pass
		try:
			githubinfo2 = githubsoup.find("span", {"class": "p-label"}).get_text()
			print(colored("[-]" + githubinfo2, "yellow"))
		except:
			pass
		try:
			githubinfo3 = githubsoup.find("a", {"class": "link-gray-dark","rel": "nofollow me"}).get_text()
			print(colored("[-]" + githubinfo3, "yellow"))
		except:
			pass
		try:
			githubinfo4 = githubsoup.find("span", {"class": "text-bold text-gray-dark"}).get_text()
			print(colored("[-]" + "Followed By " + githubinfo4 + " Users", "yellow"))
			print(colored("[-]" + "https://github.com/" + thingtosearch + "?tab=followers", "yellow"))
		except:
			pass
		try:
			githubinfo5 = githubsoup.find("a", {"class": "link-gray no-underline no-wrap","href": "/" + thingtosearch + "?tab=following"}).get_text(strip=True)
			print(colored("[-]" + "Following " + githubinfo5[0] + " Users", "yellow"))
			print(colored("[-]" + "https://github.com/" + thingtosearch + "?tab=following", "yellow"))
		except:
			pass
		try:
			githubinfo7 = githubsoup.find("h2", {"class": "f4 text-normal mb-2"}).get_text(strip=True)
			print(colored("[-]" + githubinfo7[0] + " Contributions in the last year", "yellow"))
		except:
			pass
	else:
		print("Not Found")
		
try: github()
except: 
	print(colored("[+]Not Found", "red"))
	pass

#Instagram Account
time.sleep(5)
print(colored("[?]Searching For Instagram Account...", "blue"))
def instagram():
	try:
		print(colored("[?]Searching On Instagram...", "blue"))
		instagram_results = google.search("intext:" + thingtosearch + " inurl:instagram.com", 1)
		for instagram in instagram_results:
			print(colored("[-]URL :" + instagram.link + " | " + instagram.name, "yellow"))
	except:
		pass
	instagram = requests.get('https://www.instagram.com/' + thingtosearch)
	if instagram.status_code == 200:
		print(colored("[+]Account Found !\n[+]Instagram URL :https://www.instagram.com/" + thingtosearch, "green"))	
	else:
		print("Not Found")



try: instagram()
except: 
	print(colored("Not Found", "red"))
	pass



