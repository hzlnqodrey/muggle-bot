from random import choice, randint

def get_response(user_input: str) -> str:

    lowered: str = user_input.lower()

    if lowered == ' ':
        return "I'm Sorry, I didn't catch that. Could you repeat it?"
    elif 'hello' in lowered:
        return "Hello! How can I help you today?"
    elif 'flip coin' in lowered:
        return choice(['Heads', 'Tails'])
    else:
        return choice([
            'I am sorry, I do not understand.',
            'What do you mean?',
            'Are you sure about that?',
            'I am not sure what you are talking about.',
            'I can not help you with that.',
        ])
