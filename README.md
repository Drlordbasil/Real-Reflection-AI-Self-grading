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
   ```
   git clone https://github.com/yourusername/Real-Reflection-AI-Self-grading.git
   cd Real-Reflection-AI-Self-grading
   ```

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

- OpenAI for their powerful language models
- Groq for their API services
- The open-source community for various libraries and tools used in this project