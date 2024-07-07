from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task

crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'What I Eat To Stay LEAN | A Day In My Life + Full Day Of Eating'})
print(result)