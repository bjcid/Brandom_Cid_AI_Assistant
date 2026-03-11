import streamlit as st
import os
from openai import OpenAI

# ---- Load API key (local or Streamlit Cloud) ----
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except:
    api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# ---- Page configuration ----
st.set_page_config(page_title="Brandom Cid AI Assistant")

st.title("🤖 AI Assistant – Brandom Cid")
st.write("Ask anything about my experience, skills and basically why you should hire me 😉")

# ---- Knowledge base about you ----
context = """
Brandom Cid is a passionate engineer and Ph.D. with a strong focus on research, data analysis, 
machine learning, feature engineering, artificial intelligence, and project management. 
Motivated to apply my problem-solving skills and contribute to impactful projects.


EXPERIENCE

Ops Data Analyst
Nissan Motor Corporation · Full time
jun. 2025 - current job · 10 months
Nashville, Tennessee, USA · Remote
✅️ Reporting to IS infrastructure Manager and Senior Manager.
✅️ Collaborated with a global team (USA, India, Brazil and Mexico) to ensure data accuracy, improve customer experience and optimize sevice desk activities, supporting collective cost savings of $7M in 2025.
✅️ Worked with cloud-based environments to process, store, and visualize large-scale data, reducing in 30% the cloud resources.
✅️ Automated ETL pipelines and deployed monitoring solutions for SLAs, incidents, requests, and demands, enhancing decision-making efficiency.
✅️ Leveraged AI/ML-driven techniques, including Time Series predictions and NLP
for accurate ticket classification, achieving over 90% accuracy.


Graduate Researcher
Instituto Politécnico Nacional · Full time
sept. 2019 - aug. 2025 · 6 years
Mexico City, Mexico · Hybrid
✅️ Led end-to-end 4+ multidisciplinary projects focused on the application of AI/ML and computational simulations for energy storage and environmental remediation.
✅️ Developed and optimized custom Python scripts to automate data queries, visualizations, and routine processes, reducing task execution time by over 50%.
✅️ Coordinate teams of 4–8 members and optimize the use of shared high-performance computing resources, resulting in a 20% reduction of computational waste and associated costs.
✅️ Mentored and supervised 4 junior graduate researchers, providing guidance on data workflows, research methodology, and best practices.
✅️ Presented research findings at 15+ national/international conferences, and served on the evaluation committee of 2 Master’s students.
✅️ Reached over 220 citations and 11 high-impact JCR publications.


Associate Researcher
Lehigh University · Full time
mar. 2024 - sept. 2024 · 7 months
Belén, Pennsylvania, USA · On site
✅️ Developed a AI/ML model that integrates published information with quantum simulations to accurately predict electronic properties of nanomaterials, achieving 97% R² accuracy, reducing prediction time from 1 week to a few minutes.
✅️ Collaborated with a 5-member research team, handling complex databases and applying ML algorithms and feature engineering to extract high-value insights for next-generation materials discovery.
✅️ Automated data extraction processes using web scraping (BeautifulSoup), reducing information gathering time by over 60% and streamlining the creation of datasets.


Performance Jr. Engineer 
DHL Express · Full time
jul. 2018 - feb. 2019 · 8 months
Mexico City, Mexico · On site
✅️ Generated and monitored key operational KPIs for the Metropolitan area of Mexico, providing data-driven insights that supported strategic decision-making across logistics operations.
✅️ Analyzed trends and performance metrics, delivering regular reports to the Operational Management Team to drive improvements in service quality and efficiency.


Quality Assurance Trainee
Aeromar · Trainee
jan. 2017 - jul. 2017 · 7 months
Mexico City, Mexico · On site
✅️ Managed and updated operational databases, ensuring accuracy and reliability of quality-related data for performance tracking and reporting.
✅️ Mapped business processes to identify inefficiencies, supporting the development of improved workflows and standard operating procedures.


EDUCATION

Instituto Politécnico Nacional
Doctor of Philosophy - PhD, Materials Engineering
2021 - 2025

Instituto Politécnico Nacional
Master's degree, Engineering Sciences
2019 - 2021

Instituto Politécnico Nacional
Engineer's degree, Aeronautical Engineering 
2013 - 2018

USP - Universidade de São Paulo
Bachelor of Applied Science - BASc, Aeronautical/Aerospace Engineering 
2017 - 2018


LANGUAGES

Proeficient on English and Portuguese with experience living in the US and Brazil


AWARDS

Best STEM PhD Thesis of the  Instituto Politécnico Nacional - This award recognizes the best doctoral thesis in the STEM fields at the Instituto Politécnico Nacional, highlighting Brandom Cid's outstanding research contributions and academic excellence in his PhD work. In this project I mixed AI/ML techniques with computational simulations to predict properties of novel materials, achieving high accuracy and significant advancements in the field of materials science.
Best PhD student performance of the Instituto Politécnico Nacional - I received this award for having the best performance as a PhD student, involving projects presentations, publications, and overall contribution to the research community during my doctoral studies.
More than 11 high impact papers published on high impact journals
More than 250 citations
Presented more than 15 projects on national and international conferences.


CERTIFICATIONS

Foundations of Project Management
Google
apr. 2025


SKILLS

Agentic AI
LLMs
MySQL
Scrum/Agile
ServiceNow
PowerBI
Machine Learning
Project Management
Linux
Python
Analytical Skills
Storytelling
Communication
Teamwork
Data analysis


CHALLENGES

Throughout my career, I have faced the challenge of bridging advanced research and real-world data applications across different environments and industries. During my research stay in the United States at Lehigh University, I worked on developing neural network models for the discovery and prediction of properties in novel nanomaterials, which required managing complex scientific datasets, designing machine learning architectures, and collaborating within multidisciplinary research teams. This experience pushed me to translate theoretical machine learning concepts into practical computational tools capable of supporting materials discovery. Later, in my role as a Data Analyst at Nissan within the IT Service Management (ITSM) global team, I encountered a different set of challenges—working with large-scale operational data in cloud environments, improving data pipelines, and transforming raw service data into actionable insights for decision-making. Balancing rigorous scientific thinking with the need for scalable, efficient solutions in an enterprise environment has been one of the most significant challenges in my career, but it has also strengthened my ability to apply data science, machine learning, and analytical thinking to solve complex problems in both research and industry contexts.


GENERAL

Companies should hire me because I bring a unique combination of advanced research expertise and practical industry experience in data science and machine learning. As a PhD candidate with a strong background in developing neural network models and analyzing complex datasets, I have demonstrated the ability to transform large amounts of data into meaningful insights and predictive solutions. My research experience at Lehigh University allowed me to apply machine learning techniques to challenging scientific problems, strengthening my skills in Python, model development, and working with high-dimensional data. At the same time, my role as a Data Analyst at Nissan has given me hands-on experience with real-world business data, where I have improved data pipelines, optimized cloud resource usage, and delivered insights that support operational decision-making. This combination of analytical rigor, technical proficiency, and business awareness enables me to quickly understand complex problems and build scalable data-driven solutions that create measurable value for organizations.


COMUNICATION

Companies should hire me because I combine strong data science expertise with the ability to clearly communicate complex ideas and insights to diverse audiences. In my current role as a Data Analyst at Nissan, I regularly transform technical analyses and operational data into understandable insights for managers and stakeholders, enabling data-driven decisions across teams. Additionally, through presenting my work at national and international conferences and publishing scientific articles, I have developed the ability to communicate technical findings in a structured and impactful way. This combination of technical depth and strong communication skills allows me to bridge the gap between data, technology, and business needs, helping organizations fully leverage the value of their data.


PROFESSIONAL INTERESTS

I am an engineer with a strong background in AI/ML and data analysis. I currently develop a Data Analyst role at Nissan North America. However, given the financial situation of my current company, where operations in different areas may soon cease, I am actively seeking a new opportunity where I can contribute with my technical expertise, problem-solving skills, and passion for data-driven innovation. Im looking for a company where I can contribute for long term, grow professionally and personally, and be part of a team that values creativity, collaboration, and impact. I am particularly interested in roles related to Data Analysis, Data Science, Machine Learning Engineering, AI Engineering, and similar positions where I can apply my skills to solve complex problems and drive meaningful outcomes.


Current Salary
$51,200 mexican pesos per month (approximately $2,600 USD per month), however, in my case, salary is not the most important factor, but rather the opportunity to contribute, grow and be part of a great team and company for long term.


PERSONAL INFORMATION

Beyond my professional work, I value maintaining a balanced and active lifestyle that supports both my productivity and creativity. I enjoy playing tennis and staying physically active, as regular exercise helps me maintain focus, discipline, and resilience—qualities that I also bring into my professional work. In my free time, I like listening to rock music, which has always been a source of energy and inspiration for me. These personal interests reflect my commitment to continuous growth, curiosity, and maintaining a healthy balance between professional challenges and personal well-being.

"""

# ---- Chat history ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---- Chat input ----
question = st.chat_input("Ask something about me...")

if question:

    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.write(question)

    prompt = f"""
You are an AI assistant answering questions about Brandom Cid. He is trying to get a job and you are helping him by answering questions about his experience, skills, education, awards, certifications and basically anything that can be relevant for a recruiter to know about him. Im aplying for Data Analyst, Data Scientist, Machine Learning Engineer, AI Engineer and related positions, so adapt the response accordin these roles.

Use ONLY the information below to answer.

If another name or last name is mentioned, say you don't have information about that person.

Information:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)