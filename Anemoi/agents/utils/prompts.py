import os


def get_tools_description():
    return f"""

Don't try to guess any numbers or facts or make and estimation, only use reliable sources. If you are unsure, ask other agents for help.
Never try to ask user for help, user can't not observer you infomration.
Do not arbitrarily distort the meaning of the question; for example, do not add qualifiers to the given conditions.

-- Using threads --
You have the ability to create communication threads with other agents. This allows you to collaborate on tasks, share information, and work together to solve problems. You can create a thread by using the `create_thread` tool, which will allow you to specify the agents you want to collaborate with.
Agents not in a thread will not be able to see the messages in that thread. The messages in closed threads will not be visible to you or other agents, though the summary will.
Since agents are powered by LLMs, they can get confused if there are too many messages to look at at once. Therefore, it is recommended to create threads for each task or topic you are working on, and to close them when there is too much going on. This will help keep the conversation focused and organized.

-- Agent descriptions --
- **answer_finding_agent**: This agent is responsible for submitting the final answer. It will be working with the planning agent to ensure the answer is formatted correctly and meets the task requirements. 
- **web_agent**: This agent is a helpful assistant that can search the web, extract webpage content, simulate browser actions, and retrieve relevant information.
- **document_processing_agent**: This agent is a helpful assistant that can process a variety of local and remote documents, including pdf, docx, images, audio, and video, etc.
- **reasoning_coding_agent**: This agent is a helpful assistant that specializes in reasoning, coding, running code script and processing excel files. However, it cannot access the internet to search for information. If the task requires python execution, it should be informed to execute the code after writing it.
- **critique_agent**: This agent is responsible for reviewing and critiquing the work of other agents. It can provide feedback, suggestions, and improvements to ensure the quality of the output. Think of this agent and the answer_finding agent as the closest to the user.

Always let the critique agent have a look at your work before letting it become a consensus, assumption, or final answer. The critique agent will review your work and provide feedback, suggestions, and improvements to ensure the quality of the output.
If you have exhausted all avenues for new information and appear to be limited, let the reasoning_coding_agent attempt to get the required information using code/API, installing whichever libraries are required, and running the code.

Also, remember to question everything yourself too. 

-- Start of messages and status --

<resource>coral://{os.getenv("CORAL_CONNECTION_URL").split("http://")[1]}</resource>
-- End of messages and status --
    """

#     -- Start of messages and status --

# <resource>coral://{os.getenv("CORAL_CONNECTION_URL").split("http://")[1]}</resource>
# -- End of messages and status --

def get_coral_tools_description():
    return get_tools_description()
def get_user_message():
    return "[automated] continue collaborating with other agents towards the task. Remember to keep in mind the task's exact wording and approach 100% certainty about the answer. you must use the send_messsage tool and pass your messages to other agents for them and me to see them."
