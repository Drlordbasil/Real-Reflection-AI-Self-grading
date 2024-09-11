# Real Reflection AI Self-grading

Real Reflection AI Self-grading is an innovative project that leverages advanced AI technologies to create a self-improving chatbot system. This system can search the internet, scrape websites, analyze images, generate ideas, and grade its own responses to continuously enhance its performance.

## Features

- 🤖 AI-powered chatbot with self-grading capabilities
- 🌐 Web scraping and Google search integration
- 🖼️ Image analysis using vision AI
- 📊 Response grading and improvement
- 🚀 Function calling for extended capabilities
- 💡 Idea generation and refinement
- 📈 Benchmark testing and visualization

## Components

1. `benchmark_testing.py`: Runs comprehensive benchmarks on the AI system's performance.
2. `chat_flow.py`: Manages the conversation flow and self-grading process.
3. `generate_idea.py`: Generates and refines innovative ideas based on given constraints.
4. `caching.py`: Implements a caching system to improve performance.
5. `config.py`: Contains configuration settings for the project.
6. `function_calling_usage.py`: Handles API calls and function execution.
7. `tools_functions.json`: Defines available tools and functions for the AI.
8. `website_scraper.py`: Scrapes websites for content.
9. `grade_response_with_llm.py`: Grades AI responses using language models.
10. `image_vision_usage.py`: Analyzes images using AI vision capabilities.

## Setup

1. Clone the repository:


2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root and add your API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. Run benchmark tests:
   ```
   python benchmark_testing.py
   ```

2. Generate and refine ideas:
   ```
   python generate_idea.py
   Idea eval:
   Idea evaluation:
   Novelty: 6
   The idea of using Wikipedia's content on climate modeling to evaluate the concept is not novel, but the context of using it for social entrepreneurship is somewhat unique.
   
   Feasibility: 7
   The idea is feasible as it does not require any specific skills or resources, but it relies on the availability of accurate information on Wikipedia.
   
   Scalability: 5
   The idea has limited scalability as it relies on a single source of information and may not be able to accommodate a large number of users.
   
   Social impact: 8
   The idea has the potential to create a significant social impact by providing accurate information on climate modeling and its implications.
   
   Sustainability: 6
   The idea is sustainable as it relies on a publicly available source of information and does not require any specific resources.
   
   Accessibility: 8
   The idea is highly accessible as it can be accessed by anyone with an internet connection.
   
   Constraint compliance: 9
   The idea meets all the constraints as it is created in Python code, does not use credentials, is free to start, and does not rely on selling or trading.
   
   Overall score: 6.9
   
   Strengths:
   
   1. High accessibility: The idea can be accessed by anyone with an internet connection, making it highly accessible.
   2. High social impact: The idea has the potential to create a significant social impact by providing accurate information on climate modeling and its implications.
   3. Compliance with constraints: The idea meets all the constraints, making it a viable solution.
   
   Weaknesses:
   
   1. Limited scalability: The idea has limited scalability as it relies on a single source of information and may not be able to accommodate a large number of users.
   2. Limited novelty: The idea is not highly novel, but the context of using it for social entrepreneurship is somewhat unique.
   3. Relying on a single source of information: The idea relies on Wikipedia as the sole source of information, which may not be comprehensive or accurate.
   
   Improvement suggestions:
   
   1. Diversify sources of information: To improve the idea, consider diversifying the sources of information to include other credible sources, such as academic journals or government reports.
   2. Develop a more interactive platform: To increase scalability and engagement, consider developing a more interactive platform that allows users to engage with the information in different ways, such as through quizzes or games.
   3. Develop a feedback mechanism: To improve the accuracy and comprehensiveness of the information, consider developing a feedback mechanism that allows users to provide feedback and suggestions for improvement.  
   ``` 

3. To use the chatbot in your own application, import the `ChatFlow` class from `chat_flow.py`:
   ```python
   from chat_flow import ChatFlow
   
   chat_flow = ChatFlow()
   response = chat_flow.chat("Your prompt here")
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for their library
- Groq for their API services
- The open-source community for various libraries and tools used in this project
