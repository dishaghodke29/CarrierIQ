"""
Learning Resources Database for CarrierIQ.
Curated courses, videos, docs, and learning metadata for each skill.
"""

# ── Skill Resources Database ───────────────────────────────────────────────
# Each skill maps to: courses, videos, docs, time estimate, difficulty

SKILL_RESOURCES = {
    # ── Programming Languages ──────────────────────────────────────────────
    "python": {
        "courses": [
            {"title": "Python for Everybody (Coursera)", "url": "https://www.coursera.org/specializations/python", "free": True},
            {"title": "100 Days of Code - Python (Udemy)", "url": "https://www.udemy.com/course/100-days-of-code/", "free": False},
        ],
        "videos": [
            {"title": "Python Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
            {"title": "Python Tutorial - Mosh", "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"},
        ],
        "docs": [{"title": "Official Python Docs", "url": "https://docs.python.org/3/tutorial/"}],
        "time": "4-6 weeks", "difficulty": "beginner",
    },
    "java": {
        "courses": [
            {"title": "Java Programming (Coursera - Duke)", "url": "https://www.coursera.org/specializations/java-programming", "free": True},
            {"title": "Java Masterclass (Udemy)", "url": "https://www.udemy.com/course/java-the-complete-java-developer-course/", "free": False},
        ],
        "videos": [
            {"title": "Java Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=grEKMHGYyns"},
            {"title": "Java Tutorial - Bro Code", "url": "https://www.youtube.com/watch?v=xk4_1vDrzzo"},
        ],
        "docs": [{"title": "Oracle Java Docs", "url": "https://docs.oracle.com/javase/tutorial/"}],
        "time": "6-8 weeks", "difficulty": "beginner",
    },
    "javascript": {
        "courses": [
            {"title": "JavaScript Algorithms (freeCodeCamp)", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "free": True},
            {"title": "The Complete JavaScript Course (Udemy)", "url": "https://www.udemy.com/course/the-complete-javascript-course/", "free": False},
        ],
        "videos": [
            {"title": "JavaScript Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
            {"title": "JavaScript in 1 Hour - Mosh", "url": "https://www.youtube.com/watch?v=W6NZfCO5SIk"},
        ],
        "docs": [{"title": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"}],
        "time": "4-6 weeks", "difficulty": "beginner",
    },
    "typescript": {
        "courses": [
            {"title": "Understanding TypeScript (Udemy)", "url": "https://www.udemy.com/course/understanding-typescript/", "free": False},
        ],
        "videos": [
            {"title": "TypeScript Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=30LWjhZzg50"},
            {"title": "TypeScript Tutorial - Net Ninja", "url": "https://www.youtube.com/watch?v=2pZmKW9-I_k&list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI"},
        ],
        "docs": [{"title": "TypeScript Handbook", "url": "https://www.typescriptlang.org/docs/handbook/"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },
    "c++": {
        "courses": [
            {"title": "C++ For C Programmers (Coursera)", "url": "https://www.coursera.org/learn/c-plus-plus-a", "free": True},
        ],
        "videos": [
            {"title": "C++ Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y"},
        ],
        "docs": [{"title": "C++ Reference", "url": "https://en.cppreference.com/w/"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },
    "r": {
        "courses": [
            {"title": "R Programming (Coursera - Johns Hopkins)", "url": "https://www.coursera.org/learn/r-programming", "free": True},
        ],
        "videos": [
            {"title": "R Programming Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=_V8eKsto3Ug"},
        ],
        "docs": [{"title": "R Documentation", "url": "https://www.r-project.org/other-docs.html"}],
        "time": "3-4 weeks", "difficulty": "beginner",
    },
    "swift": {
        "courses": [
            {"title": "iOS & Swift - The Complete iOS App Development Bootcamp", "url": "https://www.udemy.com/course/ios-13-app-development-bootcamp/", "free": False},
        ],
        "videos": [
            {"title": "Swift Programming Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=comQ1-x2a1Q"},
        ],
        "docs": [{"title": "Swift Documentation", "url": "https://www.swift.org/documentation/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "kotlin": {
        "courses": [
            {"title": "Kotlin for Java Developers (Coursera)", "url": "https://www.coursera.org/learn/kotlin-for-java-developers", "free": True},
        ],
        "videos": [
            {"title": "Kotlin Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=F9UC9DY-vIU"},
        ],
        "docs": [{"title": "Kotlin Official Docs", "url": "https://kotlinlang.org/docs/home.html"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },

    # ── Web Development ────────────────────────────────────────────────────
    "html": {
        "courses": [
            {"title": "Responsive Web Design (freeCodeCamp)", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "free": True},
        ],
        "videos": [
            {"title": "HTML Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=pQN-pnXPaVg"},
        ],
        "docs": [{"title": "MDN HTML Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML"}],
        "time": "1-2 weeks", "difficulty": "beginner",
    },
    "css": {
        "courses": [
            {"title": "Responsive Web Design (freeCodeCamp)", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "free": True},
        ],
        "videos": [
            {"title": "CSS Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=1Rs2ND1ryYc"},
            {"title": "CSS Flexbox & Grid - Traversy Media", "url": "https://www.youtube.com/watch?v=3YW65K6LcIA"},
        ],
        "docs": [{"title": "MDN CSS Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "react": {
        "courses": [
            {"title": "React - The Complete Guide (Udemy)", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "free": False},
        ],
        "videos": [
            {"title": "React Full Course 2024 - freeCodeCamp", "url": "https://www.youtube.com/watch?v=CgkZ7MvWUAA"},
            {"title": "React in 1 Hour - Mosh", "url": "https://www.youtube.com/watch?v=SqcY0GlETPk"},
        ],
        "docs": [{"title": "React Official Docs", "url": "https://react.dev/learn"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "node.js": {
        "courses": [
            {"title": "The Complete Node.js Developer Course (Udemy)", "url": "https://www.udemy.com/course/the-complete-nodejs-developer-course-2/", "free": False},
        ],
        "videos": [
            {"title": "Node.js Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=Oe421EPjeBE"},
        ],
        "docs": [{"title": "Node.js Official Docs", "url": "https://nodejs.org/en/docs/guides"}],
        "time": "3-5 weeks", "difficulty": "intermediate",
    },
    "next.js": {
        "courses": [
            {"title": "Next.js 14 & React (Udemy)", "url": "https://www.udemy.com/course/nextjs-react-the-complete-guide/", "free": False},
        ],
        "videos": [
            {"title": "Next.js Full Course - JavaScript Mastery", "url": "https://www.youtube.com/watch?v=wm5gMKuwSYk"},
        ],
        "docs": [{"title": "Next.js Official Docs", "url": "https://nextjs.org/docs"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "vue.js": {
        "courses": [
            {"title": "Vue.js 3 Complete Guide (Udemy)", "url": "https://www.udemy.com/course/vuejs-2-the-complete-guide/", "free": False},
        ],
        "videos": [
            {"title": "Vue.js Course for Beginners - freeCodeCamp", "url": "https://www.youtube.com/watch?v=FXpIoQ_rT_c"},
        ],
        "docs": [{"title": "Vue.js Official Docs", "url": "https://vuejs.org/guide/introduction.html"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "angular": {
        "courses": [
            {"title": "Angular Complete Guide (Udemy)", "url": "https://www.udemy.com/course/the-complete-guide-to-angular-2/", "free": False},
        ],
        "videos": [
            {"title": "Angular Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=3qBXWUpoPHo"},
        ],
        "docs": [{"title": "Angular Official Docs", "url": "https://angular.io/docs"}],
        "time": "5-7 weeks", "difficulty": "intermediate",
    },
    "responsive design": {
        "courses": [
            {"title": "Responsive Web Design (freeCodeCamp)", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/", "free": True},
        ],
        "videos": [
            {"title": "Responsive Web Design - freeCodeCamp", "url": "https://www.youtube.com/watch?v=srvUrASNj0s"},
        ],
        "docs": [{"title": "MDN Responsive Design", "url": "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"}],
        "time": "1-2 weeks", "difficulty": "beginner",
    },
    "rest api": {
        "courses": [
            {"title": "APIs and RESTful Services (Udemy)", "url": "https://www.udemy.com/course/rest-api/", "free": False},
        ],
        "videos": [
            {"title": "REST API Crash Course - Traversy Media", "url": "https://www.youtube.com/watch?v=Q-BpqyOT3a8"},
        ],
        "docs": [{"title": "RESTful API Design Guide", "url": "https://restfulapi.net/"}],
        "time": "1-2 weeks", "difficulty": "intermediate",
    },
    "graphql": {
        "courses": [
            {"title": "GraphQL by Example (Udemy)", "url": "https://www.udemy.com/course/graphql-by-example/", "free": False},
        ],
        "videos": [
            {"title": "GraphQL Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=ed8SzALpx1Q"},
        ],
        "docs": [{"title": "GraphQL Official Docs", "url": "https://graphql.org/learn/"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },

    # ── Data Science & ML ──────────────────────────────────────────────────
    "machine learning": {
        "courses": [
            {"title": "Machine Learning Specialization (Coursera - Andrew Ng)", "url": "https://www.coursera.org/specializations/machine-learning-introduction", "free": True},
            {"title": "ML A-Z: AI, Python & R (Udemy)", "url": "https://www.udemy.com/course/machinelearning/", "free": False},
        ],
        "videos": [
            {"title": "Machine Learning Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=NWONeJKn6kc"},
            {"title": "ML Full Course - Simplilearn", "url": "https://www.youtube.com/watch?v=GwIo3gDZCVQ"},
        ],
        "docs": [{"title": "Google ML Crash Course", "url": "https://developers.google.com/machine-learning/crash-course"}],
        "time": "8-12 weeks", "difficulty": "intermediate",
    },
    "deep learning": {
        "courses": [
            {"title": "Deep Learning Specialization (Coursera - Andrew Ng)", "url": "https://www.coursera.org/specializations/deep-learning", "free": True},
        ],
        "videos": [
            {"title": "Deep Learning Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=VyWAvY2CF9c"},
        ],
        "docs": [{"title": "Deep Learning Book (Goodfellow)", "url": "https://www.deeplearningbook.org/"}],
        "time": "10-14 weeks", "difficulty": "advanced",
    },
    "statistics": {
        "courses": [
            {"title": "Statistics with Python (Coursera - Michigan)", "url": "https://www.coursera.org/specializations/statistics-with-python", "free": True},
        ],
        "videos": [
            {"title": "Statistics Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=xxpc-HPKN28"},
        ],
        "docs": [{"title": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "data analysis": {
        "courses": [
            {"title": "Google Data Analytics Certificate (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-data-analytics", "free": True},
        ],
        "videos": [
            {"title": "Data Analysis with Python - freeCodeCamp", "url": "https://www.youtube.com/watch?v=r-uOLxNrNk8"},
        ],
        "docs": [{"title": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}],
        "time": "4-6 weeks", "difficulty": "beginner",
    },
    "data visualization": {
        "courses": [
            {"title": "Data Visualization with Python (Coursera)", "url": "https://www.coursera.org/learn/python-for-data-visualization", "free": True},
        ],
        "videos": [
            {"title": "Matplotlib Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=3Xc3CA655Y4"},
        ],
        "docs": [{"title": "Matplotlib Documentation", "url": "https://matplotlib.org/stable/tutorials/index.html"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "pandas": {
        "courses": [
            {"title": "Data Analysis with Pandas (Kaggle)", "url": "https://www.kaggle.com/learn/pandas", "free": True},
        ],
        "videos": [
            {"title": "Pandas Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=vmEHCJofslg"},
        ],
        "docs": [{"title": "Pandas Official Docs", "url": "https://pandas.pydata.org/docs/getting_started/"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "numpy": {
        "courses": [
            {"title": "NumPy (Kaggle)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "free": True},
        ],
        "videos": [
            {"title": "NumPy Full Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=QUT1VHiLmmI"},
        ],
        "docs": [{"title": "NumPy Official Docs", "url": "https://numpy.org/doc/stable/user/absolute_beginners.html"}],
        "time": "1-2 weeks", "difficulty": "beginner",
    },
    "scikit-learn": {
        "courses": [
            {"title": "Intro to Machine Learning (Kaggle)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning", "free": True},
        ],
        "videos": [
            {"title": "Scikit-learn Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=pqNCD_5r0IU"},
        ],
        "docs": [{"title": "Scikit-learn Official Docs", "url": "https://scikit-learn.org/stable/getting_started.html"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "tensorflow": {
        "courses": [
            {"title": "DeepLearning.AI TensorFlow Developer (Coursera)", "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice", "free": True},
        ],
        "videos": [
            {"title": "TensorFlow 2.0 Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=tPYj3fFJGjk"},
        ],
        "docs": [{"title": "TensorFlow Official Tutorials", "url": "https://www.tensorflow.org/tutorials"}],
        "time": "5-7 weeks", "difficulty": "advanced",
    },
    "pytorch": {
        "courses": [
            {"title": "PyTorch for Deep Learning (freeCodeCamp)", "url": "https://www.freecodecamp.org/news/pytorch-full-course/", "free": True},
        ],
        "videos": [
            {"title": "PyTorch Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=V_xro1bcAuU"},
        ],
        "docs": [{"title": "PyTorch Official Tutorials", "url": "https://pytorch.org/tutorials/"}],
        "time": "5-7 weeks", "difficulty": "advanced",
    },
    "nlp": {
        "courses": [
            {"title": "NLP Specialization (Coursera - deeplearning.ai)", "url": "https://www.coursera.org/specializations/natural-language-processing", "free": True},
        ],
        "videos": [
            {"title": "NLP with Python - freeCodeCamp", "url": "https://www.youtube.com/watch?v=fOvTtapxa9c"},
        ],
        "docs": [{"title": "Hugging Face NLP Course", "url": "https://huggingface.co/learn/nlp-course"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
    "computer vision": {
        "courses": [
            {"title": "Computer Vision (Coursera)", "url": "https://www.coursera.org/learn/computer-vision-basics", "free": True},
        ],
        "videos": [
            {"title": "OpenCV Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=oXlwWbU8l2o"},
        ],
        "docs": [{"title": "OpenCV Documentation", "url": "https://docs.opencv.org/4.x/d9/df8/tutorial_root.html"}],
        "time": "5-7 weeks", "difficulty": "advanced",
    },
    "mathematics": {
        "courses": [
            {"title": "Mathematics for Machine Learning (Coursera)", "url": "https://www.coursera.org/specializations/mathematics-machine-learning", "free": True},
        ],
        "videos": [
            {"title": "Math for ML - freeCodeCamp", "url": "https://www.youtube.com/watch?v=1VSZtNYMntM"},
        ],
        "docs": [{"title": "Khan Academy Math", "url": "https://www.khanacademy.org/math"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },

    # ── Databases & SQL ────────────────────────────────────────────────────
    "sql": {
        "courses": [
            {"title": "SQL for Data Science (Coursera)", "url": "https://www.coursera.org/learn/sql-for-data-science", "free": True},
        ],
        "videos": [
            {"title": "SQL Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
            {"title": "SQL Tutorial - Mosh", "url": "https://www.youtube.com/watch?v=7S_tz1z_5bA"},
        ],
        "docs": [{"title": "W3Schools SQL", "url": "https://www.w3schools.com/sql/"}],
        "time": "2-4 weeks", "difficulty": "beginner",
    },
    "mongodb": {
        "courses": [
            {"title": "MongoDB University (Free)", "url": "https://university.mongodb.com/", "free": True},
        ],
        "videos": [
            {"title": "MongoDB Crash Course - Traversy Media", "url": "https://www.youtube.com/watch?v=-56x56UppqQ"},
        ],
        "docs": [{"title": "MongoDB Official Docs", "url": "https://www.mongodb.com/docs/manual/tutorial/getting-started/"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "postgresql": {
        "courses": [
            {"title": "PostgreSQL Bootcamp (Udemy)", "url": "https://www.udemy.com/course/the-complete-python-postgresql-developer-course/", "free": False},
        ],
        "videos": [
            {"title": "PostgreSQL Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=qw--VYLpxG4"},
        ],
        "docs": [{"title": "PostgreSQL Official Docs", "url": "https://www.postgresql.org/docs/current/tutorial.html"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },
    "redis": {
        "courses": [
            {"title": "Redis University (Free)", "url": "https://university.redis.com/", "free": True},
        ],
        "videos": [
            {"title": "Redis Crash Course - Traversy Media", "url": "https://www.youtube.com/watch?v=jgpVdJB2sKQ"},
        ],
        "docs": [{"title": "Redis Official Docs", "url": "https://redis.io/docs/"}],
        "time": "1-2 weeks", "difficulty": "intermediate",
    },
    "databases": {
        "courses": [
            {"title": "Databases for Developers (Oracle)", "url": "https://education.oracle.com/", "free": True},
        ],
        "videos": [
            {"title": "Database Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=ztHopE5Wnpc"},
        ],
        "docs": [{"title": "Database Design Guide", "url": "https://www.vertabelo.com/blog/database-design/"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },

    # ── DevOps & Cloud ─────────────────────────────────────────────────────
    "docker": {
        "courses": [
            {"title": "Docker Mastery (Udemy)", "url": "https://www.udemy.com/course/docker-mastery/", "free": False},
        ],
        "videos": [
            {"title": "Docker Full Course - TechWorld with Nana", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE"},
            {"title": "Docker Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo"},
        ],
        "docs": [{"title": "Docker Official Docs", "url": "https://docs.docker.com/get-started/"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },
    "kubernetes": {
        "courses": [
            {"title": "Kubernetes for Beginners (KodeKloud)", "url": "https://www.udemy.com/course/learn-kubernetes/", "free": False},
        ],
        "videos": [
            {"title": "Kubernetes Course - TechWorld with Nana", "url": "https://www.youtube.com/watch?v=X48VuDVv0do"},
        ],
        "docs": [{"title": "Kubernetes Official Docs", "url": "https://kubernetes.io/docs/tutorials/"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },
    "aws": {
        "courses": [
            {"title": "AWS Cloud Practitioner (Coursera)", "url": "https://www.coursera.org/learn/aws-cloud-practitioner-essentials", "free": True},
        ],
        "videos": [
            {"title": "AWS Certified Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=3hLmDS179YE"},
        ],
        "docs": [{"title": "AWS Documentation", "url": "https://docs.aws.amazon.com/"}],
        "time": "4-8 weeks", "difficulty": "intermediate",
    },
    "linux": {
        "courses": [
            {"title": "Linux Fundamentals (edX)", "url": "https://www.edx.org/learn/linux/the-linux-foundation-introduction-to-linux", "free": True},
        ],
        "videos": [
            {"title": "Linux Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=sWbUDq4S6Y8"},
        ],
        "docs": [{"title": "Linux Journey", "url": "https://linuxjourney.com/"}],
        "time": "3-4 weeks", "difficulty": "beginner",
    },
    "ci/cd": {
        "courses": [
            {"title": "CI/CD with Jenkins (Udemy)", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero/", "free": False},
        ],
        "videos": [
            {"title": "CI/CD Full Course - TechWorld with Nana", "url": "https://www.youtube.com/watch?v=7Mh4LHJrONE"},
        ],
        "docs": [{"title": "GitHub Actions Docs", "url": "https://docs.github.com/en/actions"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },
    "terraform": {
        "courses": [
            {"title": "HashiCorp Terraform Associate (Udemy)", "url": "https://www.udemy.com/course/terraform-beginner-to-advanced/", "free": False},
        ],
        "videos": [
            {"title": "Terraform Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=SLB_c_ayRMo"},
        ],
        "docs": [{"title": "Terraform Official Docs", "url": "https://developer.hashicorp.com/terraform/tutorials"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "git": {
        "courses": [
            {"title": "Version Control with Git (Coursera)", "url": "https://www.coursera.org/learn/version-control-with-git", "free": True},
        ],
        "videos": [
            {"title": "Git & GitHub Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},
        ],
        "docs": [{"title": "Git Official Docs", "url": "https://git-scm.com/doc"}],
        "time": "1-2 weeks", "difficulty": "beginner",
    },

    # ── CS Fundamentals ────────────────────────────────────────────────────
    "data structures": {
        "courses": [
            {"title": "Data Structures & Algorithms (Coursera - UC San Diego)", "url": "https://www.coursera.org/specializations/data-structures-algorithms", "free": True},
        ],
        "videos": [
            {"title": "DSA Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=8hly31xKli0"},
            {"title": "Striver's DSA Playlist", "url": "https://www.youtube.com/watch?v=0bHoB32fuj0&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz"},
        ],
        "docs": [{"title": "GeeksforGeeks DSA", "url": "https://www.geeksforgeeks.org/data-structures/"}],
        "time": "6-10 weeks", "difficulty": "intermediate",
    },
    "algorithms": {
        "courses": [
            {"title": "Algorithms Specialization (Coursera - Stanford)", "url": "https://www.coursera.org/specializations/algorithms", "free": True},
        ],
        "videos": [
            {"title": "Algorithms Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=8hly31xKli0"},
        ],
        "docs": [{"title": "GeeksforGeeks Algorithms", "url": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"}],
        "time": "6-10 weeks", "difficulty": "intermediate",
    },
    "oop": {
        "courses": [
            {"title": "Object Oriented Programming (Coursera)", "url": "https://www.coursera.org/learn/object-oriented-java", "free": True},
        ],
        "videos": [
            {"title": "OOP in Python - freeCodeCamp", "url": "https://www.youtube.com/watch?v=Ej_02ICOIgs"},
        ],
        "docs": [{"title": "OOP Concepts Guide", "url": "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "system design": {
        "courses": [
            {"title": "Grokking System Design (Educative)", "url": "https://www.educative.io/courses/grokking-modern-system-design-interview-for-engineers-managers", "free": False},
        ],
        "videos": [
            {"title": "System Design - Gaurav Sen Playlist", "url": "https://www.youtube.com/watch?v=xpDnVSmNFX0&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX"},
        ],
        "docs": [{"title": "System Design Primer (GitHub)", "url": "https://github.com/donnemartin/system-design-primer"}],
        "time": "6-10 weeks", "difficulty": "advanced",
    },
    "testing": {
        "courses": [
            {"title": "Software Testing (Coursera)", "url": "https://www.coursera.org/learn/introduction-software-testing", "free": True},
        ],
        "videos": [
            {"title": "Software Testing Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=u6QfIXgjwGQ"},
        ],
        "docs": [{"title": "Pytest Documentation", "url": "https://docs.pytest.org/en/latest/"}],
        "time": "2-3 weeks", "difficulty": "intermediate",
    },
    "design patterns": {
        "courses": [
            {"title": "Design Patterns in Python (Udemy)", "url": "https://www.udemy.com/course/design-patterns-python/", "free": False},
        ],
        "videos": [
            {"title": "Design Patterns - freeCodeCamp", "url": "https://www.youtube.com/watch?v=tv-_1er1mWI"},
        ],
        "docs": [{"title": "Refactoring Guru - Patterns", "url": "https://refactoring.guru/design-patterns"}],
        "time": "3-4 weeks", "difficulty": "advanced",
    },
    "microservices": {
        "courses": [
            {"title": "Microservices Architecture (Udemy)", "url": "https://www.udemy.com/course/microservices-architecture/", "free": False},
        ],
        "videos": [
            {"title": "Microservices Explained - TechWorld with Nana", "url": "https://www.youtube.com/watch?v=rv4LlmLmVWk"},
        ],
        "docs": [{"title": "Microservices.io", "url": "https://microservices.io/"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },

    # ── Data Engineering & Tools ───────────────────────────────────────────
    "spark": {
        "courses": [
            {"title": "Apache Spark with Python (Udemy)", "url": "https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/", "free": False},
        ],
        "videos": [
            {"title": "PySpark Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=_C8kWso4ne4"},
        ],
        "docs": [{"title": "Spark Official Docs", "url": "https://spark.apache.org/docs/latest/"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },
    "etl": {
        "courses": [
            {"title": "ETL with Python (DataCamp)", "url": "https://www.datacamp.com/courses/etl-in-python", "free": False},
        ],
        "videos": [
            {"title": "ETL Explained - IBM Technology", "url": "https://www.youtube.com/watch?v=OW5OgsLpDCQ"},
        ],
        "docs": [{"title": "Airflow ETL Tutorial", "url": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "data warehousing": {
        "courses": [
            {"title": "Data Warehousing (Coursera)", "url": "https://www.coursera.org/learn/data-warehousing", "free": True},
        ],
        "videos": [
            {"title": "Data Warehouse Concepts", "url": "https://www.youtube.com/watch?v=AHR_7jFCMeY"},
        ],
        "docs": [{"title": "Snowflake Documentation", "url": "https://docs.snowflake.com/en/"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "excel": {
        "courses": [
            {"title": "Excel Skills for Business (Coursera)", "url": "https://www.coursera.org/specializations/excel", "free": True},
        ],
        "videos": [
            {"title": "Excel Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg"},
        ],
        "docs": [{"title": "Microsoft Excel Support", "url": "https://support.microsoft.com/en-us/excel"}],
        "time": "2-3 weeks", "difficulty": "beginner",
    },
    "tableau": {
        "courses": [
            {"title": "Data Visualization with Tableau (Coursera)", "url": "https://www.coursera.org/specializations/data-visualization", "free": True},
        ],
        "videos": [
            {"title": "Tableau Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=aHaOIvR00So"},
        ],
        "docs": [{"title": "Tableau Learning", "url": "https://www.tableau.com/learn/training"}],
        "time": "3-4 weeks", "difficulty": "beginner",
    },
    "power bi": {
        "courses": [
            {"title": "Microsoft Power BI (Coursera)", "url": "https://www.coursera.org/learn/microsoft-power-bi", "free": True},
        ],
        "videos": [
            {"title": "Power BI Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=3u7MQz1EyPY"},
        ],
        "docs": [{"title": "Power BI Documentation", "url": "https://learn.microsoft.com/en-us/power-bi/"}],
        "time": "3-4 weeks", "difficulty": "beginner",
    },

    # ── Mobile Development ─────────────────────────────────────────────────
    "react native": {
        "courses": [
            {"title": "React Native - Practical Guide (Udemy)", "url": "https://www.udemy.com/course/react-native-the-practical-guide/", "free": False},
        ],
        "videos": [
            {"title": "React Native Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=obH0Po_RdWk"},
        ],
        "docs": [{"title": "React Native Official Docs", "url": "https://reactnative.dev/docs/getting-started"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "flutter": {
        "courses": [
            {"title": "Flutter & Dart Complete Guide (Udemy)", "url": "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/", "free": False},
        ],
        "videos": [
            {"title": "Flutter Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=VPvVD8t02U8"},
        ],
        "docs": [{"title": "Flutter Official Docs", "url": "https://docs.flutter.dev/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "android sdk": {
        "courses": [
            {"title": "Android Basics (Google)", "url": "https://developer.android.com/courses", "free": True},
        ],
        "videos": [
            {"title": "Android Development Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=fis26HvvDII"},
        ],
        "docs": [{"title": "Android Developer Docs", "url": "https://developer.android.com/docs"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },

    # ── Security ───────────────────────────────────────────────────────────
    "network security": {
        "courses": [
            {"title": "Network Security (Coursera)", "url": "https://www.coursera.org/learn/network-security", "free": True},
        ],
        "videos": [
            {"title": "Network Security Full Course - Simplilearn", "url": "https://www.youtube.com/watch?v=qiQR5rTSshw"},
        ],
        "docs": [{"title": "OWASP Security Guide", "url": "https://owasp.org/www-project-web-security-testing-guide/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "penetration testing": {
        "courses": [
            {"title": "Penetration Testing (Coursera)", "url": "https://www.coursera.org/learn/ibm-penetration-testing-incident-response-forensics", "free": True},
        ],
        "videos": [
            {"title": "Ethical Hacking - freeCodeCamp", "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE"},
        ],
        "docs": [{"title": "HackTheBox Academy", "url": "https://academy.hackthebox.com/"}],
        "time": "6-10 weeks", "difficulty": "advanced",
    },

    # ── Design & Product ───────────────────────────────────────────────────
    "figma": {
        "courses": [
            {"title": "Google UX Design Certificate (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-ux-design", "free": True},
        ],
        "videos": [
            {"title": "Figma UI Design Tutorial - freeCodeCamp", "url": "https://www.youtube.com/watch?v=jwCmIBJ8Jtc"},
        ],
        "docs": [{"title": "Figma Help Center", "url": "https://help.figma.com/"}],
        "time": "2-4 weeks", "difficulty": "beginner",
    },
    "user research": {
        "courses": [
            {"title": "UX Research (Coursera - Google)", "url": "https://www.coursera.org/learn/foundations-user-experience-design", "free": True},
        ],
        "videos": [
            {"title": "UX Research Methods", "url": "https://www.youtube.com/watch?v=0mNPWmSzyos"},
        ],
        "docs": [{"title": "Nielsen Norman Group", "url": "https://www.nngroup.com/articles/"}],
        "time": "3-4 weeks", "difficulty": "beginner",
    },
    "agile": {
        "courses": [
            {"title": "Agile with Atlassian Jira (Coursera)", "url": "https://www.coursera.org/learn/agile-atlassian-jira", "free": True},
        ],
        "videos": [
            {"title": "Agile Methodology - Simplilearn", "url": "https://www.youtube.com/watch?v=Z9QbYZh1YXY"},
        ],
        "docs": [{"title": "Atlassian Agile Coach", "url": "https://www.atlassian.com/agile"}],
        "time": "1-2 weeks", "difficulty": "beginner",
    },

    # ── AI / LLM ───────────────────────────────────────────────────────────
    "transformers": {
        "courses": [
            {"title": "Hugging Face NLP Course", "url": "https://huggingface.co/learn/nlp-course", "free": True},
        ],
        "videos": [
            {"title": "Transformers Explained - CodeEmporium", "url": "https://www.youtube.com/watch?v=4Bdc55j80l8"},
        ],
        "docs": [{"title": "Hugging Face Docs", "url": "https://huggingface.co/docs/transformers/"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },
    "langchain": {
        "courses": [
            {"title": "LangChain for LLM Application (Udemy)", "url": "https://www.udemy.com/course/langchain/", "free": False},
        ],
        "videos": [
            {"title": "LangChain Crash Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=lG7Uxts9SXs"},
        ],
        "docs": [{"title": "LangChain Official Docs", "url": "https://python.langchain.com/docs/get_started/introduction"}],
        "time": "3-4 weeks", "difficulty": "advanced",
    },
    "mlops": {
        "courses": [
            {"title": "MLOps Specialization (Coursera - DeepLearning.AI)", "url": "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops", "free": True},
        ],
        "videos": [
            {"title": "MLOps Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=Vf2cLdHz4II"},
        ],
        "docs": [{"title": "MLflow Documentation", "url": "https://mlflow.org/docs/latest/index.html"}],
        "time": "5-7 weeks", "difficulty": "advanced",
    },

    # ── Mechanical Engineering ─────────────────────────────────────────────
    "solidworks": {
        "courses": [
            {"title": "SolidWorks Complete Course (Udemy)", "url": "https://www.udemy.com/course/solidworks-from-beginner-to-professional/", "free": False},
        ],
        "videos": [
            {"title": "SolidWorks Full Tutorial - CAD CAM Tutorial", "url": "https://www.youtube.com/watch?v=ixPMD8BjjQY"},
        ],
        "docs": [{"title": "SolidWorks Help", "url": "https://help.solidworks.com/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "autocad": {
        "courses": [
            {"title": "AutoCAD Complete Course (Udemy)", "url": "https://www.udemy.com/course/autocad-2d-and-3d-practice-drawings/", "free": False},
        ],
        "videos": [
            {"title": "AutoCAD Full Course for Beginners", "url": "https://www.youtube.com/watch?v=VtLXKU1PorQ"},
        ],
        "docs": [{"title": "AutoCAD Documentation", "url": "https://help.autodesk.com/view/ACD/2025/ENU/"}],
        "time": "3-5 weeks", "difficulty": "beginner",
    },
    "ansys": {
        "courses": [
            {"title": "ANSYS Workbench Course (Udemy)", "url": "https://www.udemy.com/course/ansys-workbench/", "free": False},
        ],
        "videos": [
            {"title": "ANSYS Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=MKHGhqo53Ek"},
        ],
        "docs": [{"title": "ANSYS Learning Hub", "url": "https://www.ansys.com/academic/learning-resources"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "matlab": {
        "courses": [
            {"title": "MATLAB Onramp (MathWorks - Free)", "url": "https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted", "free": True},
            {"title": "MATLAB for Engineers (Coursera)", "url": "https://www.coursera.org/learn/matlab", "free": True},
        ],
        "videos": [
            {"title": "MATLAB Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=7f50sQYjNRA"},
        ],
        "docs": [{"title": "MATLAB Documentation", "url": "https://www.mathworks.com/help/matlab/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "mechanical design": {
        "courses": [
            {"title": "Machine Design (NPTEL)", "url": "https://nptel.ac.in/courses/112105124", "free": True},
        ],
        "videos": [
            {"title": "Machine Design Full Course", "url": "https://www.youtube.com/watch?v=RVFav42E_KA"},
        ],
        "docs": [{"title": "MIT OpenCourseWare - Mechanical Design", "url": "https://ocw.mit.edu/courses/mechanical-engineering/"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },
    "thermodynamics": {
        "courses": [
            {"title": "Thermodynamics (NPTEL)", "url": "https://nptel.ac.in/courses/112104113", "free": True},
        ],
        "videos": [
            {"title": "Thermodynamics Full Course", "url": "https://www.youtube.com/watch?v=VnGR86Hx0tM"},
        ],
        "docs": [{"title": "MIT OCW Thermodynamics", "url": "https://ocw.mit.edu/courses/mechanical-engineering/2-005-thermal-fluids-engineering-i-fall-2006/"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },
    "ros": {
        "courses": [
            {"title": "ROS for Beginners (Udemy)", "url": "https://www.udemy.com/course/ros-for-beginners/", "free": False},
        ],
        "videos": [
            {"title": "ROS2 Tutorial - Robotics Back-End", "url": "https://www.youtube.com/watch?v=0aPbWsyENA8"},
        ],
        "docs": [{"title": "ROS2 Official Docs", "url": "https://docs.ros.org/en/humble/"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },
    "control systems": {
        "courses": [
            {"title": "Control Systems (NPTEL)", "url": "https://nptel.ac.in/courses/108102043", "free": True},
        ],
        "videos": [
            {"title": "Control Systems - Brian Douglas", "url": "https://www.youtube.com/watch?v=oBc_BHxw78s&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk"},
        ],
        "docs": [{"title": "MIT OCW Control Systems", "url": "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-302-feedback-systems-spring-2007/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },

    # ── Electrical & Electronics ───────────────────────────────────────────
    "c": {
        "courses": [
            {"title": "C Programming (Coursera - Duke)", "url": "https://www.coursera.org/specializations/c-programming", "free": True},
        ],
        "videos": [
            {"title": "C Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=KJgsSFOSQv0"},
        ],
        "docs": [{"title": "C Reference", "url": "https://en.cppreference.com/w/c"}],
        "time": "4-6 weeks", "difficulty": "beginner",
    },
    "microcontrollers": {
        "courses": [
            {"title": "Embedded Systems with ARM (Coursera)", "url": "https://www.coursera.org/learn/introduction-embedded-systems", "free": True},
        ],
        "videos": [
            {"title": "STM32 Microcontroller Course", "url": "https://www.youtube.com/watch?v=EExZAQ_jtkA"},
        ],
        "docs": [{"title": "Arduino Getting Started", "url": "https://www.arduino.cc/en/Guide"}],
        "time": "5-7 weeks", "difficulty": "intermediate",
    },
    "rtos": {
        "courses": [
            {"title": "Real-Time OS (Udemy)", "url": "https://www.udemy.com/course/mastering-rtos-hands-on-with-freertos-arduino-and-stm32fx/", "free": False},
        ],
        "videos": [
            {"title": "FreeRTOS Tutorial", "url": "https://www.youtube.com/watch?v=F321087yYy4"},
        ],
        "docs": [{"title": "FreeRTOS Documentation", "url": "https://www.freertos.org/Documentation/RTOS_book.html"}],
        "time": "4-6 weeks", "difficulty": "advanced",
    },
    "verilog": {
        "courses": [
            {"title": "FPGA Design with Verilog (Udemy)", "url": "https://www.udemy.com/course/fpga-verilog-vhdl/", "free": False},
        ],
        "videos": [
            {"title": "Verilog Full Course - Neso Academy", "url": "https://www.youtube.com/watch?v=d6DA8HGOcKw&list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm"},
        ],
        "docs": [{"title": "ASIC World Verilog", "url": "https://www.asic-world.com/verilog/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
    "vhdl": {
        "courses": [
            {"title": "VHDL & FPGA Design (Udemy)", "url": "https://www.udemy.com/course/vhdl-and-fpga-development-for-beginners-and-intermediates/", "free": False},
        ],
        "videos": [
            {"title": "VHDL Tutorial - Neso Academy", "url": "https://www.youtube.com/watch?v=EHDFo886MuI"},
        ],
        "docs": [{"title": "VHDL Reference", "url": "https://www.ics.uci.edu/~jmoorkan/vhdlref/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
    "fpga": {
        "courses": [
            {"title": "FPGA Design (Coursera)", "url": "https://www.coursera.org/learn/intro-fpga-design-embedded-systems", "free": True},
        ],
        "videos": [
            {"title": "FPGA Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=lLg1AgA2Xoo"},
        ],
        "docs": [{"title": "Xilinx Documentation", "url": "https://docs.xilinx.com/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
    "pcb design": {
        "courses": [
            {"title": "PCB Design with KiCad (Udemy)", "url": "https://www.udemy.com/course/kicad-pcb-design/", "free": False},
        ],
        "videos": [
            {"title": "KiCad PCB Design Tutorial", "url": "https://www.youtube.com/watch?v=vaCVh2SAZY4"},
        ],
        "docs": [{"title": "KiCad Documentation", "url": "https://docs.kicad.org/"}],
        "time": "3-5 weeks", "difficulty": "intermediate",
    },
    "plc programming": {
        "courses": [
            {"title": "PLC Programming (Udemy)", "url": "https://www.udemy.com/course/plc-programming-from-scratch/", "free": False},
        ],
        "videos": [
            {"title": "PLC Programming Tutorial", "url": "https://www.youtube.com/watch?v=_2w9JO7BKWA"},
        ],
        "docs": [{"title": "PLC Manual", "url": "https://www.plcmanual.com/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "mqtt": {
        "courses": [
            {"title": "MQTT Essentials (HiveMQ - Free)", "url": "https://www.hivemq.com/mqtt-essentials/", "free": True},
        ],
        "videos": [
            {"title": "MQTT Tutorial", "url": "https://www.youtube.com/watch?v=EIxdz-2rhLs"},
        ],
        "docs": [{"title": "MQTT.org", "url": "https://mqtt.org/getting-started/"}],
        "time": "1-2 weeks", "difficulty": "intermediate",
    },

    # ── Civil Engineering ──────────────────────────────────────────────────
    "staad pro": {
        "courses": [
            {"title": "STAAD Pro Complete Course (Udemy)", "url": "https://www.udemy.com/course/staad-pro/", "free": False},
        ],
        "videos": [
            {"title": "STAAD Pro Full Tutorial", "url": "https://www.youtube.com/watch?v=9VLFGzTqz94"},
        ],
        "docs": [{"title": "Bentley STAAD Docs", "url": "https://docs.bentley.com/LiveContent/web/STAAD.Pro%20Help/en/GUID-18E3F2BA-10E2-40B3-9365-45C393B4DD28.html"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "etabs": {
        "courses": [
            {"title": "ETABS Complete Course (Udemy)", "url": "https://www.udemy.com/course/etabs-complete-course/", "free": False},
        ],
        "videos": [
            {"title": "ETABS Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=RFqaUswMeMg"},
        ],
        "docs": [{"title": "CSi ETABS Documentation", "url": "https://www.csiamerica.com/products/etabs/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "revit": {
        "courses": [
            {"title": "Revit Complete Course (Udemy)", "url": "https://www.udemy.com/course/autodesk-revit-architecture/", "free": False},
        ],
        "videos": [
            {"title": "Revit Full Course for Beginners", "url": "https://www.youtube.com/watch?v=EE5WjBLFb_I"},
        ],
        "docs": [{"title": "Autodesk Revit Help", "url": "https://help.autodesk.com/view/RVT/2025/ENU/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "bim": {
        "courses": [
            {"title": "BIM Fundamentals (Coursera)", "url": "https://www.coursera.org/learn/bim-fundamentals", "free": True},
        ],
        "videos": [
            {"title": "BIM Explained", "url": "https://www.youtube.com/watch?v=C-dPLqMFoI0"},
        ],
        "docs": [{"title": "Autodesk BIM Resources", "url": "https://www.autodesk.com/solutions/bim"}],
        "time": "3-4 weeks", "difficulty": "intermediate",
    },
    "structural analysis": {
        "courses": [
            {"title": "Structural Engineering (NPTEL)", "url": "https://nptel.ac.in/courses/105106049", "free": True},
        ],
        "videos": [
            {"title": "Structural Analysis Full Course", "url": "https://www.youtube.com/watch?v=F7n5V3xqVbQ"},
        ],
        "docs": [{"title": "MIT OCW Structural Analysis", "url": "https://ocw.mit.edu/courses/civil-and-environmental-engineering/"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },
    "gis": {
        "courses": [
            {"title": "GIS Specialization (Coursera - UC Davis)", "url": "https://www.coursera.org/specializations/gis", "free": True},
        ],
        "videos": [
            {"title": "GIS Full Course", "url": "https://www.youtube.com/watch?v=TAbGVXJVqXQ"},
        ],
        "docs": [{"title": "QGIS Documentation", "url": "https://docs.qgis.org/3.28/en/docs/"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },

    # ── Additional IT Skills ───────────────────────────────────────────────
    "solidity": {
        "courses": [
            {"title": "Blockchain Specialization (Coursera)", "url": "https://www.coursera.org/specializations/blockchain", "free": True},
        ],
        "videos": [
            {"title": "Solidity Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=gyMwXuJrbJQ"},
        ],
        "docs": [{"title": "Solidity Official Docs", "url": "https://docs.soliditylang.org/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
    "unity": {
        "courses": [
            {"title": "Unity Game Development (Udemy)", "url": "https://www.udemy.com/course/unitycourse/", "free": False},
        ],
        "videos": [
            {"title": "Unity Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=gB1F9G0JXOo"},
        ],
        "docs": [{"title": "Unity Documentation", "url": "https://docs.unity3d.com/Manual/"}],
        "time": "6-8 weeks", "difficulty": "intermediate",
    },
    "c#": {
        "courses": [
            {"title": "C# Fundamentals (Pluralsight)", "url": "https://www.pluralsight.com/courses/csharp-fundamentals-dev", "free": False},
        ],
        "videos": [
            {"title": "C# Full Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=GhQdlMFylQ8"},
        ],
        "docs": [{"title": "Microsoft C# Docs", "url": "https://learn.microsoft.com/en-us/dotnet/csharp/"}],
        "time": "4-6 weeks", "difficulty": "beginner",
    },
    "cisco": {
        "courses": [
            {"title": "Cisco CCNA (Udemy)", "url": "https://www.udemy.com/course/ccna-complete/", "free": False},
        ],
        "videos": [
            {"title": "CCNA Full Course - NetworkChuck", "url": "https://www.youtube.com/watch?v=rv3QK2UquxM"},
        ],
        "docs": [{"title": "Cisco Learning Network", "url": "https://learningnetwork.cisco.com/"}],
        "time": "8-12 weeks", "difficulty": "intermediate",
    },
    "networking": {
        "courses": [
            {"title": "Computer Networking (Coursera - Google)", "url": "https://www.coursera.org/learn/computer-networking", "free": True},
        ],
        "videos": [
            {"title": "Computer Networking Course - freeCodeCamp", "url": "https://www.youtube.com/watch?v=qiQR5rTSshw"},
        ],
        "docs": [{"title": "Cisco Networking Basics", "url": "https://www.netacad.com/courses/networking"}],
        "time": "4-6 weeks", "difficulty": "intermediate",
    },
    "signal processing": {
        "courses": [
            {"title": "Digital Signal Processing (Coursera)", "url": "https://www.coursera.org/learn/dsp", "free": True},
        ],
        "videos": [
            {"title": "Signal Processing - NPTEL", "url": "https://www.youtube.com/watch?v=hVOA8VtKLgk"},
        ],
        "docs": [{"title": "MIT OCW Signals & Systems", "url": "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-003-signals-and-systems-fall-2011/"}],
        "time": "6-8 weeks", "difficulty": "advanced",
    },
}


def get_skill_resources(skill_name):
    """Get learning resources for a specific skill."""
    key = skill_name.lower().strip()
    return SKILL_RESOURCES.get(key, None)


def build_learning_roadmap(missing_core, missing_important, missing_nice):
    """
    Build a phased learning roadmap from missing skills with resources.

    Args:
        missing_core: list of missing core skill names
        missing_important: list of missing important skill names
        missing_nice: list of missing nice-to-have skill names

    Returns:
        list of phases, each with name, icon, color, and skills (with resources)
    """
    phases = []

    def _build_skills(skill_list):
        items = []
        for skill in skill_list:
            resources = get_skill_resources(skill)
            items.append({
                "name": skill,
                "resources": resources or _default_resources(skill),
            })
        return items

    if missing_core:
        phases.append({
            "name": "Phase 1 — Master Core Skills",
            "icon": "🔴",
            "color": "core",
            "description": "These are must-have skills. Prioritize learning these first.",
            "skills": _build_skills(missing_core),
        })

    if missing_important:
        phases.append({
            "name": "Phase 2 — Build Important Skills",
            "icon": "🟡",
            "color": "important",
            "description": "These skills significantly strengthen your profile.",
            "skills": _build_skills(missing_important),
        })

    if missing_nice:
        phases.append({
            "name": "Phase 3 — Add Bonus Skills",
            "icon": "🟢",
            "color": "nice",
            "description": "These give you an extra edge over other candidates.",
            "skills": _build_skills(missing_nice),
        })

    return phases


def _default_resources(skill_name):
    """Generate default resource links for skills not in the database."""
    query = skill_name.replace(" ", "+")
    return {
        "courses": [
            {"title": f"Search Coursera for {skill_name}", "url": f"https://www.coursera.org/search?query={query}", "free": True},
        ],
        "videos": [
            {"title": f"Search YouTube for {skill_name} tutorial", "url": f"https://www.youtube.com/results?search_query={query}+full+course"},
        ],
        "docs": [
            {"title": f"Search Google for {skill_name} documentation", "url": f"https://www.google.com/search?q={query}+documentation"},
        ],
        "time": "2-4 weeks",
        "difficulty": "intermediate",
    }
