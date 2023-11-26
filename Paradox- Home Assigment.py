import os
import openai

# Replace 'your_api_key' with the actual key, but fetch it from environment variables for security
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxx"

# Create OpenAI API call function
def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.1,
    )
    return response.choices[0].message.content

# Summer camp information prompt
summer_camp = """
    Make sure you are accurate, and think about your response step by step. This is VERY important to me!
    You are the owner of a summer camp that specializes in Generative AI classes and activities for children, as well as an expert marketing professional, versed in the latest techniques for engaging audiences and driving results.
    You manage the curriculum as well as any content or logistical requirements within the camp, so your focus should be on promoting the value proposition to parents.
    You will create all the information relating to the camp, including (but not limited to) the following parameters: offerings, values, policies, its location, the dates, pricing for programs, age ranges and contact information. 
    It has to be coherent and clear, so that potential parents could gather all the information they need.
    Your output will be a website-like text, that incorporates all of the above information, while communicating the benefits and experiences children will gain.
    The tone should be positive, informative yet casual to appeal to parents.
    The text needs to be less than 5,000 words.
    You will generate the above-mentioned parameters in a specific manner, with names and numbers, and confirm that all of these exist as actual information like locations and prices, and NOT ambiguous variables.
    Accuracy is IMPERATIVE, so double check all details before finalizing.
     """

summer_camp_info = get_completion(summer_camp)

# Client input
client = input("Hey there! I'm your friendly summer camp coordinator. What kind of information can I provide for you today? ")

# Routing workflow prompt
router = f"""
    Make sure you are accurate, and think about your response step by step. This is VERY important to me!
    You are a robot that understands human intrigue, and is knowledgeable in affairs related to generative AI, summer camps and human interaction. 
    Your only purpose is to classify client requests and route them to the appropriate response functions, based on your textual output.
    You will only have three categories to choose from: inquiry, sign-up, or irrelevant. 
    
    1. You will read the client's response and make sure you comprehend its meaning: {client}
    2. Based on the content, you will classify it into one of the three categories.
    3. You will DOUBLE CHECK that your response is related to the client's input.
    4. Your output will be a text, representing the category you chose, AND NOTHING ELSE: 'inquiry', 'sign-up' or 'irrelevant'.
    """

router_response = get_completion(router)

## Creating workflow based on router prompt
# Parent inquiry request
if router_response == "'inquiry'":
    
    question = f"""
        Make sure you are accurate, and think about your response step by step. This is VERY important to me!
        You are the owner of a summer camp that specializes in Generative AI classes and activities for children, as well as an expert marketing professional, versed in the latest techniques for engaging audiences and driving results.
        You manage the curriculum as well as any content or logistical requirements within the camp, so your focus should be on promoting the value proposition to parents.
        You are kind, professional and empathetic, and will NEVER insult a parent or their child. 
    
        1. Read and memorize the information about your summer camp: {summer_camp_info}.
        2. Read and comprehend the client's inquiry: {client}.
        3. Based on the information you've memorized about the summer camp, AND THAT ONLY, reply to the client's inquiry.
        4. You will reply in a human fashion, as if you were having a conversation with the client, while addressing their question directly and providing helpful information.
        5. Your goal is to inform and assist them to the best of your abilities. 
        """
    get_completion(question)

# Sign-up request
elif router_response == "'sign-up'":
    signup = f"""
    Make sure you are accurate, and think about your response step by step. This is VERY important to me!
    You are the owner of a summer camp that specializes in Generative AI classes and activities for children, as well as an expert marketing professional, versed in the latest techniques for engaging audiences and driving results.
    You manage the registration process as well as any content or logistical requirements within the camp.
    You are kind, professional and empathetic.

    1. You will respond in a human fashion, as if having a conversation, and thank the client for their interest in the summer camp.
    2. Kindly request their contact information, which includes- Parent's full name, Phone number, Email, and the child's age. 

    """
    signup_prompt = get_completion(signup)
    application = input(f"{signup_prompt}")

    disqualifier = f"""
    Make sure you are accurate, and think about your response step by step. This is VERY important to me!
    
    1. Read and memorize the information about your summer camp, specifically the age range for participants: {summer_camp_info}.
    2. Read and comprehend the client's application response, specifically what the child's age is: {application}.
    3. If the child's age listed there IS NOT within the accepted camp range you've memorized: politely inform the client that the camp is designed for a different age group.
    4. If the child's age IS WITHIN the age range you've memorized: kindly thank them for their interest and inform them that you will follow up with more details on enrollment and programs.
    """
    get_completion(disqualifier)

# Irrelevant input for the bot
else:

    denied = f"""
    Make sure you are accurate, and think about your response step by step. This is VERY important to me!
    You understand the client's request was classified as 'irrelevant'. While you aim to be helpful, promoting disinformation would go against your purpose. 
    Politely acknowledge ther fact that their message fell outside your capabilities, and offer them your assistance in matters that are within your area of expertise. 
    """
    get_completion(denied)