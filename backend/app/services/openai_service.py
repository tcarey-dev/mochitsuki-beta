from ..core.config import settings

import openai


class OpenAIService:
    @staticmethod
    async def get_flashcard(deck_in, text_in, parent_in=None):
        openai.api_key = settings.OPENAI_KEY
        token_usage = 0
        role_content = "You are an assistant that helps to make and correctly format text for use as flashcards."
        user_content = f"""Please perform the following steps on the text given after "Text input:" below:
        - Extract and condense the most important details of the text
        - Use these bullet points to generate flash card style question and answer pairs
        - Always begin a question with "Q:"
        - You MUST ABSOLUTELY ALWAYS begin an answer with "A:" on a new line, followed by a new line
        - When providing bullet points in an answer, use a hyphen (-) followed by a space and start each point on a new line
        - If the text contains code blocks, use code examples in your questions and answers as appropriate, using markdown to format the examples as a code block
        - Be sure to include any important context in the question portion
        - Format the answers in concise bullet points

        Here's an example of the desired format:
        Q: What are creational design patterns?
        A:
        - Design patterns dealing with object creation mechanisms
        - Meant to create objects in a suitable manner for the situation
        - Solve design problems and reduce added complexity

        Now, apply these instructions to the text input below:
        Text input:
        {text_in}
        """
        request = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": role_content},
                {"role": "user", "content": user_content}
            ],
            temperature=0.5
        )

        return request['choices'][0]['message']['content']