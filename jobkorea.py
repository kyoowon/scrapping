import requests # requests is an elegant and simple HTTP library for Python, built for human beings.
from bs4 import BeautifulSoup # bs4 is a Python library for pulling data out of HTML and XML files.

Page_num = 1
URL = f"http://www.jobkorea.co.kr/starter/?chkSubmit=1&schCareer=1&schLocal=I000,B000&schPart=10016&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&schType=0&schGid=0&schOrderBy=0&schTxt="


def extract_last_pages():
	result = requests.get(URL)
	soup = BeautifulSoup(result.text, 'html.parser') # soup은 추출된 data
	pagination = soup.find("div", {"class": "tplPagination"}) # div 태그에 class, "tplPagination"인 data 추출
	links = pagination.find_all('a')
	pages = []
	for link in links:
		pages.append(int(link.string))
	max_page = pages[-1]
	return max_page



def extract_job(html):
	company = html.find("a", {"class":"coLink"})
	title = html.find("a", {"class", "link"})
	if company is not None:
		company = company.string.strip('\n')
	if title is not None:
		href = title["href"].strip('\n')
		title = title.get_text().strip('\n')
	if company is not None and title is not None:
		return {
			'company' : company, 
			'title' : title, 
			'link' : f"www.jobkorea.co.kr{href}"
		}



def extract_jobs(last_page):
	jobs = []
	for page in range(last_page):
		print(f"scrapping page JobKorea: {page}")
		result = requests.get(f"{URL}&page={Page_num + page}")
		soup = BeautifulSoup(result.text, 'html.parser')
		results = soup.find_all("li")
		for result in results:
			job = extract_job(result)
			if job is not None:
				jobs.append(job)
	return jobs

def get_jobs():
	last_pages = extract_last_pages()
	jobs = extract_jobs(last_pages)
	return jobs