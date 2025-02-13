from textblob import TextBlob 

userInput = input("Insert Text: ")

text = userInput.lower()

#List of school related terms 

associationList = ["school", "college", "university", "student", "professor", "lecture", "class", "course", 
                   "major", "minor", "degree", "dormitory", "campus", "tuition", "scholarship", 
                   "student loans", "financial aid", "gpa", "credits", "semester", "quarter", 
                   "registration", "syllabus", "final exam", "midterm", "assignment", "essay", 
                   "group project", "study group", "graduation", "capstone", "thesis", "dissertation", 
                   "internship", "research", "lab", "academic advisor", "office hours", "commencement", 
                   "valedictorian", "academic probation", "academic dismissal", "drop out", "withdraw", 
                   "academic calendar", "transfer credits", "student id", "student union", "residence hall", 
                   "roommate", "meal plan", "cafeteria", "study abroad", "extracurricular", "fraternity", 
                   "sorority", "greek life", "student organization", "student club", "library", "career fair", 
                   "resume", "cover letter", "job interview", "career services", "work-study", "campus job", 
                   "part-time student", "full-time student", "online classes", "distance learning", "hybrid classes", 
                   "learning management system", "blackboard", "canvas", "moodle", "bachelor's degree", "master's degree", 
                   "doctorate", "phd", "alumni", "graduate student", "undergraduate", "freshman", "sophomore", "junior", 
                   "senior", "academic freedom", "academic integrity", "plagiarism", "cheating", "honor code", "student conduct", 
                   "disciplinary hearing", "appeal process", "on-campus housing", "off-campus housing", "roommate agreement", 
                   "campus security", "student parking", "parking pass", "study lounge", "study carrel", "academic resource center", 
                   "tutoring services", "writing center", "math lab", "language lab", "library reserve", "research project", 
                   "teaching assistant", "research assistant", "graduate assistant", "fellowship", "student discount", 
                   "counseling center", "mental health", "career counseling", "student debt", "loan forgiveness", "prerequisite", 
                   "elective", "core curriculum", "general education", "learning styles", "study habits", "time management", 
                   "critical thinking", "academic writing", "research skills", "peer review", "peer tutoring", "personal statement", 
                   "academic portfolio", "extracurricular activities", "campus involvement", "community service", "campus rec",
                     "intramural sports", "campus dining", "student ambassador", "student government", "dean's list", "honors program",
                    "double major", "academic goals", "graduation requirements", "post-graduation plans", "alumni network", "career readiness"]


blob = TextBlob(text) #turns the str to a textblob where the textblob could analyze the text

sentiment = blob.polarity 

if any(word in text for word in associationList):  # Check if any word is in the text
    if sentiment < 0:
        print("Aw, that's too bad. I hope the best for you in your academic endeavors.")
    elif sentiment == 0:
        print("I hope you have a better time at school!")
    else:
        print("That sounds great! Have a nice day!")

