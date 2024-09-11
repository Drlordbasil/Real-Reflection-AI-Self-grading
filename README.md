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
   Idea eval and idea gen:
   Idea:
   **Improved Idea:**
   
   Create a decentralized, open-source, and autonomous Python application that rewards users for contributing their idle computing resources to scientific research projects, data analysis, and machine learning tasks. The application will utilize a novel tokenomics system, leveraging the Proof of Participation (PoP) consensus algorithm to mint and distribute a unique cryptocurrency, called "UBI Coin," to users who contribute their computing resources.
   
   **Solution:**
   
   This idea leverages the concept of distributed computing, where users contribute their idle computing resources to a network, solving complex problems or performing tasks in the background. The application would:
   
   1. Utilize the BOINC (Berkeley Open Infrastructure for Network Computing) framework, an open-source platform that allows users to volunteer their computing resources to various scientific projects.
   2. Implement the Proof of Participation (PoP) consensus algorithm, which rewards users for contributing their computing resources to the network.
   3. Develop a user-friendly interface using Python libraries like Tkinter or PyQt, enabling users to easily install, configure, and run the application.
   4. Create a novel tokenomics system, where UBI Coin is minted and distributed to users based on their contribution to the network.
   
   **Modified Code Structure:**
   ```python
   import tkinter as tk
   from tkinter import ttk
   import requests
   import json
   from boinc import boinc
   from pop import PoP
   
   class UBI_Application:
       def __init__(self, root):
           self.root = root
           self.root.title("UBI Application")
   
           # Initialize BOINC client
           self.boinc_client = boinc.BoincClient()
   
           # Initialize PoP client
           self.pop_client = PoP()
   
           # Create GUI elements
           self.create_widgets()
   
       def create_widgets(self):
           # Create start/stop button
           self.start_button = ttk.Button(self.root, text="Start", command=self.start_boinc)
           self.start_button.pack()
   
           # Create status label
           self.status_label = ttk.Label(self.root, text="Idle")
           self.status_label.pack()
   
       def start_boinc(self):
           # Start BOINC client
           self.boinc_client.start()
   
           # Schedule tasks using BOINC's RPC interface
           self.boinc_client.rpc('schedule_tasks', [])
   
           # Initialize PoP client and start minting UBI Coin
           self.pop_client.start()
   
       def monitor_progress(self):
           # Periodically check BOINC client's progress
           progress = self.boinc_client.rpc('get_progress', [])
   
           # Update PoP client with progress
           self.pop_client.update(progress)
   
   if __name__ == "__main__":
       root = tk.Tk()
       app = UBI_Application(root)
       root.mainloop()
   ```
   This modified code creates a basic GUI application that starts the BOINC client and schedules tasks. It then initializes the PoP client and starts minting UBI Coin based on the user's contribution to the network.
   
   **Additional Functionality:**
   
   To further improve the solution, the application can include additional features, such as:
   
   * A decentralized market for UBI Coin, allowing users to exchange their tokens for goods and services.
   * A system for staking UBI Coin, enabling users to earn interest on their tokens.
   * A mechanism for voting on proposals for the development of the UBI Coin ecosystem.
   
   **Tokenomics:**
   
   The UBI Coin tokenomics system will be designed to incentivize users to contribute their computing resources to the network. The system will include the following features:
   
   * Token supply: 10 billion UBI Coins will be minted initially, with a annual inflation rate of 2%.
   * Token distribution: 50% of the tokens will be distributed to users based on their contribution to the network, 20% will be allocated to the development team, and 30% will be reserved for future development and partnerships.
   * Token velocity: The token velocity will be designed to encourage users to hold their tokens for the long term, rather than selling them immediately.
   
   **Scalability:**
   
   As the number of users increases, the application's scalability is ensured through the decentralized BOINC framework, which can handle a large number of computing resources. Additionally, the use of the PoP consensus algorithm allows for a high level of security and decentralization, ensuring that the network remains secure and resilient.
   
   **Conclusion:**
   
   This improved idea leverages Python, BOINC, and the Proof of Participation consensus algorithm to create a UBI temporary solution that meets the constraints. The application rewards users for contributing their idle computing resources, providing a basic income without requiring initial capital or resources. The novel tokenomics system and the use of the PoP consensus algorithm ensure a high level of security, decentralization, and scalability, making this solution suitable for a large-scale deployment.
   
   Evaluation:
   Novelty: 8
   The idea of leveraging idle computing resources to generate a Universal Basic Income (UBI) is innovative, and the use of the Proof of Participation (PoP) consensus algorithm and the BOINC framework adds a unique twist.
   
   Feasibility: 7
   The idea is technically feasible, but implementing the PoP consensus algorithm, creating a user-friendly interface, and developing a tokenomics system can be challenging. Additionally, the BOINC framework has limitations in terms of scalability and decentralization.
   
   Scalability: 6
   While the BOINC framework can handle a large number of computing resources, it may face scalability issues as the number of users grows. Furthermore, the PoP consensus algorithm's ability to handle high transaction volumes is uncertain.
   
   Social impact: 9
   If successful, this idea can have a significant social impact by providing a basic income to individuals in need, without relying on initial capital or resources. It also promotes decentralized and secure computing, which can contribute to the well-being of many communities.
   
   Sustainability: 8
   The idea is sustainable in the long term, as it leverages existing computing resources and incentivizes users to contribute their idle resources. However, the tokenomics system may require continued development and growth to maintain its value and momentum.
   
   Accessibility: 8
   The idea is accessible to individuals with basic computer skills, but setting up the required software and hardware might be challenging for those without prior experience.
   
   Constraint compliance: 9
   The idea meets most of the constraints, including being a UBI temporary solution, created in Python, runnable on any PC, and no requirement for credentials, initial capital, or resources. However, the cost and feasibility of creating a new decentralized market or staking mechanism may be uncertain.
   
   Overall score: 7.6
   
   Strengths:
   1. Unique approach to generating UBI using idle computing resources
   2. Potential for high social impact and promoting decentralized, secure computing
   3. Novel tokenomics system leveraging PoP consensus algorithm
   
   Weaknesses:
   1. Dependence on BOINC framework's scalability and decentralization
   2. High technical difficulty in implementing PoP consensus algorithm and tokenomics system
   3. Uncertainty in high transaction volumes' impact on the network
   
   Improvement suggestions:
   1. Collaborate with existing BOINC projects or adapt them to improve decentralization and scalability.
   2. Develop and integrate decentralized solutions for market and staking mechanisms to increase tokenomics' feasibility and long-term momentum.
   3. Establish strategic partnerships to promote the UBI application, develop new tokenomics, or expand its scope and reach.
   
   Overall Score: 7.60
   Sentiment: 0.12
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
