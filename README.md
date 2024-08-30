# EduGenie: an-Ed-tech QnA llm based system 
This is a comprehensive LLM project utilizing Google Palm and Langchain. Basically, a Q&A system for an ed-tech company that offers data-related courses and bootcamps. With thousands of learners reaching out via Discord or email, this system will feature a Streamlit-based user interface allowing students to ask questions and receive answers.

# Project Highlights-

1)Utilize an CSV file of FAQs.

2)This file aids human staff in supporting course learners.

3)We will develop an LLM-based Q&A system to alleviate the workload of their staff.

4)Students will be able to ask questions directly through the system and receive answers within seconds.

# Key concepts - 

1)Langchain + Google Palm: LLM based Q&A

2)Streamlit: UI

3)Huggingface instructor embeddings: Text embeddings

4)FAISS: Vector database

# Usage- 

1)Locate to the path of your directory in your command prompt.For example - cd  C:\Users\LATISHA\Downloads\EduGenie

2)Set GOOGLE_API_KEY=your_api_key

3)Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
   
4)Run the Streamlit app by executing:
streamlit run main.py

# Sample Questions-

Do you guys provide internship and also do you offer EMI payments?

Do you have javascript course?

Should I learn power bi or tableau?

what about placement assistance?

# Project Structure-

1)main.py: The main Streamlit application script.

2)langchain_helper.py: This has all the langchain code

3)requirements.txt: A list of required Python packages for the project.

4).env: Configuration file for storing your Google API key.
