from django.shortcuts import render
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = Path(__file__).resolve().parent.parent
XML_NS = {'a': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

STEMDAY_2026_ENTRIES = [
    {
        'title': 'Intercept: A Mobile-First AI System for Phishing Detection',
        'authors': 'Austin Minor, Noah Moore, Jaylen Carter, Tim Pickett, Camron Gayle',
        'faculty_mentors': 'Dr. Ed Pearson',
        'keywords': 'Phishing Detection, Artificial Intelligence, Machine Learning',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Intercept is a mobile-first, artificial intelligence–based phishing detection system designed to protect job seekers, students, and employees from socially engineered email attacks before they interact with malicious content. As phishing attacks continue to increase and frequently target individuals through email communication, many traditional security solutions focus primarily on enterprise-level infrastructure rather than protecting individual users directly. This creates a gap in accessible cybersecurity tools for people who frequently check emails on mobile devices, especially in job-seeking scenarios involving recruiter communications and employment offers. Intercept addresses this problem by leveraging a machine learning–based detection approach using a Random Forest classification model to analyze email characteristics and identify potential phishing threats. The system evaluates multiple features within an email, such as suspicious language patterns, sender information, and structural indicators commonly associated with phishing attempts. By aggregating predictions from multiple decision trees, the Random Forest model improves detection stability and classification accuracy when determining whether a message is legitimate or potentially malicious. The application is designed with a user-centered, mobile-first interface that allows individuals to paste suspicious emails and receive immediate analysis, clear explanations, and actionable recommendations. This approach ensures that users without technical backgrounds can easily interpret the results and make informed decisions about potential threats.',
    },
    {
        'title': 'PhishGuard: AI-Powered Phishing Detection for Students and Everyday Users',
        'authors': 'Goodluck Badewole, Ibrahim Bello, Gabriel Chambers, Asia Harris, Amber Jamison, Taylor Pippins',
        'faculty_mentors': 'Dr. Ed Pearson',
        'keywords': 'AI, Phishing, Cybersecurity',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'As phishing attacks continue to evolve, students and everyday email users remain frequent targets of scams disguised as job offers, delivery notifications, and account alerts. These attacks often lead to identity theft, financial loss, and compromised personal information. Many existing security tools are designed for enterprise environments and can be overly complex, technical, or overwhelming for individual users. Our project addresses this gap by proposing PhishGuard, an AI-powered phishing detection prototype focused on simplicity, clarity, and user understanding. This solution aligns with the Network Security focus area of AI-Based Phishing Detection, which emphasizes the use of NLP and deep learning to detect phishing emails, websites, and social engineering attempts. PhishGuard is designed to analyze email content and behavioral patterns using artificial intelligence techniques. The system aims to identify suspicious language, impersonation attempts, malicious links, and other forms of social engineering while providing clear explanations for why an email may be risky. By emphasizing explainable alerts and beginner-friendly setup, the prototype seeks to reduce alert fatigue and empower users to make informed decisions about potential threats. This project demonstrates how AI can be leveraged to enhance everyday cybersecurity in an accessible and user-focused way. Future development would include user testing, dataset expansion, and refinement of the detection model to improve accuracy and usability.',
    },
    {
        'title': 'Automated Comparative Evaluation of Large Language Models for Cybersecurity Code Generation',
        'authors': 'Adeyori Adekunle',
        'faculty_mentors': 'Dr. Ed Pearson III',
        'keywords': 'Large Language Models (LLMs), Cybersecurity, Code Generation, Model Evaluation, Python Automation',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Large Language Models (LLMs) are increasingly used for software development, including cybersecurity applications. However, reliability remains a critical concern. This project presents a structured, automated framework for evaluating and comparing three leading LLMs: GPT-4o, Claude-3, and Gemini on their ability to generate executable, functional Python code for real-world cybersecurity tasks. Ten cybersecurity-focused prompts were designed, including AES encryption, RSA key generation, port scan detection, SQL injection testing, XSS payload scanning, log anomaly detection, secure login systems, JWT validation, suspicious file detection, and reverse shell implementation. Each prompt was submitted to all three models through a Python-based evaluation script. The system automatically: • Submits prompts to each LLM via API • Extracts and cleans generated code • Saves outputs as executable Python files • Executes code in a controlled environment • Logs results as Pass or Fail in structured CSV files • Records failure causes (SyntaxError, ModuleNotFoundError, IndentationError, etc.) A "Pass" indicates syntactically correct, executable code. A "Fail" indicates runtime errors, missing dependencies, formatting issues, or non-executable output Results Summary Out of 10 tasks: • Gemini: 6 Pass / 4 Fail • GPT-4o: 4 Pass / 6 Fail • Claude-3: 2 Pass / 8 Fail Common failure causes included: • Syntax errors • Missing Python modules • Improper indentation • File dependency errors The results demonstrate significant variability in model reliability for cybersecurity code generation. Gemini performed best overall in execution reliability, while Claude-3 produced the highest rate of syntax-related failures. Impact This research contributes to data science and applied AI by providing a measurable framework for LLM reliability testing, highlighting execution risks in generative AI for cybersecurity, and introducing a pathway toward automated LLM selection systems.',
    },
    {
        'title': 'Cost transparency and care navigation using an agentic AI system: the CareLens approach',
        'authors': 'Daniel Lambo',
        'faculty_mentors': 'Dr. Ed Pearson III',
        'keywords': 'AI, Healthcare, Transparency, Estimation, Agentic Systems',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Healthcare cost uncertainty is a major barrier to timely medical care in the United States. Many patients delay treatment because they cannot determine the likely cost of care or which healthcare setting is most appropriate. This research presents CareLens, a privacy-first healthcare navigation system designed to improve cost transparency and decision-making before a patient seeks treatment. The platform uses an agentic reasoning architecture that evaluates de-identified symptom descriptions, geographic location, and optional insurance information to recommend appropriate care settings—such as urgent care versus emergency departments—while providing estimated price ranges derived from hospital price-transparency files, CMS datasets, and publicly available insurance coverage data. The system incorporates safety guardrails that prevent diagnostic outputs and focuses exclusively on logistical and financial guidance. CareLens also prioritizes privacy by processing only de-identified inputs and avoiding the storage of protected health information, supporting HIPAA-aware design principles. By presenting understandable cost ranges and nearby care alternatives, the platform aims to reduce delayed treatment, unexpected medical bills, and inefficient healthcare utilization. Importantly, improving access to transparent cost information may disproportionately benefit uninsured and underserved populations who are most affected by healthcare price opacity. Overall, this research explores how AI-assisted healthcare navigation tools can improve patient decision-making and support more equitable access to medical services.',
    },
    {
        'title': 'Semina: AI-Driven Intrusion Detection in SCADA/ICS Environments for Water Utilities',
        'authors': 'Olasubomi Awodipe, Emmanuel Aina, Solomon Agyire, Taiwo Olawepo, Mercy Akinyemi, Moshopefoluwa Omotoso, Vincent Anim-Addo',
        'faculty_mentors': 'Dr. Ed Pearson, Rahmat Herron',
        'keywords': 'Intrusion Detection System, SCADA/ICS Security, Machine Learning, Cybersecurity',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Semina is an AI-powered intrusion detection system (IDS) engineered specifically for the unique constraints of small and public water utilities. Utilizing a machine-learning based anomaly detection engine powered by a Random Forest model, the system achieves a 99.1% AUC by training on 145 operational and security features. A core functionality of Semina is its ability to fuse Operational Technology (OT) data from physical infrastructure, such as pump levels, pressure junctions, and water quality metrics (pH, turbidity, and chlorine), with Information Technology (IT) telemetry, including firewall logs and remote access patterns. This data fusion enables more accurate, context-aware detection of cyber-physical threats, equipment failures, and potential contamination. Designed for reliability in rural or low-connectivity environments, Semina runs locally on dedicated hardware to ensure continuous real-time monitoring. It brings advanced threat detection to utilities that often lack dedicated cybersecurity resources, delivering practical, enterprise level protection tailored to the realities of public water systems.',
    },
    {
        'title': 'Autonomous Multi-Robot Navigation in Constrained 3D Environments via Soft Actor-Critic Reinforcement Learning on Physical QBot Platforms',
        'authors': 'Elton Mawire, Yujian Fu',
        'faculty_mentors': 'Dr. Yujian Fu',
        'keywords': 'Multi-Agent Reinforcement Learning (MARL), Soft Actor-Critic (SAC), Quanser QBot, Collision Avoidance, Real-World Robotics',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'This project presents a reinforcement learning (RL) framework for multi-robot path generation and collision avoidance implemented on physical Quanser QBot platforms. Navigating constrained 3D environments in the real world introduces significant challenges, including sensor noise, asynchronous communication, and the necessity of maintaining physical safety buffers. We address these by formulating the navigation task as a Multi-Agent Markov Decision Process (MMDP), focusing on the deployment of a Soft Actor-Critic (SAC) algorithm to handle continuous action spaces for smooth, precise motion control. Unlike simulation-only studies, our approach prioritizes safe exploration and high sample efficiency to minimize hardware wear while ensuring effective collision avoidance between agents and environmental obstacles. We specifically evaluate the performance of SAC in maintaining a strict 3 cm safety buffer during high-density navigation tasks, comparing its adaptability against Proximal Policy Optimization (PPO) baselines. Experimental results demonstrate that the learned RL policies enable a team of QBots to achieve cooperative, collision-free paths with high success rates and optimized mission completion times. This work highlights the viability of deep reinforcement learning for robust, real-time coordination in physical multi-robot systems.',
    },
    {
        'title': 'AI and Autonomous Vehicle Research',
        'authors': 'Jeeban Bashyal',
        'faculty_mentors': 'Dr. Yujian Fu',
        'keywords': 'AI, Autonomous vehicle, AGI',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Autonomous navigation in multi-platform environments remains a central challenge in robotics, particularly when systems must operate reliably across simulation and real-world conditions. This project focuses on the development of leader-follower navigation algorithms for drones, mobile robots, and autonomous vehicles using Robot Operating System (ROS), Gazebo, and hardware platforms including QDrone, QBot, Arduino, Raspberry Pi, and autonomous car systems. The research integrates artificial intelligence and robotics to enable coordinated motion, adaptive decision-making, object detection, obstacle avoidance, and path planning in dynamic environments. The work emphasizes both simulation-based development and sim-to-real transfer, addressing the common gap between controlled virtual testing and physical deployment. Navigation behaviors were designed and tested in Gazebo before being implemented on hardware to evaluate performance under real-time constraints. Python and C++ were used to program intelligent control pipelines that supported perception, localization, and cooperative movement among aerial, ground, and vehicular agents. Special attention was given to multi-agent coordination, where leader-follower strategies improved group navigation efficiency and system responsiveness. Results demonstrate improved reliability in real-time navigation tasks, with enhanced path planning accuracy, obstacle avoidance capability, and coordination consistency across multiple robotic platforms. By optimizing sim-to-real performance, this research contributes to the advancement of scalable autonomous systems that can be deployed in practical applications such as surveillance, search and rescue, smart transportation, and collaborative robotics. Overall, the project highlights the value of integrating AI-driven control with robotics middleware to build adaptable and robust autonomous platforms.',
    },
    {
        'title': 'Building a Scaled Autonomous Vehicle Using the Quanser QCar2',
        'authors': 'Mercy Akinyemi, Yujian Fu',
        'faculty_mentors': 'Dr. Yujian Fu',
        'keywords': 'Autonomous Vehicles, Computer Vision, LiDAR Sensing, Reinforcement Learning, Autonomous Navigation',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'This project focuses on developing an autonomous vehicle platform using the Quanser QCar2 to simulate real-world driving scenarios in a controlled environment. The QCar2 is equipped with a comprehensive sensor suite including a 384-point LiDAR, CSI cameras, and an Intel RealSense RGB-D sensor, enabling it to perceive its surroundings and navigate a structured driving map. The platform serves as a scaled autonomous driving testbed, allowing real-world evaluation of perception, control, and learning algorithms similar to those used in full-scale self-driving vehicles. Current system capabilities include closed-loop speed control using motor tachometer feedback, LiDAR-based obstacle detection with dual-threshold emergency stopping (1.5 m safety zone and 0.5 m emergency zone), and vision-based lane following. Lane detection is implemented using HSV color space thresholding with region-of-interest cropping for yellow lane detection, followed by contour analysis and moment-based center-of-mass calculation for lane positioning. Vehicle steering and motion are regulated using Proportional Integral (PI) control strategies. This system follows a perception–control architecture where visual and LiDAR sensors provide environmental perception, computer vision algorithms estimate lane position, and control strategies regulate steering and vehicle motion. These behaviors are currently implemented using rule-based methods with obstacle avoidance that analyzes left and right space availability for steering decisions. A key objective of this project is transitioning toward more intelligent navigation through the integration of Deep Learning and Reinforcement Learning. By collecting sensor data and analyzing vehicle responses under different driving conditions, this work aims to develop learning-based navigation strategies that allow the vehicle to adapt to dynamic environments while maintaining safety and reliability.',
    },
    {
        'title': 'CS Advisor',
        'authors': 'Prashant Banjade',
        'faculty_mentors': 'Dr. Yujian Fu',
        'keywords': 'Academic Advising Systems, Course Recommendation System, Degree Progress Tracking, Web-Based Education Platform, Rule-Based Decision System',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'Academic advising plays a crucial role in helping students successfully navigate their degree programs; however, many advisors still rely on manual processes to track academic progress and recommend courses. This project presents the development of the CS Advisor System, a web-based platform designed to assist professors and academic advisors at Alabama A&M University in efficiently monitoring student progress and generating informed course recommendations. Requirement gathering was conducted through discussions with professors who currently advise students manually by referencing the undergraduate bulletin each semester. This process was identified as repetitive and time-consuming, requiring advisors to individually analyze each student’s academic history to determine course eligibility and progression. These findings motivated the development of an automated solution that streamlines the advising workflow. The system was developed using React for the frontend and Node.js with Express for the backend, supported by a PostgreSQL database managed through Prisma ORM. An agile and iterative development approach was used, allowing features to evolve as advising requirements became more clearly defined. At the core of the system is a rule-based recommendation engine that analyzes completed coursework, grades, classification standing, and concentration to determine eligible courses, identify missed requirements from previous semesters, and suggest appropriate courses for upcoming terms. Course eligibility is determined by evaluating prerequisite completion, minimum grade thresholds, and classification requirements. The platform provides advisors with a centralized dashboard to review student academic records, identify unmet degree requirements, and receive tailored course recommendations. By automating a previously manual process, the CS Advisor System reduces administrative workload, minimizes advising errors, and supports more efficient academic planning.',
    },
    {
        'title': 'Artificial Intelligence in Education: A Systematic Review of Methodologies and Their Impact on Learning Outcomes (2015–2025)',
        'authors': 'Toluwani Esan',
        'faculty_mentors': 'Dr. Yujian Fu',
        'keywords': 'Adaptive Learning, Machine Learning, Artificial Intelligence in Education',
        'department': 'Electrical Engineering & Computer Science',
        'abstract': 'This paper examines the evolution of Artificial Intelligence (AI) and its growing role in education between 2015 and 2025. It discusses key AI methodologies, including machine learning and deep learning, and explains how these technologies have enabled systems to analyze large datasets and improve decision-making. The study also explores the application of AI in education through tools such as adaptive learning platforms, intelligent tutoring systems, and predictive analytics, which support personalized learning and improved instructional outcomes. Additionally, the paper highlights challenges associated with AI adoption, including data privacy, bias, and ethical considerations. Overall, the study provides an overview of recent AI developments and their impact on modern educational practices.',
    },
]

STEMDAY_2025_ENTRIES = [
    {
        'title': 'Leveraging Artificial Intelligence for Detecting Zero-Day Attacks',
        'authors': 'Tapiwa Musinga and Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Blue Horizon',
        'authors': 'Brandon Ramadan, Da\'Quandalon Daniel, Yana Dhamija, Riley Roberts, Oluwabukunmi Balogun, and Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Smart Sensei: An AI-Powered Learning Assistant for Quality Education',
        'authors': 'Jackson Cooper, Chasity Harris, Cameron Mahand, and Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Learning for student benefit: AI-based Solutions to maintain quality education.',
        'authors': 'Trenton Moore-lee, Saron Dubale, Makiya Bunch, Taniya Rainge, and Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Plastic Reducers',
        'authors': 'Jordan Fleming, Evette Wherry, Jordan Wren, Tyson Wren, and Raymond Egson, Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Bulldog Supply',
        'authors': 'Zantasia Baldwin, Aniah Cosby, Joseph Johnson, Samya Whiteside',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'Sentinel',
        'authors': 'Jordyn Johnson, Roy Stallworth, Rudaruis Anthony, Terrence Bagget, and Dewayne Maye',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'The Fraudulent Fingerprint: Developing a Dynamic Scam Detection System Through Machine Learning and Network Analysis',
        'authors': 'Daniel Lambo and Ed Pearson',
        'faculty_mentors': 'Ed Pearson',
        'program': 'CS',
    },
    {
        'title': 'AI-Powered Deciphering of Medical Images: A Deep Learning Approach',
        'authors': 'Amarachi J. Ezekiel and Michael Ayokunmi',
        'faculty_mentors': 'Michael Ayokunmi',
        'program': 'CS',
    },
    {
        'title': 'Real-Time Disaster Analysis Using NLP and Social Media',
        'authors': 'Solomon Agyire and Terry Miller',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'AsthmaAssist: A Machine Learning approach to Smart Asthma Management using No2 concentration and Geographical data',
        'authors': 'Mauyon Wusu, Opeyeolowa Olanipekun, and Terry Miller',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'Media Influence on AI Perception: A Sentiment Analysis of News Narratives',
        'authors': 'Thabo Ibrahim Traore',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'Optimizing ACAT siRN Delivery for Targeted Gene Silencing in Neurodegenerative Diseases',
        'authors': 'Jayden Boatwright, Osionela Ogiogwa, and Terry Miller',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'Careers in Your Inbox: Personalized Job Alerts via Automated Web Scraping',
        'authors': 'Asia Harris, John Adeyemo, Terry Miller',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'Energy Consumption - Analyzing and Predicting Usage in Alabama',
        'authors': 'Taniya Rainge, Ruvarashe Nyabando, and Terry Miller',
        'faculty_mentors': 'Terry Miller',
        'program': 'CS',
    },
    {
        'title': 'SMART CMS',
        'authors': 'Dipin Dawadi and Yujian Fu',
        'faculty_mentors': 'Yujian Fu',
        'program': 'CS',
    },
    {
        'title': 'The Smart Learning System',
        'authors': 'Zizwe Mtonga, Olayiwola Ajibode, and Yujian Fu',
        'faculty_mentors': 'Yujian Fu',
        'program': 'CS',
    },
    {
        'title': 'Embedded Systems and Robotics: From Microcontrollers to Intelligent Machines',
        'authors': 'Mercy Akinyemi and Yujian Fu',
        'faculty_mentors': 'Yujian Fu',
        'program': 'CS',
    },
    {
        'title': 'Enhancing Autonomous Navigation in Zumi Robot thruogh Machine Vision and Infrared Sensing',
        'authors': 'Emily Omezi and Yujian Fu',
        'faculty_mentors': 'Yujian Fu',
        'program': 'CS',
    },
    {
        'title': 'Enhancing Object Detection and Motion Planning in the XGO Mini Quadruped Robot',
        'authors': 'Jada Haley and Yujian Fu',
        'faculty_mentors': 'Yujian Fu',
        'program': 'CS',
    },
]


def _read_shared_strings(archive):
    strings = []
    if 'xl/sharedStrings.xml' not in archive.namelist():
        return strings
    root = ET.fromstring(archive.read('xl/sharedStrings.xml'))
    for si in root.findall('.//a:si', XML_NS):
        segments = [t.text or '' for t in si.findall('.//a:t', XML_NS)]
        strings.append(''.join(segments))
    return strings


def _normalize_header(name):
    if not name:
        return ''
    normalized = name.strip().lower()
    mapping = {
        'abstract#': 'abstract_number',
        'ref': 'ref',
        'authors': 'authors',
        'author(s)': 'authors',
        'faculty mentors': 'faculty_mentors',
        'faculty mentor(s)': 'faculty_mentors',
        'program': 'program',
        'title': 'title',
        'keywords': 'keywords',
        'department': 'department',
        'abstract': 'abstract',
        'memo': 'memo',
    }
    normalized = normalized.replace('(', '').replace(')', '').replace('/', ' ').replace('#', 'number')
    return mapping.get(normalized, normalized.replace(' ', '_'))


def _parse_spreadsheet(path):
    if not path.exists():
        return []

    with zipfile.ZipFile(path) as archive:
        shared = _read_shared_strings(archive)
        raw = archive.read('xl/worksheets/sheet1.xml')

    sheet = ET.fromstring(raw)
    rows = []
    for row in sheet.findall('.//a:row', XML_NS):
        cells = {}
        for cell in row.findall('a:c', XML_NS):
            ref = cell.get('r') or ''
            col = ''.join([ch for ch in ref if ch.isalpha()])
            cell_type = cell.get('t')
            v = cell.find('a:v', XML_NS)
            if v is None:
                value = ''
            elif cell_type == 's':
                value = shared[int(v.text)]
            else:
                value = v.text or ''
            cells[col] = value
        rows.append(cells)

    header_row = None
    parsed = []
    for cells in rows:
        if header_row is None:
            headers = {col: _normalize_header(value) for col, value in cells.items() if value}
            if {'authors', 'title'} & set(headers.values()):
                header_row = headers
                continue
            continue

        row_data = {normalized: cells.get(col, '') for col, normalized in header_row.items()}
        row_title = str(row_data.get('title', '')).strip()
        row_authors = str(row_data.get('authors', '')).strip()
        if not row_title or not row_authors:
            continue
        parsed.append(row_data)
    return parsed


def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')

def researchprojects(request):
    return render(request, 'researchprojects.html')

def project1(request):
    return render(request, 'researchprojects/project1.html')

def project2(request):
    return render(request, 'researchprojects/project2.html')

def project3(request):
    return render(request, 'researchprojects/project3.html')

def project4(request):
    return render(request, 'researchprojects/project4.html')

def stemday(request):
    return render(request, 'stemday.html', {
        'stemday_2025': STEMDAY_2025_ENTRIES,
        'stemday_2026': STEMDAY_2026_ENTRIES,
    })

def publications(request):
    return render(request, 'publications.html')

def courses(request):
    return render(request, 'courses.html')

def software(request):
    return render(request, 'software.html')

def bio(request):
    return render(request, 'bio.html')
