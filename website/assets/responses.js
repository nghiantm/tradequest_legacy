function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }

    //123
    if (input == "tell me about this website") {
        return "This is the best simulator ever!";
    }

    return "Please ask something else. I'm not able to answer that right now."
}