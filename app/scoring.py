from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load Spacy NLP model
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    """Extracts skills from text using NLP."""
    skill_keywords = [
    # Programming Languages
    "Python", "SQL", "Java", "JavaScript", "C", "C++", "C#", "R", "Go", "Swift", "Kotlin", 
    "Rust", "Scala", "TypeScript", "Objective-C", "Ruby", "PHP", "Dart", "Shell Scripting", 
    "Bash", "PowerShell", "MATLAB", "Perl", "Haskell", "Lua",

    # Web Development
    "HTML", "CSS", "React", "Node.js", "Angular", "Vue.js", "Django", "Flask", "Spring Boot",
    "ASP.NET", "Next.js", "Nuxt.js", "Svelte", "Tailwind CSS", "Bootstrap", "GraphQL", 
    "FastAPI", "Express.js", "NestJS",

    # AI, Machine Learning & Data Science
    "Machine Learning", "Deep Learning", "Data Science", "NLP", "Computer Vision",
    "Reinforcement Learning", "MLOps", "Jupyter", "Scikit-learn", "TensorFlow", "Keras", 
    "PyTorch", "XGBoost", "LightGBM", "Hugging Face", "AutoML", "OpenCV", "H2O.ai", 
    "Data Mining", "Feature Engineering", "Explainable AI (XAI)", "LLMs", "LangChain",
    "Vector Databases", "RAG (Retrieval-Augmented Generation)", "Generative AI", "Prompt Engineering",

    # Databases & Data Engineering
    "PostgreSQL", "MySQL", "MongoDB", "NoSQL", "SQL Server", "Oracle", "Redis", "DynamoDB", 
    "Firestore", "Cassandra", "Elasticsearch", "BigQuery", "Redshift", "Snowflake", "Neo4j", 
    "Firebase", "PL/SQL", "T-SQL", "DuckDB", "ClickHouse", "ETL Pipelines", "Data Lakehouse",
    
    # Cloud & DevOps
    "AWS", "Azure", "Google Cloud Platform", "Cloud Computing", "Serverless", "Terraform",
    "Ansible", "Docker", "Kubernetes", "Jenkins", "Git", "GitHub Actions", "CI/CD", "CloudFormation",
    "VPC", "Load Balancing", "Cloud Security", "DevOps", "Site Reliability Engineering (SRE)",
    "ArgoCD", "Pulumi", "Istio", "Service Mesh", "FinOps", "Multi-cloud Architecture",

    # Big Data & Analytics
    "Big Data", "Hadoop", "Apache Spark", "Kafka", "Flink", "Hive", "Airflow", "Beam",
    "Data Pipelines", "Data Warehousing", "ETL", "Data Lake", "HDFS", "MapReduce",
    "Druid", "Delta Lake", "Apache Iceberg", "PrestoDB",

    # Cybersecurity & Ethical Hacking
    "Penetration Testing", "Network Security", "Ethical Hacking", "SIEM", "IDS/IPS", "SOC",
    "Firewalls", "SSL/TLS", "Zero Trust Security", "IAM", "OAuth", "SAML", "Cyber Threat Intelligence",
    "Endpoint Security", "Risk Assessment", "Encryption", "OWASP", "Cloud Security", "Bug Bounty",
    "Threat Modeling", "DevSecOps", "Blockchain Security",

    # Networking & System Administration
    "TCP/IP", "DNS", "DHCP", "VPN", "SDN", "MPLS", "Wireshark", "Linux Administration",
    "Windows Server", "Active Directory", "LDAP", "VMware", "KVM", "Hyper-V", "Nagios",
    "Zabbix", "Prometheus", "Grafana", "Load Balancers", "Networking Automation",

    # Business Intelligence & Visualization
    "Tableau", "Power BI", "DAX", "Looker", "Data Visualization", "Excel", "Google Data Studio",
    "Matplotlib", "Seaborn", "Pandas", "dbt (Data Build Tool)", "Superset", "Streamlit",

    # Software Testing & QA
    "Selenium", "Appium", "Test Automation", "Unit Testing", "TDD", "BDD", "Cypress",
    "Load Testing", "Performance Testing", "API Testing", "JUnit", "PyTest", "Katalon",
    "Playwright", "Chaos Engineering",

    # Mobile Development
    "Android Development", "iOS Development", "React Native", "Flutter", "Xamarin",
    "SwiftUI", "Jetpack Compose", "KMM (Kotlin Multiplatform Mobile)", "Mobile UI/UX",

    # Emerging Technologies
    "Blockchain", "Quantum Computing", "Edge Computing", "IoT", "AI Security",
    "Robotic Process Automation", "Chatbots", "AR/VR", "Metaverse", "5G", 
    "Self-driving AI", "AI-powered Code Generation (Copilot, CodeWhisperer)", "Synthetic Data",

    # Project Management & Agile Methodologies
    "Agile", "Scrum", "Kanban", "Jira", "Confluence", "PMP", "ITIL", "Risk Management",
    "Stakeholder Management", "Change Management", "Incident Management", "Lean Six Sigma",
    "OKRs", "SAFE Agile", "Design Thinking",

    # Software Architecture & Engineering
    "Microservices", "Monolith to Microservices Migration", "Event-Driven Architecture",
    "API Gateway", "Serverless Architecture", "CQRS (Command Query Responsibility Segregation)",
    "Hexagonal Architecture", "DDD (Domain-Driven Design)", "Service Oriented Architecture (SOA)",
    "Observability", "Telemetry", "OpenTelemetry", "Distributed Systems"
]

    extracted_skills = set()
    doc = nlp(text)

    for token in doc:
        if token.text in skill_keywords:
            extracted_skills.add(token.text)

    return extracted_skills

def compute_match_score(resume_text, job_desc_text):
    """Calculates resume-job match score and identifies missing skills"""
    # TF-IDF Similarity
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc_text])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    match_score = round(similarity * 100, 2)

    # Extract skills from both
    resume_skills = extract_skills(resume_text)
    job_desc_skills = extract_skills(job_desc_text)
    missing_skills = job_desc_skills - resume_skills

    return {
        "match_score": match_score,
        "missing_skills": list(missing_skills)
    }
