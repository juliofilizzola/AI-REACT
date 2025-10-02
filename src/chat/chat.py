class Chat:
    llm = None
    def __init__(self, llm):
        self.llm = llm

    def send_message(self, message):
        """
        Send a message to the chat model and return the response.

        Args:
            message (str): The message to send to the chat model.

        Returns:
            response (dict): The response from the chat model.
        """
        response = self.llm.invoke(message)
        return response
    
    