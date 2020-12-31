import requests
from bs4 import BeautifulSoup

Page_num = 1
URL = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404%2C407%2C408%2C402%2C416&loc_mcd=101000%2C102000&job_type=1&company_type=scale001&panel_type=&search_optional_item=y&search_done=y&panel_count=y"


def extract_last_pages():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text, 'html.parser')
	pagination = soup.find("div", {"class" :"pagination"})
	links = pagination.find_all('a')
	pages = []
	for link in links:
		pages.append(int(link.string))
	max_page = pages[-1]
	return max_page

def extract_job(html):
	company = html.find("a", {"class":"str_tit"})["title"].strip('\n')
	title = html.find("div", {"class", "job_tit"}).find("a", {"class", "str_tit"})["title"].strip('\n')
	link = html.find("div", {"class", "job_tit"}).find("a", {"class", "str_tit"})["href"].strip('\n')
	return {'company' : company, 'title' : title, 'link' : f"www.saramin.co.kr{link}"}

def extract_jobs(last_page):
	jobs = []
	for page in range(last_page):
		print(f"scrapping page Saramin: {page}")
		result = requests.get(f"{URL}&page={Page_num + 0}")
		soup = BeautifulSoup(result.text, 'html.parser')
		results = soup.find_all("div", {"class" : "list_item"})
		for result in results:
			jobs.append(extract_job(result))
	return jobs

def get_jobs():
	last_pages = extract_last_pages()
	jobs = extract_jobs(last_pages)
	return jobs

