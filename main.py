from jobkorea import get_jobs as get_jobkorea_jobs
from saramin import get_jobs as get_saramin_jobs
from save import save_to_file

job_jobkorea = get_jobkorea_jobs()
job_saramin = get_saramin_jobs()

jobs = job_jobkorea + job_saramin
save_to_file(jobs)